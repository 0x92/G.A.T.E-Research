import json
import os
from pathlib import Path
from typing import Iterable, List, Optional

from meilisearch import Client


DEFAULT_INDEX_NAME = "documents"


def _build_filter(
    types: Optional[Iterable[str]] = None,
    sources: Optional[Iterable[str]] = None,
    topics: Optional[Iterable[str]] = None,
    entities: Optional[Iterable[str]] = None,
) -> Optional[str]:
    """Construct a Meilisearch filter string from provided filter values."""
    filters: List[str] = []

    def clause(field: str, values: Optional[Iterable[str]]) -> None:
        if not values:
            return
        if isinstance(values, str):
            values = [values]
        parts = [f"{field} = '{v}'" for v in values]
        filters.append("(" + " OR ".join(parts) + ")")

    clause("type", types)
    clause("source", sources)
    clause("topics", topics)
    clause("entities", entities)

    return " AND ".join(filters) if filters else None


def search(
    query: str,
    *,
    types: Optional[Iterable[str]] = None,
    sources: Optional[Iterable[str]] = None,
    topics: Optional[Iterable[str]] = None,
    entities: Optional[Iterable[str]] = None,
    limit: int = 20,
    index_name: str = DEFAULT_INDEX_NAME,
) -> dict:
    """Search the index with optional filters."""
    host = os.getenv("MEILISEARCH_HOST", "http://127.0.0.1:7700")
    api_key = os.getenv("MEILISEARCH_API_KEY", "masterKey")
    client = Client(host, api_key)
    index = client.index(index_name)

    filter_str = _build_filter(types, sources, topics, entities)
    return index.search(query, {"filter": filter_str, "limit": limit})


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Query the Meilisearch index")
    parser.add_argument("query")
    parser.add_argument("--type", dest="types", action="append")
    parser.add_argument("--source", dest="sources", action="append")
    parser.add_argument("--topic", dest="topics", action="append")
    parser.add_argument("--entity", dest="entities", action="append")
    parser.add_argument("--limit", type=int, default=20)
    parser.add_argument("--index-name", default=DEFAULT_INDEX_NAME)
    args = parser.parse_args()

    result = search(
        args.query,
        types=args.types,
        sources=args.sources,
        topics=args.topics,
        entities=args.entities,
        limit=args.limit,
        index_name=args.index_name,
    )
    print(json.dumps(result, indent=2))
