from pydantic import BaseModel


class PortfolioCreate(BaseModel):
    ticker: str
    quantity: float
    buy_price: float