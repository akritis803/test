
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.expense import ExpenseCreate, ExpenseResponse
from app.services.expense import create_expense


router = APIRouter(
    prefix="/api/expenses",
    tags=["Expenses"]
)


@router.post(
    "",
    response_model=ExpenseResponse,
    status_code=status.HTTP_201_CREATED
)
def add_expense(
    payload: ExpenseCreate,
    db: Session = Depends(get_db)
):
    return create_expense(db, payload)
