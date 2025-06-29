from barchartFetcher.utils import QueryManager, SyncQueryFunctions


class Technicals:
    def __init__(self):
        self.__query_manager__ = QueryManager()

    def moving_averages(self, symbols: str = "AAPL", raw: int = 1):
        """Query function for moving_averages using QueryManager"""
        return SyncQueryFunctions.technicals.moving_averages(
            self.__query_manager__, symbols, raw
        )

    def stochastics(self, symbols: str = "AAPL", raw: int = 1):
        """Query function for stochastics using QueryManager"""
        return SyncQueryFunctions.technicals.stochastics(
            self.__query_manager__, symbols, raw
        )

    def strength(self, symbols: str = "AAPL", raw: int = 1):
        """Query function for strength using QueryManager"""
        return SyncQueryFunctions.technicals.strength(
            self.__query_manager__, symbols, raw
        )

    def composite_indicator(self, symbols: str = "AAPL", raw: int = 1):
        """Query function for composite_indicator using QueryManager"""
        return SyncQueryFunctions.technicals.composite_indicator(
            self.__query_manager__, symbols, raw
        )

    def long_term_indicators(self, symbols: str = "AAPL", raw: int = 1):
        """Query function for long_term_indicators using QueryManager"""
        return SyncQueryFunctions.technicals.long_term_indicators(
            self.__query_manager__, symbols, raw
        )

    def medium_term_indicators(self, symbols: str = "AAPL", raw: int = 1):
        """Query function for medium_term_indicators using QueryManager"""
        return SyncQueryFunctions.technicals.medium_term_indicators(
            self.__query_manager__, symbols, raw
        )

    def barchart_opinion(self, symbols: str = "AAPL", raw: int = 1):
        """Query function for opinion using QueryManager"""
        return SyncQueryFunctions.technicals.opinion(
            self.__query_manager__, symbols, raw
        )

    def short_term_indicators(self, symbols: str = "AAPL", raw: int = 1):
        """Query function for short_term_indicators using QueryManager"""
        return SyncQueryFunctions.technicals.short_term_indicators(
            self.__query_manager__, symbols, raw
        )
