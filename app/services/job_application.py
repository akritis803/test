from sqlalchemy.orm import Session
from sqlalchemy import func

from app.models.job_application import JobApplication
from app.schemas.job_application import JobApplicationCreate


def find_duplicate_application(db: Session, data: JobApplicationCreate):

    return db.query(JobApplication).filter(
        func.lower(JobApplication.email) == str(data.email).lower(),
        func.lower(JobApplication.company_name) == data.company_name.lower(),
        func.lower(JobApplication.job_title) == data.job_title.lower()
    ).first()


def create_job_application(db: Session, data: JobApplicationCreate):

    application = JobApplication(
        **data.model_dump(),
        status="pending"
    )

    db.add(application)

    db.commit()

    db.refresh(application)

    return application