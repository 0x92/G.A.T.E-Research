import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.append(str(ROOT))
sys.path.append(str(ROOT / 'backend'))

from fastapi.testclient import TestClient

import backend.app as app_module

# Patch global state to avoid file I/O during tests
app_module.NOTES = {}
app_module._save_notes = lambda: None
app_module._log_audit = lambda *a, **k: None

client = TestClient(app_module.app)


def get_token(username="alice", password="secret"):
    response = client.post("/token", data={"username": username, "password": password})
    assert response.status_code == 200
    return response.json()["access_token"]


def test_notes_crud():
    token = get_token()
    headers = {"Authorization": f"Bearer {token}"}

    # Initially no note
    r = client.get("/notes/doc1", headers=headers)
    assert r.status_code == 200
    assert r.json() == {"text": "", "tags": []}

    # Save note
    payload = {"text": "Hello", "tags": ["tag1"]}
    r = client.post("/notes/doc1", headers=headers, json=payload)
    assert r.status_code == 200
    assert app_module.NOTES["doc1"] == payload

    # Retrieve note
    r = client.get("/notes/doc1", headers=headers)
    assert r.json() == payload


def test_notes_auth_required():
    r = client.get("/notes/doc1")
    assert r.status_code == 401


def test_search_endpoint(monkeypatch):
    called = {}

    def fake_search(q, **kwargs):
        called["q"] = q
        called.update(kwargs)
        return {"hits": []}

    monkeypatch.setattr(app_module, "ms_search", fake_search)

    r = client.get("/search", params={"q": "test", "type": ["a"], "limit": 5})
    assert r.status_code == 200
    assert r.json() == {"hits": []}
    assert called["q"] == "test"
    assert called["types"] == ["a"]
    assert called["limit"] == 5
