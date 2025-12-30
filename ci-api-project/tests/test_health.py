import pytest
from app.main import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_health_status_code(client):
    response = client.get("/health")
    assert response.status_code == 200


def test_health_response_json(client):
    response = client.get("/health")
    assert response.get_json() == {"status": "ok"}
