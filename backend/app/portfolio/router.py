from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.auth.dependencies import get_current_user
from app.database.database import get_db
from app.models.user import User
from app.portfolio.schemas import PortfolioCreate
from app.portfolio.service import add_stock

router = APIRouter(
    prefix="/portfolio",
    tags=["Portfolio"],
)


@router.post("/")
def create_portfolio(
    request: PortfolioCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    stock = add_stock(
        db=db,
        user_id=current_user.id,
        ticker=request.ticker,
        quantity=request.quantity,
        buy_price=request.buy_price,
    )

    return stock