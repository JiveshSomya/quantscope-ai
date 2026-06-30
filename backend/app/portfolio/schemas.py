from pydantic import BaseModel


class PortfolioCreate(BaseModel):
    ticker: str
    quantity: float
    buy_price: float


class PortfolioUpdate(BaseModel):
    quantity: float
    buy_price: float


class PortfolioResponse(BaseModel):
    id: int
    ticker: str
    quantity: float
    buy_price: float

    class Config:
        from_attributes = True