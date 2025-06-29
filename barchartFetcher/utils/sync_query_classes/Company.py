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
        """Query function for sector_competitors using QueryManager"""
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
        """Query function for company_informations using QueryManager"""
        return SyncQueryFunctions.company.company_informations(
            self.__query_manager__, symbols, raw
        )

    def growth(self, symbols: str = "AAPL", raw: int = 1):
        """Query function for growth using QueryManager"""
        return SyncQueryFunctions.company.growth(
            self.__query_manager__, symbols, raw
        )

    def quote_overview(self, symbols: str = "AAPL", raw: int = 1):
        """Query function for overview using QueryManager"""
        return SyncQueryFunctions.company.overview(
            self.__query_manager__, symbols, raw
        )

    def per_share_information(self, symbols: str = "AAPL", raw: int = 1):
        """Query function for per_share_information using QueryManager"""
        return SyncQueryFunctions.company.per_share_information(
            self.__query_manager__, symbols, raw
        )

    def ratios(self, symbols: str = "AAPL", raw: int = 1):
        """Query function for ratios using QueryManager"""
        return SyncQueryFunctions.company.ratios(
            self.__query_manager__, symbols, raw
        )

    def sec_filings(
        self,
        symbol: str = "AAPL",
        transactions: int | float = 1,
        limit: int = 20,
    ):
        """Query function for sec_filings using QueryManager"""
        return SyncQueryFunctions.company.sec_filings(
            self.__query_manager__, symbol, transactions, limit
        )
