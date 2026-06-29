from fastapi import FastAPI

from app.database.database import Base, engine

# Import ALL models here
from app.models.user import User

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="QuantScope AI",
    version="1.0.0",
)


@app.get("/")
def root():
    return {
        "message": "QuantScope AI 🚀"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }