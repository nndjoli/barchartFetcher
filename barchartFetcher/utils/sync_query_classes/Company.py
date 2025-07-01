from barchartFetcher.utils import QueryManager, SyncQueryFunctions


class Company:
    def __init__(self):
        self.__query_manager__ = QueryManager()

    def sector_competitors(
        self,
        symbol: str = "AAPL",
        sector_symbol: str = "-COMC",
        orderBy: str = "weightedAlpha",
        orderDir: str = "desc",
        hasOptions: str = "true",
        page: int = 1,
        limit: int = 100,
        raw: int = 1,
    ):
        """List competitors within `sector_symbol` for `symbol`.

        Parameters
        ----------
        symbol : str, default "AAPL"
            Base ticker symbol.
        sector_symbol : str, default "-COMC"
            Identifier for the sector in Barchart's API.
        orderBy : str, default "weightedAlpha"
            Field used for sorting results.
        orderDir : str, default "desc"
            Sorting direction, `"asc"` or `"desc"`.
        hasOptions : str, default "true"
            Filter companies that have listed options.
        page : int, default 1
            Page number for paginated results.
        limit : int, default 100
            Maximum number of rows to return.
        raw : int, default 1
            `1` to request raw values from the API.
        """
        return SyncQueryFunctions.company.sector_competitors(
            self.__query_manager__,
            symbol,
            sector_symbol,
            orderBy,
            orderDir,
            hasOptions,
            page,
            limit,
            raw,
        )

    def company_informations(self, symbols: str = "AAPL", raw: int = 1):
        """Return company statistics for `symbols` from Barchart.

        Parameters
        ----------
        symbols : str, default "AAPL"
            Comma separated ticker symbols.
        raw : int, default 1
            `1` to request raw values from the API.
        """
        return SyncQueryFunctions.company.company_informations(
            self.__query_manager__, symbols, raw
        )

    def growth(self, symbols: str = "AAPL", raw: int = 1):
        """Retrieve growth metrics for `symbols` from Barchart.

        Parameters
        ----------
        symbols : str, default "AAPL"
            Comma separated ticker symbols.
        raw : int, default 1
            `1` to request raw values from the API.
        """
        return SyncQueryFunctions.company.growth(
            self.__query_manager__, symbols, raw
        )

    def quote_overview(self, symbols: str = "AAPL", raw: int = 1):
        """Get an overview quote for `symbols` from Barchart.

        Parameters
        ----------
        symbols : str, default "AAPL"
            Comma separated ticker symbols.
        raw : int, default 1
            `1` to request raw values from the API.
        """
        return SyncQueryFunctions.company.overview(
            self.__query_manager__, symbols, raw
        )

    def per_share_information(self, symbols: str = "AAPL", raw: int = 1):
        """Return per share data for `symbols` from Barchart.

        Parameters
        ----------
        symbols : str, default "AAPL"
            Comma separated ticker symbols.
        raw : int, default 1
            `1` to request raw values from the API.
        """
        return SyncQueryFunctions.company.per_share_information(
            self.__query_manager__, symbols, raw
        )

    def ratios(self, symbols: str = "AAPL", raw: int = 1):
        """Fetch financial ratios for `symbols` from Barchart.

        Parameters
        ----------
        symbols : str, default "AAPL"
            Comma separated ticker symbols.
        raw : int, default 1
            `1` to request raw values from the API.
        """
        return SyncQueryFunctions.company.ratios(
            self.__query_manager__, symbols, raw
        )

    def sec_filings(
        self,
        symbol: str = "AAPL",
        transactions: int | float = 1,
        limit: int = 20,
    ):
        """Retrieve SEC filings for `symbol` from Barchart.

        Parameters
        ----------
        symbol : str, default "AAPL"
            Ticker symbol.
        transactions : int or float, default 1
            Number of transactions to request.
        limit : int, default 20
            Maximum number of rows to return.
        """
        return SyncQueryFunctions.company.sec_filings(
            self.__query_manager__, symbol, transactions, limit
        )

    def insider_trades(
        self,
        symbol: str = "AAPL",
        transactions: int | float = 1,
        limit: int = 20,
    ):
        """Retrieve insider trades for `symbol` from Barchart.

        Parameters
        ----------
        symbol : str, default "AAPL"
            Ticker symbol.
        transactions : int or float, default 1
            Number of transactions to request.
        limit : int, default 20
            Maximum number of rows to return.
        """
        return SyncQueryFunctions.company.insider_trades(
            self.__query_manager__, symbol, transactions, limit
        )
