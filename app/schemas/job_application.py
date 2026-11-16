from datetime import datetime
from decimal import Decimal
from typing import Optional

from pydantic import BaseModel, EmailStr, Field, ConfigDict


class JobApplicationCreate(BaseModel):

    applicant_name: str = Field(..., min_length=1)

    email: EmailStr

    phone: str = Field(..., pattern=r"^[0-9]{10}$")

    company_name: str = Field(..., min_length=1)

    job_title: str = Field(..., min_length=1)

    experience: int = Field(..., ge=0)

    expected_salary: Decimal = Field(..., gt=0)

    resume_url: Optional[str] = None


class JobApplicationResponse(BaseModel):

    model_config = ConfigDict(from_attributes=True)

    id: int
    applicant_name: str
    email: str
    phone: str
    company_name: str
    job_title: str
    experience: int
    expected_salary: Decimal
    resume_url: Optional[str]
    status: str
    applied_at: datetime