from fastapi import FastAPI

app = FastAPI()


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/predict")
def predict(amount: float, hour: int):
    score = 0

    if amount > 300:
        score += 0.35

    if hour >= 22 or hour <= 5:
        score += 0.25

    if score >= 0.7:
        risk_level = "high"
    elif score >= 0.4:
        risk_level = "medium"
    else:
        risk_level = "low"

    return {
        "amount": amount,
        "hour": hour,
        "fraud_score": score,
        "risk_level": risk_level
    }