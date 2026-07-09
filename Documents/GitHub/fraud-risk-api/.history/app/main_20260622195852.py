from fastapi import FastAPI
from app.schemas import Transaction
from app.model import predict_fraud
app = FastAPI()


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/predict")
def predict(transaction: Transaction):
    result = predict_fraud(transaction)
    return result