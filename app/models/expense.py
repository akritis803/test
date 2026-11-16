from sqlalchemy import Column, Integer, String, Text
from sqlalchemy import Date, DateTime, Numeric, func

from app.database import Base


class Expense(Base):

    __tablename__ = "expenses"

    id = Column(Integer, primary_key=True, index=True)

    title = Column(String(150), nullable=False)

    amount = Column(Numeric(12, 2), nullable=False)

    category = Column(String(100), nullable=False)

    description = Column(Text, nullable=True)

    payment_method = Column(String(30), nullable=False)

    expense_date = Column(Date, nullable=False)

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False
    )