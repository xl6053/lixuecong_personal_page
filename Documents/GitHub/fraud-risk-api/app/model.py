from app.schemas import Transaction


def predict_fraud(transaction: Transaction):
    score = 0
    reasons = []
    if transaction.amount > 300:
        score += 0.35
        reasons.append("High transaction amount")

    if transaction.hour >= 22 or transaction.hour <= 5:
        score += 0.25
        reasons.append("Unusual transaction time")

    if transaction.user_age_days < 30:
        score += 0.25
        reasons.append("User age is less than 30 days")
                
    if transaction.country not in {"PT", "ES", "FR", "DE"}:
        score += 0.15
        reasons.append("Transaction country is not in the allowed list")
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
        "risk_level": risk_level,
        "reasons": reasons
    }