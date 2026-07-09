from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)
def test_health_endpoint():
    response = client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "ok"
    assert data["service"] == "fraud-risk-api"
    assert data["model_version"] == "rule-based-v1"

def test_predict_endpoint_high_risk():
    payload = {
        "merchant_id": "M123",
        "amount": 650,
        "country": "PT",
        "hour": 23,
        "user_age_days": 10
    }

    response = client.post("/predict", json=payload)

    assert response.status_code == 200

    data = response.json()

    assert data["merchant_id"] == "M123"
    assert data["amount"] == 650
    assert data["country"] == "PT"
    assert data["hour"] == 23
    assert data["user_age_days"] == 10
    assert data["fraud_score"] == 0.85
    assert data["risk_level"] == "high"
    assert data["model_version"] == "rule-based-v1"

    assert "High transaction amount" in data["reasons"]
    assert "Unusual transaction time" in data["reasons"]
    assert "User age is less than 30 days" in data["reasons"]   

def test_predict_endpoint_invalid_input():
    payload = {
        "merchant_id": "M123",
        "amount": -10,
        "country": "PT",
        "hour": 30,
        "user_age_days": -1
    }

    response = client.post("/predict", json=payload)

    assert response.status_code == 422