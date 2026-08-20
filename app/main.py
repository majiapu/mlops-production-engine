# app/main.py
from fastapi import FastAPI

from app.schemas import PredictionOutput, TransactionInput

# Initialize the FastAPI application instance

app = FastAPI(
    title="Real-Time Fraud Detection Engine",
    description="Production-grade MLOps microservice for transaction risk scoring",
    version="0.1.0",
)


# Health Check Endpoint (GET)
@app.get("/health")
def health_check():
    """
    Returns the health status of the API service.
    Used by monitoring systems and load balancers to verify the server is live.
    """
    return {"status": "healthy", "service": "fraud-detection-api", "version": "0.1.0"}


# Fraud Prediction Endpoint (POST)
@app.post("/predict", response_model=PredictionOutput)
def predict_fraud(payload: TransactionInput):
    """
    Accepts validated transaction features and returns a fraud risk score.
    """
    # Simple rule-based mock logic for now (replaced with trained ML model in Week 3)
    # High location risk or large unexplained balance drops
    # trigger high fraud probability
    balance_delta = payload.old_balance - payload.new_balance

    if payload.location_score > 0.8 or balance_delta > 5000:
        fraud_prob = 0.92
        is_fraud = True
    else:
        fraud_prob = 0.05
        is_fraud = False

    return PredictionOutput(
        is_fraud=is_fraud, fraud_probability=fraud_prob, status="success"
    )
