from barchartFetcher.utils import QueryManager, SyncQueryFunctions


class Analysts:
    def __init__(self):
        self.__query_manager__ = QueryManager()

    def earnings_estimates(self, symbols: str = "AAPL", raw: int = 1):
        """Query function for earnings_estimates using QueryManager"""
        return SyncQueryFunctions.analysts.earnings_estimates(
            self.__query_manager__, symbols, raw
        )

    def analyst_ratings(self, symbol: str = "AAPL", raw: str = "1"):
        """Query function for analyst_ratings using QueryManager"""
        return SyncQueryFunctions.analysts.analyst_ratings(
            self.__query_manager__, symbol, raw
        )
