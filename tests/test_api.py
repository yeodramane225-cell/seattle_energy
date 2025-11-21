from fastapi.testclient import TestClient
from api.main import app

client = TestClient(app)

def test_predict_endpoint():
    data = {
        "PropertyGFATotal": 48210,
        "Latitude": 48.85,
        "Longitude": 2.35,
        "YearBuilt": 1990
    }
    response = client.post("/predict", json=data)
    assert response.status_code == 200
    assert "prediction" in response.json()
