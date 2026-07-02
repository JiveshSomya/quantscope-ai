from fastapi import FastAPI
import app.models.portfolio

from app.portfolio.router import router as portfolio_router
from app.market.router import router as market_router

from app.auth.router import router as auth_router
from app.database.database import Base, engine
from app.ai.router import router as ai_router
from app.system.router import router as system_router

app.include_router(system_router)

app.include_router(ai_router)

import app.models.user

Base.metadata.create_all(bind=engine)

app = FastAPI(title="QuantScope AI")
from app.advisor.router import router as advisor_router

app.include_router(advisor_router)

app.include_router(auth_router)
app.include_router(portfolio_router)
app.include_router(market_router)

@app.get("/")
def root():
    return {"message": "QuantScope AI "}