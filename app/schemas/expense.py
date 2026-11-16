from datetime import date
from decimal import Decimal
from typing import Optional, Literal

from pydantic import BaseModel, Field, ConfigDict


class ExpenseCreate(BaseModel):

    title: str = Field(..., min_length=1)

    amount: Decimal = Field(..., gt=0)

    category: str = Field(..., min_length=1)

    description: Optional[str] = None

    payment_method: Literal[
        "Cash",
        "UPI",
        "Card",
        "Net Banking",
        "Bank Transfer"
    ]

    expense_date: date


class ExpenseResponse(BaseModel):

    model_config = ConfigDict(from_attributes=True)

    id: int
    title: str
    amount: Decimal
    category: str
    description: Optional[str]
    payment_method: str
    expense_date: date
    created_at: date | None = None