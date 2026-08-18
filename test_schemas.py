# test_schemas.py
from app.schemas import TransactionInput, PredictionOutput

# 1. Simulate valid raw input data arriving from a user
valid_raw_data = {
    "amount": 150.50,
    "old_balance": 1000.00,
    "new_balance": 849.50,
    "location_score": 0.12
}

# 2. Parse and validate through Pydantic
validated_input = TransactionInput(**valid_raw_data)
print("✅ Validation Successful for Valid Input!")
print(f"Validated Amount: ${validated_input.amount}\n")

# 3. Simulate invalid raw input (negative transaction amount)
invalid_raw_data = {
    "amount": -50.00,  # Fails gt=0 validation
    "old_balance": 1000.00,
    "new_balance": 1050.00,
    "location_score": 0.12
}

print("Attempting to validate invalid payload (negative amount)...")
try:
    TransactionInput(**invalid_raw_data)
except Exception as error:
    print("❌ Pydantic caught the invalid data as expected!")
    print(error)