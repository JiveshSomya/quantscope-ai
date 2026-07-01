from abc import ABC, abstractmethod


class MarketDataProvider(ABC):

    @abstractmethod
    def get_price(self, symbol: str):
        pass