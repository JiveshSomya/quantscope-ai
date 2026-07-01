from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.portfolio.service import portfolio_summary

from app.auth.dependencies import get_current_user
from app.database.database import get_db
from app.models.user import User
from app.portfolio.schemas import (
    PortfolioCreate,
    PortfolioUpdate,
)
from app.portfolio.service import (
    add_stock,
    get_all_stocks,
    get_stock,
    update_stock,
    delete_stock,
)

router = APIRouter(
    prefix="/portfolio",
    tags=["Portfolio"],
)


@router.post("/")
def create_stock(
    request: PortfolioCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return add_stock(
        db,
        current_user.id,
        request.ticker,
        request.quantity,
        request.buy_price,
    )


@router.get("/")
def list_portfolio(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return get_all_stocks(
        db,
        current_user.id,
    )


@router.get("/{stock_id}")
def get_one_stock(
    stock_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    stock = get_stock(
        db,
        current_user.id,
        stock_id,
    )

    if stock is None:
        raise HTTPException(
            status_code=404,
            detail="Stock not found",
        )

    return stock


@router.patch("/{stock_id}")
def edit_stock(
    stock_id: int,
    request: PortfolioUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    stock = get_stock(
        db,
        current_user.id,
        stock_id,
    )

    if stock is None:
        raise HTTPException(
            status_code=404,
            detail="Stock not found",
        )

    return update_stock(
        db,
        stock,
        request.quantity,
        request.buy_price,
    )


@router.delete("/{stock_id}")
def remove_stock(
    stock_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    stock = get_stock(
        db,
        current_user.id,
        stock_id,
    )

    if stock is None:
        raise HTTPException(
            status_code=404,
            detail="Stock not found",
        )

    delete_stock(
        db,
        stock,
    )

    return {
        "message": "Deleted Successfully"
    }
    
    
@router.get("/summary")

def summary(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
    ):

    return portfolio_summary(db,current_user.id,)