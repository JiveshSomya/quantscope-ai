import yfinance as yf

from app.market.providers.base import MarketDataProvider


class YahooFinanceProvider(MarketDataProvider):

    def get_price(self, symbol: str):

        stock = yf.Ticker(symbol)

        price = stock.fast_info.get("lastPrice")

        return {
            "symbol": symbol.upper(),
            "price": price,
        }