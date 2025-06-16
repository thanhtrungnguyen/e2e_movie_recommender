from fastapi.testclient import TestClient
from main import app

def test_interact():
    client = TestClient(app)
    response = client.post("/interact", json={"user_id": 1, "movie_id": 2, "event": "click"})
    assert response.status_code == 200
    assert response.json()["status"] == "event published"
