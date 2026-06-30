from sqlalchemy.orm import Session

from app.models.portfolio import Portfolio


def add_stock(
    db: Session,
    user_id: int,
    ticker: str,
    quantity: float,
    buy_price: float,
):

    stock = Portfolio(
        user_id=user_id,
        ticker=ticker.upper(),
        quantity=quantity,
        buy_price=buy_price,
    )

    db.add(stock)
    db.commit()
    db.refresh(stock)

    return stock


def get_all_stocks(
    db: Session,
    user_id: int,
):

    return (
        db.query(Portfolio)
        .filter(Portfolio.user_id == user_id)
        .all()
    )


def get_stock(
    db: Session,
    user_id: int,
    stock_id: int,
):

    return (
        db.query(Portfolio)
        .filter(
            Portfolio.id == stock_id,
            Portfolio.user_id == user_id,
        )
        .first()
    )


def update_stock(
    db: Session,
    stock: Portfolio,
    quantity: float,
    buy_price: float,
):

    stock.quantity = quantity
    stock.buy_price = buy_price

    db.commit()
    db.refresh(stock)

    return stock


def delete_stock(
    db: Session,
    stock: Portfolio,
):

    db.delete(stock)
    db.commit()