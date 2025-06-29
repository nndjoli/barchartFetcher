from barchartFetcher.utils import QueryManager, SyncQueryFunctions


class Quotes:
    def __init__(self):
        self.__query_manager__ = QueryManager()

    def analyst_rating(self, symbols: str = "AAPL", raw: int = 1):
        """Query function for analyst_rating using QueryManager"""
        return SyncQueryFunctions.quotes.analyst_rating(
            self.__query_manager__, symbols, raw
        )

    def fundamentals(self, symbols: str = "AAPL", raw: int = 1):
        """Query function for fundamentals using QueryManager"""
        return SyncQueryFunctions.quotes.fundamentals(
            self.__query_manager__, symbols, raw
        )

    def options_overview(self, symbols: str = "AAPL", raw: int = 1):
        """Query function for options_overview using QueryManager"""
        return SyncQueryFunctions.quotes.options_overview(
            self.__query_manager__, symbols, raw
        )

    def price_performance(self, symbols: str = "AAPL", raw: int = 1):
        """Query function for price_performance using QueryManager"""
        return SyncQueryFunctions.quotes.price_performance(
            self.__query_manager__, symbols, raw
        )

    def quote(self, symbols: str = "AAPL", raw: int = 1):
        """Query function for quote using QueryManager"""
        return SyncQueryFunctions.quotes.quote(
            self.__query_manager__, symbols, raw
        )

    def technical_opinion(self, symbols: str = "AAPL", raw: int = 1):
        """Query function for technical_opinion using QueryManager"""
        return SyncQueryFunctions.quotes.technical_opinion(
            self.__query_manager__, symbols, raw
        )

    def lows_highs(self, symbols: str = "AAPL", raw: int = 1):
        """Query function for lows_highs using QueryManager"""
        return SyncQueryFunctions.quotes.lows_highs(
            self.__query_manager__, symbols, raw
        )

    def performance_past_5d(self, symbols: str = "AAPL", raw: int = 1):
        """Query function for past_5d using QueryManager"""
        return SyncQueryFunctions.quotes.past_5d(
            self.__query_manager__, symbols, raw
        )

    def performance_past_5m(self, symbols: str = "AAPL", raw: int = 1):
        """Query function for past_5m using QueryManager"""
        return SyncQueryFunctions.quotes.past_5m(
            self.__query_manager__, symbols, raw
        )

    def performance_past_5w(self, symbols: str = "AAPL", raw: int = 1):
        """Query function for past_5w using QueryManager"""
        return SyncQueryFunctions.quotes.past_5w(
            self.__query_manager__, symbols, raw
        )

    def price_per(self, symbols: str = "AAPL", raw: int = 1):
        """Query function for price_perf using QueryManager"""
        return SyncQueryFunctions.quotes.price_perf(
            self.__query_manager__, symbols, raw
        )
