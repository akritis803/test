from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database import get_db

from app.schemas.job_application import (
    JobApplicationCreate,
    JobApplicationResponse
)

from app.services.job_application import (
    find_duplicate_application,
    create_job_application
)


router = APIRouter(
    prefix="/api/job-applications",
    tags=["Job Applications"]
)


@router.post(
    "",
    response_model=JobApplicationResponse,
    status_code=status.HTTP_201_CREATED
)
def add_job_application(
    payload: JobApplicationCreate,
    db: Session = Depends(get_db)
):

    duplicate = find_duplicate_application(db, payload)

    if duplicate:
        raise HTTPException(
            status_code=409,
            detail="Duplicate job application"
        )

    return create_job_application(db, payload)