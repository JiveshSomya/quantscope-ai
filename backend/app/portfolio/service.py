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