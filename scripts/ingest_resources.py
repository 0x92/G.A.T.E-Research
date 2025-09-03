#!/usr/bin/env python3
"""Ingest resources and generate a metadata index.

Walk through the ``ressources`` and ``images`` directories and extract basic
metadata from HTML, PDF and image files. The resulting data are stored in
``data/index.json``.
"""
from __future__ import annotations

import hashlib
import json
import os
from datetime import datetime
from typing import List, Dict

from bs4 import BeautifulSoup
import pdfplumber
import pytesseract
import spacy
from PIL import Image
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation

RESOURCE_DIRS: List[str] = ["ressources", "images"]
TAG_KEYWORDS: List[str] = ["GATE", "MKULTRA"]


def get_tags(path: str) -> List[str]:
    """Return tags based on keywords present in *path*."""
    upper = path.upper()
    return [tag for tag in TAG_KEYWORDS if tag in upper]


def extract_html_title(path: str) -> str:
    """Return the HTML page title if available."""
    try:
        with open(path, "r", encoding="utf-8", errors="ignore") as fh:
            soup = BeautifulSoup(fh, "html.parser")
            if soup.title and soup.title.string:
                return soup.title.string.strip()
    except Exception:
        pass
    return os.path.basename(path)


def extract_pdf_title(path: str) -> str:
    """Return the PDF title if available."""
    try:
        with pdfplumber.open(path) as pdf:
            title = pdf.metadata.get("Title")
            if title:
                return title
    except Exception:
        pass
    return os.path.basename(path)


def extract_text(path: str) -> str:
    """Extract plain text from HTML or PDF files."""
    ext = os.path.splitext(path)[1].lower()
    try:
        if ext in {".html", ".htm"}:
            with open(path, "r", encoding="utf-8", errors="ignore") as fh:
                soup = BeautifulSoup(fh, "html.parser")
                return soup.get_text(" ", strip=True)
        if ext == ".pdf":
            with pdfplumber.open(path) as pdf:
                return "\n".join(page.extract_text() or "" for page in pdf.pages)
    except Exception:
        pass
    return ""


def extract_ocr_text(path: str) -> str:
    """Extract text from image files using Tesseract."""
    try:
        with Image.open(path) as img:
            return pytesseract.image_to_string(img)
    except Exception:
        return ""


def hash_file(path: str) -> str:
    """Return the SHA256 digest of a file."""
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()


def build_metadata(path: str) -> Dict[str, str | List[str]]:
    """Build a metadata record for *path*."""
    ext = os.path.splitext(path)[1].lower()
    stat = os.stat(path)
    metadata: Dict[str, str | List[str]] = {
        "id": hash_file(path)
        if ext in {".jpg", ".jpeg", ".png", ".gif"}
        else hashlib.sha256(path.encode()).hexdigest(),
        "title": os.path.basename(path),
        "date": datetime.fromtimestamp(stat.st_mtime).isoformat(),
        "source": "",
        "type": ext.lstrip("."),
        "filePath": path,
        "tags": get_tags(path),
    }
    if ext in {".html", ".htm"}:
        metadata["title"] = extract_html_title(path)
    elif ext == ".pdf":
        metadata["title"] = extract_pdf_title(path)
    return metadata


def main() -> None:
    nlp = spacy.load("en_core_web_sm")
    nlp.max_length = 2_000_000
    records: List[Dict[str, str | List[str]]] = []
    texts: List[str] = []
    text_indices: List[int] = []
    for base in RESOURCE_DIRS:
        if not os.path.exists(base):
            continue
        for root, _, files in os.walk(base):
            for fname in files:
                ext = os.path.splitext(fname)[1].lower()
                if ext in {".html", ".htm", ".pdf", ".jpg", ".jpeg", ".png", ".gif"}:
                    path = os.path.join(root, fname)
                    try:
                        metadata = build_metadata(path)
                        text = ""
                        ocr_text = ""
                        if ext in {".html", ".htm", ".pdf"}:
                            text = extract_text(path)
                        else:
                            ocr_text = extract_ocr_text(path)

                        analysis_text = text or ocr_text
                        if analysis_text:
                            doc = nlp(analysis_text)
                            metadata["entities"] = sorted({ent.text for ent in doc.ents})
                            texts.append(analysis_text)
                            text_indices.append(len(records))
                        else:
                            metadata["entities"] = []

                        if ocr_text:
                            metadata["ocrText"] = ocr_text

                        metadata["topics"] = []
                        records.append(metadata)
                    except Exception as exc:
                        print(f"Skipping {path}: {exc}")
    if texts:
        vectorizer = CountVectorizer(stop_words="english")
        dtm = vectorizer.fit_transform(texts)
        if dtm.shape[1] > 0:
            lda = LatentDirichletAllocation(n_components=5, random_state=0)
            doc_topic = lda.fit_transform(dtm)
            feature_names = vectorizer.get_feature_names_out()
            topic_words = [
                [feature_names[i] for i in topic.argsort()[:-6:-1]]
                for topic in lda.components_
            ]
            for idx, dist in zip(text_indices, doc_topic):
                top_topic = dist.argmax()
                records[idx]["topics"] = topic_words[top_topic]
    os.makedirs("data", exist_ok=True)
    with open("data/index.json", "w", encoding="utf-8") as fh:
        json.dump(records, fh, indent=2, ensure_ascii=False)


if __name__ == "__main__":
    main()
