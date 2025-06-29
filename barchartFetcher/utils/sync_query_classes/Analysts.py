from barchartFetcher.utils import QueryManager, SyncQueryFunctions


class Analysts:
    def __init__(self):
        self.__query_manager__ = QueryManager()

    def earnings_estimates(self, symbols: str = "AAPL", raw: int = 1):
        """Return earnings estimates for `symbols` from Barchart.

        Parameters
        ----------
        symbols : str, default "AAPL"
            Comma separated list of ticker symbols.
        raw : int, default 1
            When set to `1` the request asks for raw values from the API.
        """
        return SyncQueryFunctions.analysts.earnings_estimates(
            self.__query_manager__, symbols, raw
        )

    def analyst_ratings(self, symbol: str = "AAPL", raw: int = 1):
        """Retrieve analyst ratings for `symbol` from Barchart.

        Parameters
        ----------
        symbol : str, default "AAPL"
            Single ticker symbol.
        raw : int, default 1
            `"1"` to request raw values from the API.
        """
        return SyncQueryFunctions.analysts.analyst_ratings(
            self.__query_manager__, symbol, raw
        )
