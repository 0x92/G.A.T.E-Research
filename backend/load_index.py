import json
import os
from pathlib import Path
from typing import Any, Dict, List

from meilisearch import Client


BASE_DIR = Path(__file__).resolve().parents[1]
DEFAULT_INDEX_FILE = BASE_DIR / "data/index.json"
DEFAULT_INDEX_NAME = "documents"


def load_index(index_file: Path = DEFAULT_INDEX_FILE, index_name: str = DEFAULT_INDEX_NAME) -> None:
    """Load documents from a JSON file into a Meilisearch index.

    Parameters
    ----------
    index_file:
        Path to the JSON file containing the documents.
    index_name:
        Name of the Meilisearch index.
    """
    host = os.getenv("MEILISEARCH_HOST", "http://127.0.0.1:7700")
    api_key = os.getenv("MEILISEARCH_API_KEY", "masterKey")

    client = Client(host, api_key)

    try:
        index = client.get_index(index_name)
    except Exception:
        index = client.create_index(index_name, {"primaryKey": "id"})

    with open(index_file, "r", encoding="utf-8") as f:
        data = json.load(f)

    # The JSON may either be a list of documents or wrapped in a top-level key
    documents: List[Dict[str, Any]]
    if isinstance(data, dict) and "documents" in data:
        documents = data["documents"]
    else:
        documents = data

    index.update_filterable_attributes(["type", "source", "topics", "entities"])
    index.update_searchable_attributes([
        "title",
        "ocrText",
        "source",
        "topics",
        "entities",
        "tags",
    ])
    index.add_documents(documents)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Load data/index.json into Meilisearch")
    parser.add_argument("--index-file", type=Path, default=DEFAULT_INDEX_FILE)
    parser.add_argument("--index-name", type=str, default=DEFAULT_INDEX_NAME)
    args = parser.parse_args()

    load_index(args.index_file, args.index_name)
