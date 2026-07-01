from fastapi import APIRouter

from app.market.service import get_stock_price

router = APIRouter(
    prefix="/market",
    tags=["Market"],
)


@router.get("/{symbol}")
def market(symbol: str):

    return get_stock_price(symbol)