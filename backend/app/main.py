from fastapi import FastAPI
import app.models.portfolio
from app.portfolio.router import router as portfolio_router

from app.auth.router import router as auth_router
from app.database.database import Base, engine

import app.models.user

Base.metadata.create_all(bind=engine)

app = FastAPI(title="QuantScope AI")

app.include_router(auth_router)
app.include_router(portfolio_router)

@app.get("/")
def root():
    return {"message": "QuantScope AI 🚀"}