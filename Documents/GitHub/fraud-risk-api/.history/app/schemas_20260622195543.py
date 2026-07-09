from pydantic import BaseModel, Field


class Transaction(BaseModel):
    merchant_id: str = Field(..., min_length=1)
    amount: float = Field(..., ge=0)
    country: str = Field(..., min_length=2, max_length=2)
    hour: int = Field(..., ge=0, le=23)
    user_age_days: int = Field(..., ge=0)