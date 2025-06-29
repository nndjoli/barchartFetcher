from barchartFetcher.utils import QueryManager, SyncQueryFunctions


class Financials:
    def __init__(self):
        self.__query_manager__ = QueryManager()

    def financial_summary_quarterly(self, symbols: str = "AAPL", raw: int = 1):
        """Query function for financial_summary_q using QueryManager"""
        return SyncQueryFunctions.financials.financial_summary_q(
            self.__query_manager__, symbols, raw
        )

    def financial_summary_yearly(self, symbols: str = "AAPL", raw: int = 1):
        """Query function for financial_summary_y using QueryManager"""
        return SyncQueryFunctions.financials.financial_summary_y(
            self.__query_manager__, symbols, raw
        )
