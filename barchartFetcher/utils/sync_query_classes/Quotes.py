from barchartFetcher.utils import QueryManager, SyncQueryFunctions


class Quotes:
    def __init__(self):
        self.__query_manager__ = QueryManager()

    def analyst_rating(self, symbols: str = "AAPL", raw: int = 1):
        """Retrieve analyst ratings from Barchart.

        Parameters
        ----------
        symbols : str, default "AAPL"
            Comma separated ticker symbols.
        raw : int, default 1
            `1` to request raw values from the API.
        """
        return SyncQueryFunctions.quotes.analyst_rating(
            self.__query_manager__, symbols, raw
        )

    def fundamentals(self, symbols: str = "AAPL", raw: int = 1):
        """Fundamental data for `symbols` from Barchart.

        Parameters
        ----------
        symbols : str, default "AAPL"
            Comma separated ticker symbols.
        raw : int, default 1
            `1` to request raw values from the API.
        """
        return SyncQueryFunctions.quotes.fundamentals(
            self.__query_manager__, symbols, raw
        )

    def options_overview(self, symbols: str = "AAPL", raw: int = 1):
        """Options overview information from Barchart.

        Parameters
        ----------
        symbols : str, default "AAPL"
            Comma separated ticker symbols.
        raw : int, default 1
            `1` to request raw values from the API.
        """
        return SyncQueryFunctions.quotes.options_overview(
            self.__query_manager__, symbols, raw
        )

    def price_performance(self, symbols: str = "AAPL", raw: int = 1):
        """Price performance metrics for `symbols` from Barchart.

        Parameters
        ----------
        symbols : str, default "AAPL"
            Comma separated ticker symbols.
        raw : int, default 1
            `1` to request raw values from the API.
        """
        return SyncQueryFunctions.quotes.price_performance(
            self.__query_manager__, symbols, raw
        )

    def quote(self, symbols: str = "AAPL", raw: int = 1):
        """Latest quote information for `symbols` from Barchart.

        Parameters
        ----------
        symbols : str, default "AAPL"
            Comma separated ticker symbols.
        raw : int, default 1
            `1` to request raw values from the API.
        """
        return SyncQueryFunctions.quotes.quote(
            self.__query_manager__, symbols, raw
        )

    def technical_opinion(self, symbols: str = "AAPL", raw: int = 1):
        """Retrieve Barchart technical opinion for `symbols`.

        Parameters
        ----------
        symbols : str, default "AAPL"
            Comma separated ticker symbols.
        raw : int, default 1
            `1` to request raw values from the API.
        """
        return SyncQueryFunctions.quotes.technical_opinion(
            self.__query_manager__, symbols, raw
        )

    def lows_highs(self, symbols: str = "AAPL", raw: int = 1):
        """52-week lows and highs for `symbols` from Barchart.

        Parameters
        ----------
        symbols : str, default "AAPL"
            Comma separated ticker symbols.
        raw : int, default 1
            `1` to request raw values from the API.
        """
        return SyncQueryFunctions.quotes.lows_highs(
            self.__query_manager__, symbols, raw
        )

    def performance_past_5d(self, symbols: str = "AAPL", raw: int = 1):
        """Performance over the past five days for `symbols`.

        Parameters
        ----------
        symbols : str, default "AAPL"
            Comma separated ticker symbols.
        raw : int, default 1
            `1` to request raw values from the API.
        """
        return SyncQueryFunctions.quotes.past_5d(
            self.__query_manager__, symbols, raw
        )

    def performance_past_5m(self, symbols: str = "AAPL", raw: int = 1):
        """Performance over the past five months for `symbols`.

        Parameters
        ----------
        symbols : str, default "AAPL"
            Comma separated ticker symbols.
        raw : int, default 1
            `1` to request raw values from the API.
        """
        return SyncQueryFunctions.quotes.past_5m(
            self.__query_manager__, symbols, raw
        )

    def performance_past_5w(self, symbols: str = "AAPL", raw: int = 1):
        """Performance over the past five weeks for `symbols`.

        Parameters
        ----------
        symbols : str, default "AAPL"
            Comma separated ticker symbols.
        raw : int, default 1
            `1` to request raw values from the API.
        """
        return SyncQueryFunctions.quotes.past_5w(
            self.__query_manager__, symbols, raw
        )

    def price_per(self, symbols: str = "AAPL", raw: int = 1):
        """Return price performance ratios for `symbols`.

        Parameters
        ----------
        symbols : str, default "AAPL"
            Comma separated ticker symbols.
        raw : int, default 1
            `1` to request raw values from the API.
        """
        return SyncQueryFunctions.quotes.price_perf(
            self.__query_manager__, symbols, raw
        )
