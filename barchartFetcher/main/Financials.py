from barchartFetcher.utils import QueryManager, SyncQueryFunctions


class Financials:
    def __init__(self):
        self.__query_manager__ = QueryManager()

    def financial_summary_quarterly(self, symbols: str = "AAPL", raw: int = 1):
        """Quarterly financial summary for `symbols` from Barchart.

        Parameters
        ----------
        symbols : str, default "AAPL"
            Comma separated ticker symbols.
        raw : int, default 1
            `1` to request raw values from the API.
        """
        return SyncQueryFunctions.financials.financial_summary_q(
            self.__query_manager__, symbols, raw
        )

    def financial_summary_yearly(self, symbols: str = "AAPL", raw: int = 1):
        """Yearly financial summary for `symbols` from Barchart.

        Parameters
        ----------
        symbols : str, default "AAPL"
            Comma separated ticker symbols.
        raw : int, default 1
            `1` to request raw values from the API.
        """
        return SyncQueryFunctions.financials.financial_summary_y(
            self.__query_manager__, symbols, raw
        )

    def income_statement(
        self, symbol: str = "AAPL", frequency: str = "annual", page: int = 1
    ):
        """Income statement for `symbol` from Barchart.

        Parameters
        ----------
        symbol : str, default "AAPL"
            Ticker symbol.
        frequency : str, default "annual"
            Frequency of the income statement, either "annual" or "quarterly".
        page : int, default 1
            Page number for paginated results.
        """
        return SyncQueryFunctions.financials.process_income_statement_response(
            SyncQueryFunctions.financials.income_statement(
                self.__query_manager__, symbol, frequency, page
            )
        )

    def balance_sheet(
        self, symbol: str = "AAPL", frequency: str = "annual", page: int = 1
    ):
        """Balance sheet for `symbol` from Barchart.

        Parameters
        ----------
        symbol : str, default "AAPL"
            Ticker symbol.
        frequency : str, default "annual"
            Frequency of the balance sheet, either "annual" or "quarterly".
        page : int, default 1
            Page number for paginated results.
        """
        return SyncQueryFunctions.financials.process_balance_sheet_responser(
            SyncQueryFunctions.financials.balance_sheet(
                self.__query_manager__, symbol, frequency, page
            )
        )

    def cash_flow(
        self, symbol: str = "AAPL", frequency: str = "annual", page: int = 1
    ):
        """Cash flow statement for `symbol` from Barchart.

        Parameters
        ----------
        symbol : str, default "AAPL"
            Ticker symbol.
        frequency : str, default "annual"
            Frequency of the cash flow statement, either "annual" or "quarterly".
        page : int, default 1
            Page number for paginated results.
        """
        return SyncQueryFunctions.financials.process_cash_flow_response(
            SyncQueryFunctions.financials.cash_flow(
                self.__query_manager__, symbol, frequency, page
            )
        )
