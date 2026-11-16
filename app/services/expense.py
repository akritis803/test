from sqlalchemy.orm import Session

from app.models.expense import Expense
from app.schemas.expense import ExpenseCreate


def create_expense(db: Session, data: ExpenseCreate):

    expense = Expense(**data.model_dump())

    db.add(expense)

    db.commit()

    db.refresh(expense)

    return expense