from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_root_returns_service_status():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {
        "service": "reliable-api",
        "status": "running",
    }


def test_health_endpoint_returns_healthy():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}


def test_version_endpoint_returns_app_version():
    response = client.get("/version")

    assert response.status_code == 200
    assert response.json() == {"version": "0.1.0"}
