from app.schemas import Transaction
from app.model import predict_fraud


def test_high_risk_transaction():
    transaction = Transaction(
        merchant_id="M123",
        amount=650,
        country="PT",
        hour=23,
        user_age_days=10
    )

    result = predict_fraud(transaction)

    assert result["fraud_score"] == 0.85
    assert result["risk_level"] == "high"
    assert "High transaction amount" in result["reasons"]
    assert "Unusual transaction time" in result["reasons"]
    assert "User age is less than 30 days" in result["reasons"]