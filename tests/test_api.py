# test/test_api.py

from fastapi.testclient import TestClient
from app.main import app

# Create a simulated test client instance attached to our FastAPI app
client = TestClient(app)

def test_health_endpoint():
    """
    Test 1: Verify /health returns status code 200 and the correct JSON body.
    """
    response = client.get("/health")
    
    # Assert HTTP status is 200 OK
    assert response.status_code == 200
    
    # Assert JSON payload contents
    data = response.json()
    assert data["status"] == "healthy"
    assert data["service"] == "fraud-detection-api"

def test_predict_endpoint_valid():
    """
    Test 2: Verify /predict accepts valid data and returns a fraud prediction.
    """
    payload = {
        "amount": 150.50,
        "old_balance": 1000.00,
        "new_balance": 849.50,
        "location_score": 0.12
    }
    
    response = client.post("/predict", json=payload)
    
    assert response.status_code == 200
    
    data = response.json()
    assert "is_fraud" in data
    assert "fraud_probability" in data
    assert data["status"] == "success"
    assert isinstance(data["is_fraud"], bool)

def test_predict_endpoint_invalid():
    """
    Test 3: Verify /predict rejects invalid payload (negative amount) with 422.
    """
    payload = {
        "amount": -50.00,  # Invalid: fails Pydantic gt=0 rule
        "old_balance": 1000.00,
        "new_balance": 1050.00,
        "location_score": 0.12
    }
    
    response = client.post("/predict", json=payload)
    
    # Assert HTTP status is 422 Unprocessable Entity
    assert response.status_code == 422
