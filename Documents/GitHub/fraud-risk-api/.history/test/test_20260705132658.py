from app.schemas import Transaction, PredictionResponse, HealthResponse
from app.model import predict_fraud

def test_high_risk_transaction():
    transaction = Transaction(
        merchant_id="merchant_123",
        amount=600.0,
        country="US",
        hour=23,
        user_age_days=10
    )
    result = predict_fraud(transaction)
    assert result["fraud_score"] == "0.85"
    assert result["risk_level"] == "high"
    assert "High transaction amount" in result["reasons"]
    assert "Transaction made at odd hour" in result["reasons"]