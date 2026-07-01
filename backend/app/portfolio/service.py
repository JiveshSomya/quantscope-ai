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
    
from app.market.providers.provider import provider


def portfolio_summary(
    db: Session,
    user_id: int,
):

    stocks = (
        db.query(Portfolio)
        .filter(Portfolio.user_id == user_id)
        .all()
    )

    summary = []

    total_value = 0
    total_profit = 0

    for stock in stocks:

        market = provider.get_price(stock.ticker)

        current_price = market["price"]

        current_value = current_price * stock.quantity

        invested = stock.buy_price * stock.quantity

        profit = current_value - invested

        total_value += current_value
        total_profit += profit

        summary.append({
            "ticker": stock.ticker,
            "shares": stock.quantity,
            "buy_price": stock.buy_price,
            "current_price": current_price,
            "current_value": round(current_value, 2),
            "profit": round(profit, 2)
        })

    return {
        "portfolio": summary,
        "total_value": round(total_value,2),
        "total_profit": round(total_profit,2)
    }