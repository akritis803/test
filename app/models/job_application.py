from sqlalchemy import Column, Integer, String, DateTime, Numeric
from sqlalchemy import UniqueConstraint, func

from app.database import Base


class JobApplication(Base):

    __tablename__ = "job_applications"

    __table_args__ = (
        UniqueConstraint(
            "email",
            "company_name",
            "job_title",
            name="uq_applicant_company_job"
        ),
    )

    id = Column(Integer, primary_key=True, index=True)

    applicant_name = Column(String(150), nullable=False)

    email = Column(String(255), nullable=False)

    phone = Column(String(10), nullable=False)

    company_name = Column(String(150), nullable=False)

    job_title = Column(String(150), nullable=False)

    experience = Column(Integer, nullable=False)

    expected_salary = Column(Numeric(12, 2), nullable=False)

    resume_url = Column(String(500), nullable=True)

    status = Column(String(30), default="pending", nullable=False)

    applied_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False
    )