from app.market.providers.provider import provider


def get_stock_price(symbol: str):

    return provider.get_price(symbol)