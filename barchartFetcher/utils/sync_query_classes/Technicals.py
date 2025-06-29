from barchartFetcher.utils import QueryManager, SyncQueryFunctions


class Technicals:
    def __init__(self):
        self.__query_manager__ = QueryManager()

    def moving_averages(self, symbols: str = "AAPL", raw: int = 1):
        """Moving average values for `symbols` from Barchart.

        Parameters
        ----------
        symbols : str, default "AAPL"
            Comma separated ticker symbols.
        raw : int, default 1
            `1` to request raw values from the API.
        """
        return SyncQueryFunctions.technicals.moving_averages(
            self.__query_manager__, symbols, raw
        )

    def stochastics(self, symbols: str = "AAPL", raw: int = 1):
        """Stochastic oscillator values for `symbols` from Barchart.

        Parameters
        ----------
        symbols : str, default "AAPL"
            Comma separated ticker symbols.
        raw : int, default 1
            `1` to request raw values from the API.
        """
        return SyncQueryFunctions.technicals.stochastics(
            self.__query_manager__, symbols, raw
        )

    def strength(self, symbols: str = "AAPL", raw: int = 1):
        """Relative strength index for `symbols` from Barchart.

        Parameters
        ----------
        symbols : str, default "AAPL"
            Comma separated ticker symbols.
        raw : int, default 1
            `1` to request raw values from the API.
        """
        return SyncQueryFunctions.technicals.strength(
            self.__query_manager__, symbols, raw
        )

    def composite_indicator(self, symbols: str = "AAPL", raw: int = 1):
        """Composite technical indicator for `symbols`.

        Parameters
        ----------
        symbols : str, default "AAPL"
            Comma separated ticker symbols.
        raw : int, default 1
            `1` to request raw values from the API.
        """
        return SyncQueryFunctions.technicals.composite_indicator(
            self.__query_manager__, symbols, raw
        )

    def long_term_indicators(self, symbols: str = "AAPL", raw: int = 1):
        """Long term technical indicators for `symbols`.

        Parameters
        ----------
        symbols : str, default "AAPL"
            Comma separated ticker symbols.
        raw : int, default 1
            `1` to request raw values from the API.
        """
        return SyncQueryFunctions.technicals.long_term_indicators(
            self.__query_manager__, symbols, raw
        )

    def medium_term_indicators(self, symbols: str = "AAPL", raw: int = 1):
        """Medium term technical indicators for `symbols`.

        Parameters
        ----------
        symbols : str, default "AAPL"
            Comma separated ticker symbols.
        raw : int, default 1
            `1` to request raw values from the API.
        """
        return SyncQueryFunctions.technicals.medium_term_indicators(
            self.__query_manager__, symbols, raw
        )

    def barchart_opinion(self, symbols: str = "AAPL", raw: int = 1):
        """Barchart's overall technical opinion on `symbols`.

        Parameters
        ----------
        symbols : str, default "AAPL"
            Comma separated ticker symbols.
        raw : int, default 1
            `1` to request raw values from the API.
        """
        return SyncQueryFunctions.technicals.opinion(
            self.__query_manager__, symbols, raw
        )

    def short_term_indicators(self, symbols: str = "AAPL", raw: int = 1):
        """Short term technical indicators for `symbols`.

        Parameters
        ----------
        symbols : str, default "AAPL"
            Comma separated ticker symbols.
        raw : int, default 1
            `1` to request raw values from the API.
        """
        return SyncQueryFunctions.technicals.short_term_indicators(
            self.__query_manager__, symbols, raw
        )
