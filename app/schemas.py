# app/schemas.py
from pydantic import BaseModel, Field


# Input schema defining the strict structure for the incoming pediction requests
class TransactionInput(BaseModel):
    amount: float = Field(
        ..., gt=0, description="Transaction amount in USD", examples=[150.50]
    )
    old_balance: float = Field(
        ..., ge=0, description="Initial balance before transaction", examples=[1000.00]
    )
    new_balance: float = Field(
        ..., ge=0, description="New balance after transaction", examples=[849.50]
    )
    location_score: float = Field(
        ...,
        ge=0.0,
        le=1.0,
        description="Risk score of location (0 to 1)",
        examples=[0.12],
    )


# Output schema defining the response contract sent back to the client
class PredictionOutput(BaseModel):
    is_fraud: bool
    fraud_probability: float
    status: str
