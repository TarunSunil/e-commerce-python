from fastapi.testclient import TestClient
from app.main import app


def test_health_ok(monkeypatch):
    # Disable DB init for test to avoid external dependency
    monkeypatch.setenv("DISABLE_DB", "1")
    client = TestClient(app)
    resp = client.get("/api/health")
    assert resp.status_code == 200
    assert resp.json()["status"] == "ok"
