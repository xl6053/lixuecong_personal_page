import logging

from fastapi import FastAPI
from app.schemas import Transaction
from app.model import predict_fraud
from app.config import MODEL_VERSION, SERVICE_NAME
app = FastAPI()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
@app.get("/health")
def health():
    logger.info("Health check requested")
    return {"status": "ok", "model_version": MODEL_VERSION}


@app.post("/predict")
def predict(transaction: Transaction):
    logger.info(
        f"Prediction requested: "
        f"merchant_id={transaction.merchant_id} "
        f"amount={transaction.amount} "
        f"country={transaction.country} "
        f"hour={transaction.hour} "
        f"user_age_days={transaction.user_age_days}"
    )
    logger.info(f"Using model version: {MODEL_VERSION}")
    result = predict_fraud(transaction)
    result["model_version"] = MODEL_VERSION

    logger.info(
        f"Prediction completed: "
        f"merchant_id={transaction.merchant_id} "
        f"fraud_score={result['fraud_score']} "
        f"risk_level={result['risk_level']}"
    )

   
    return result