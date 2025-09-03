import json
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

import backend.load_index as load_index_module


def test_load_index(monkeypatch, tmp_path):
    # Create temporary index file
    data = {"documents": [{"id": 1, "title": "Doc"}]}
    index_file = tmp_path / "index.json"
    index_file.write_text(json.dumps(data))

    # Prepare fake client and index to capture interactions
    calls = {}

    class FakeIndex:
        def update_filterable_attributes(self, attrs):
            calls["filterable"] = attrs

        def update_searchable_attributes(self, attrs):
            calls["searchable"] = attrs

        def add_documents(self, docs):
            calls["docs"] = docs

    class FakeClient:
        def __init__(self, host, key):
            self.host = host
            self.key = key

        def get_index(self, name):
            raise Exception("missing index")

        def create_index(self, name, config):
            calls["created_index"] = name
            return FakeIndex()

    monkeypatch.setattr(load_index_module, "Client", FakeClient)

    load_index_module.load_index(index_file=index_file, index_name="test")

    assert calls["created_index"] == "test"
    assert calls["docs"] == data["documents"]
