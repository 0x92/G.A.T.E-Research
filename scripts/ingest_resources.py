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
    records: List[Dict[str, str | List[str]]] = []
    for base in RESOURCE_DIRS:
        if not os.path.exists(base):
            continue
        for root, _, files in os.walk(base):
            for fname in files:
                ext = os.path.splitext(fname)[1].lower()
                if ext in {".html", ".htm", ".pdf", ".jpg", ".jpeg", ".png", ".gif"}:
                    path = os.path.join(root, fname)
                    try:
                        records.append(build_metadata(path))
                    except Exception as exc:
                        print(f"Skipping {path}: {exc}")
    os.makedirs("data", exist_ok=True)
    with open("data/index.json", "w", encoding="utf-8") as fh:
        json.dump(records, fh, indent=2, ensure_ascii=False)


if __name__ == "__main__":
    main()
