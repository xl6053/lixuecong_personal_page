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


def test_low_risk_transaction():
    transaction = Transaction(
        merchant_id="M456",
        amount=100,
        country="PT",
        hour=14,
        user_age_days=100
    )

    result = predict_fraud(transaction)

    assert result["fraud_score"] == 0
    assert result["risk_level"] == "low"
    assert result["reasons"] == []


def test_uncommon_country_transaction():
    transaction = Transaction(
        merchant_id="M999",
        amount=100,
        country="US",
        hour=14,
        user_age_days=100
    )

    result = predict_fraud(transaction)

    assert result["fraud_score"] == 0.15
    assert result["risk_level"] == "low"
    assert "Transaction country is not in the allowed list" in result["reasons"]