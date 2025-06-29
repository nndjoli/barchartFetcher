from barchartFetcher.utils import QueryManager, SyncQueryFunctions


class Financials:
    def __init__(self):
        self.__query_manager__ = QueryManager()

    def financial_summary_quarterly(self, symbols: str = "AAPL", raw: int = 1):
        """Quarterly financial summary for ``symbols`` from barchart.com.

        Parameters
        ----------
        symbols : str, default "AAPL"
            Comma separated ticker symbols.
        raw : int, default 1
            ``1`` to request raw values from the API.
        """
        return SyncQueryFunctions.financials.financial_summary_q(
            self.__query_manager__, symbols, raw
        )

    def financial_summary_yearly(self, symbols: str = "AAPL", raw: int = 1):
        """Yearly financial summary for ``symbols`` from barchart.com.

        Parameters
        ----------
        symbols : str, default "AAPL"
            Comma separated ticker symbols.
        raw : int, default 1
            ``1`` to request raw values from the API.
        """
        return SyncQueryFunctions.financials.financial_summary_y(
            self.__query_manager__, symbols, raw
        )
