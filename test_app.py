from fastapi.testclient import TestClient

from app import app


client = TestClient(app)


def test_app_fetch():
    response = client.post("/fetch", json={'topic': 'APPLE'})

    assert response.status_code == 200
    assert 'headlines' in response.json().keys()
    assert len(response.json()['headlines']) > 0
