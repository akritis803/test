from fastapi import FastAPI

from app.database import Base, engine

from app.models import expense, job_application

from app.routes.expense import router as expense_router

from app.routes.job_application import (
    router as job_application_router
)


app = FastAPI(
    title="FastAPI Mini Projects",
    version="1.0.0"
)


# Create database tables
Base.metadata.create_all(bind=engine)


# Register routes
app.include_router(expense_router)

app.include_router(job_application_router)


@app.get("/")
def home():

    return {
        "message": "FastAPI is running successfully"
    }