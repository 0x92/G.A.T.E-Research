#!/usr/bin/env python3
"""Import RSS feed entries into ``data/rss``.

Reads feed URLs from ``config/rss.json`` and writes harmonised metadata
records using the same schema as ``ingest_resources.py``. By default the
script performs a single import run. Use the ``--loop`` flag to keep the
process running and fetch feeds once per day.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import time
from datetime import datetime, timezone
from typing import List

import feedparser

TAG_KEYWORDS: List[str] = ["GATE", "MKULTRA"]


def get_tags(text: str) -> List[str]:
    """Return tags based on keywords present in *text*."""
    upper = text.upper()
    return [tag for tag in TAG_KEYWORDS if tag in upper]


def load_urls() -> List[str]:
    """Load RSS feed URLs from ``config/rss.json``."""
    with open("config/rss.json", "r", encoding="utf-8") as fh:
        return json.load(fh)


def fetch_feeds(urls: List[str]) -> List[dict]:
    """Fetch feeds and return a list of metadata records."""
    records: List[dict] = []
    for url in urls:
        feed = feedparser.parse(url)
        for entry in feed.entries:
            link = entry.get("link", "")
            title = entry.get("title", link)
            date = datetime.now(timezone.utc)
            if getattr(entry, "published_parsed", None):
                date = datetime(*entry.published_parsed[:6], tzinfo=timezone.utc)
            metadata = {
                "id": hashlib.sha256(link.encode()).hexdigest(),
                "title": title,
                "date": date.isoformat(),
                "source": url,
                "type": "rss",
                "filePath": link,
                "tags": get_tags(f"{title} {link}"),
                "entities": [],
                "topics": [],
            }
            records.append(metadata)
    return records


def save_records(records: List[dict]) -> None:
    """Save *records* to ``data/rss/YYYY-MM-DD.json``."""
    if not records:
        return
    os.makedirs("data/rss", exist_ok=True)
    fname = datetime.now(timezone.utc).strftime("%Y-%m-%d.json")
    path = os.path.join("data/rss", fname)
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(records, fh, indent=2, ensure_ascii=False)


def run_once() -> None:
    urls = load_urls()
    records = fetch_feeds(urls)
    save_records(records)


def main() -> None:
    parser = argparse.ArgumentParser(description="Import RSS feeds into data/rss")
    parser.add_argument(
        "--loop",
        action="store_true",
        help="Run continuously and import feeds once per day",
    )
    args = parser.parse_args()
    run_once()
    if args.loop:
        while True:
            time.sleep(24 * 60 * 60)
            run_once()


if __name__ == "__main__":
    main()
