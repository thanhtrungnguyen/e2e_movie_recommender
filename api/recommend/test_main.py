from fastapi.testclient import TestClient
from main import app

def test_recommend():
    client = TestClient(app)
    response = client.get("/recommend/1")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
