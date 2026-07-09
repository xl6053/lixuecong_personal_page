from app.schemas import Transaction


def predict_fraud(transaction: Transaction):
    score = 0

    if transaction.amount > 300:
        score += 0.35

    if transaction.hour >= 22 or transaction.hour <= 5:
        score += 0.25

    if transaction.user_age_days < 30:
        score += 0.25

    if transaction.country not in {"PT", "ES", "FR", "DE"}:
        score += 0.15

    if score >= 0.7:
        risk_level = "high"
    elif score >= 0.4:
        risk_level = "medium"
    else:
        risk_level = "low"

    return {
        "merchant_id": transaction.merchant_id,
        "amount": transaction.amount,
        "country": transaction.country,
        "hour": transaction.hour,
        "user_age_days": transaction.user_age_days,
        "fraud_score": score,
        "risk_level": risk_level
    }