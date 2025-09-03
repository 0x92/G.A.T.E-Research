from __future__ import annotations

import json
import os
import csv
import tempfile
from pathlib import Path
from typing import Dict, List, Optional

from fastapi import FastAPI, HTTPException, Query
from fastapi.responses import FileResponse
from meilisearch import Client

from search import DEFAULT_INDEX_NAME, search as ms_search

BASE_DIR = Path(__file__).resolve().parents[1]
METADATA_FILE = BASE_DIR / "data" / "index.json"
NOTES_FILE = BASE_DIR / "data" / "notes.json"

app = FastAPI(title="GATE Research API")


# ---------------------------------------------------------------------------
# Metadata loading
# ---------------------------------------------------------------------------

def _load_metadata(path: Path) -> Dict[str, dict]:
    """Load metadata from JSON file keyed by document id.

    The JSON may either be a list of documents or wrapped in a top-level
    "documents" key. If the file cannot be parsed, an empty dict is returned
    so the application can still start up.
    """
    try:
        with path.open("r", encoding="utf-8") as f:
            data = json.load(f)
        if isinstance(data, dict) and "documents" in data:
            documents = data["documents"]
        else:
            documents = data
        return {doc["id"]: doc for doc in documents}
    except Exception:
        # Failed to parse metadata; return empty mapping
        return {}


METADATA: Dict[str, dict] = _load_metadata(METADATA_FILE)


def _load_notes(path: Path) -> Dict[str, dict]:
    try:
        with path.open("r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return {}


NOTES: Dict[str, dict] = _load_notes(NOTES_FILE)


def _save_notes() -> None:
    with NOTES_FILE.open("w", encoding="utf-8") as f:
        json.dump(NOTES, f, ensure_ascii=False, indent=2)


def _collect_unique(field: str) -> List[str]:
    values = set()
    for doc in METADATA.values():
        for item in doc.get(field, []) or []:
            values.add(item)
    return sorted(values)


ENTITIES: List[str] = _collect_unique("entities")
TOPICS: List[str] = _collect_unique("topics")


# ---------------------------------------------------------------------------
# API endpoints
# ---------------------------------------------------------------------------


@app.get("/search")
def search_endpoint(
    q: str,
    types: Optional[List[str]] = Query(None, alias="type"),
    sources: Optional[List[str]] = Query(None, alias="source"),
    topics: Optional[List[str]] = Query(None, alias="topic"),
    entities: Optional[List[str]] = Query(None, alias="entity"),
    limit: int = 20,
    index_name: str = DEFAULT_INDEX_NAME,
) -> dict:
    """Search the Meilisearch index with optional filters."""
    return ms_search(
        q,
        types=types,
        sources=sources,
        topics=topics,
        entities=entities,
        limit=limit,
        index_name=index_name,
    )


@app.get("/document/{doc_id}")
def get_document(doc_id: str) -> dict:
    """Retrieve a document by ID from the metadata."""
    if doc_id in METADATA:
        return METADATA[doc_id]

    # Fallback to Meilisearch if not present in metadata
    host = os.getenv("MEILISEARCH_HOST", "http://127.0.0.1:7700")
    api_key = os.getenv("MEILISEARCH_API_KEY", "masterKey")
    client = Client(host, api_key)
    index = client.index(DEFAULT_INDEX_NAME)
    try:
        return index.get_document(doc_id)
    except Exception:
        raise HTTPException(status_code=404, detail="Document not found")


@app.get("/entities")
def list_entities() -> List[str]:
    """Return all known entities from the metadata."""
    return ENTITIES


@app.get("/topics")
def list_topics() -> List[str]:
    """Return all known topics from the metadata."""
    return TOPICS


@app.get("/notes/{doc_id}")
def get_note(doc_id: str) -> dict:
    """Return stored note and tags for a document."""
    return NOTES.get(doc_id, {"text": "", "tags": []})


@app.post("/notes/{doc_id}")
def save_note(doc_id: str, payload: Dict[str, object]) -> dict:
    """Store note and tags for a document."""
    NOTES[doc_id] = {
        "text": payload.get("text", ""),
        "tags": payload.get("tags", []),
    }
    _save_notes()
    return {"status": "ok"}


@app.get("/export")
def export_notes(format: str = "csv"):
    """Export stored notes in CSV or PDF format."""
    if format == "csv":
        with tempfile.NamedTemporaryFile("w", delete=False, suffix=".csv") as tmp:
            writer = csv.writer(tmp)
            writer.writerow(["doc_id", "text", "tags"])
            for doc_id, note in NOTES.items():
                writer.writerow(
                    [doc_id, note.get("text", ""), ";".join(note.get("tags", []))]
                )
            tmp_path = Path(tmp.name)
        return FileResponse(tmp_path, filename="notes.csv", media_type="text/csv")
    elif format == "pdf":
        try:
            from fpdf import FPDF
        except Exception:
            raise HTTPException(status_code=500, detail="PDF export not available")

        pdf = FPDF()
        pdf.set_auto_page_break(auto=True, margin=15)
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        for doc_id, note in NOTES.items():
            pdf.multi_cell(0, 10, f"Document: {doc_id}")
            pdf.multi_cell(0, 10, f"Tags: {', '.join(note.get('tags', []))}")
            pdf.multi_cell(0, 10, note.get("text", ""))
            pdf.ln()
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
            pdf.output(tmp.name)
            tmp_path = Path(tmp.name)
        return FileResponse(
            tmp_path, filename="notes.pdf", media_type="application/pdf"
        )
    else:
        raise HTTPException(status_code=400, detail="Unsupported format")

