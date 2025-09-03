from __future__ import annotations

import json
import os
from pathlib import Path
from typing import Dict, List, Optional

from fastapi import FastAPI, HTTPException, Query
from meilisearch import Client

from search import DEFAULT_INDEX_NAME, search as ms_search

BASE_DIR = Path(__file__).resolve().parents[1]
METADATA_FILE = BASE_DIR / "data" / "index.json"

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

