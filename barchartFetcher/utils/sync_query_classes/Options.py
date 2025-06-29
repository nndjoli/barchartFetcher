from barchartFetcher.utils import QueryManager, SyncQueryFunctions


class Options:
    def __init__(self):
        self.__query_manager__ = QueryManager()

    def historical_earnings(
        self,
        symbol: str = "AAPL",
        type: str = "events",
        events: str = "earnings",
    ):
        """Query function for earnings using QueryManager"""
        return SyncQueryFunctions.options.earnings(
            self.__query_manager__, symbol, type, events
        )

    def expected_move(
        self,
        symbol: str = "AAPL",
        orderBy: str = "expirationDate",
        orderDir: str = "asc",
        raw: int = 1,
        page: int = 1,
        limit: int = 100,
    ):
        """Query function for expected_move using QueryManager"""
        return SyncQueryFunctions.options.expected_move(
            self.__query_manager__, symbol, orderBy, orderDir, raw, page, limit
        )

    def options_expirations(self, symbols: str = "AAPL", raw: int = 1):
        """Query function for expirations using QueryManager"""
        return SyncQueryFunctions.options.options_expirations(
            self.__query_manager__, symbols, raw
        )

    def bullish_bearish_sentiment(self, symbol: str = "AAPL", raw: int = 1):
        """Query function for bullish_bearish_sentiment using QueryManager"""
        return SyncQueryFunctions.options.bullish_bearish_sentiment(
            self.__query_manager__, symbol, raw
        )

    def options_flow(
        self,
        symbol: str = "AAPL",
        orderBy: str = "premium",
        orderDir: str = "desc",
        limit: int = 3,
        min_trade_size: int = 10,
        raw: int = 1,
    ):
        """Query function for options_flow using QueryManager"""
        return SyncQueryFunctions.options.options_flow(
            self.__query_manager__,
            symbol,
            orderBy,
            orderDir,
            limit,
            min_trade_size,
            raw,
        )

    def gamma_exposure(
        self,
        symbols: str = "AAPL",
        expirations=None,
        groupBy: str = "strikePrice",
        max_strike_spot_distance: int = 100,
    ):
        """Query function for gamma_exposure using QueryManager"""
        return SyncQueryFunctions.options.gamma_exposure(
            self.__query_manager__,
            symbols,
            expirations,
            groupBy,
            max_strike_spot_distance,
        )

    def max_pain_vol_skew(
        self,
        symbols: str = "AAPL",
        raw: int = 1,
        expirations=None,
        groupBy: str = "expirationDate",
        max_strike_spot_distance: int = 40,
    ):
        """Query function for max_pain_vol_skew using QueryManager"""
        return SyncQueryFunctions.options.max_pain_vol_skew(
            self.__query_manager__,
            symbols,
            raw,
            expirations,
            groupBy,
            max_strike_spot_distance,
        )

    def options_prices(
        self,
        baseSymbol: str = "AAPL",
        groupBy: str = "optionType",
        expirationDate=None,
        orderBy: str = "strikePrice",
        orderDir: str = "asc",
        optionsOverview: str = "true",
        raw: int = 1,
    ):
        """Query function for options_prices using QueryManager"""
        return SyncQueryFunctions.options.options_prices(
            self.__query_manager__,
            baseSymbol,
            groupBy,
            expirationDate,
            orderBy,
            orderDir,
            optionsOverview,
            raw,
        )

    def put_call_ratio(
        self,
        symbol: str = "AAPL",
        raw: int = 1,
        page: int = 1,
        limit: int = 100,
    ):
        """Query function for put_call_ratio using QueryManager"""
        return SyncQueryFunctions.options.put_call_ratio(
            self.__query_manager__, symbol, raw, page, limit
        )

    def historical_put_call_ratios(
        self,
        symbol: str = "AAPL",
        limit: int = 200,
        orderBy: str = "date",
        orderDir: str = "desc",
    ):
        """Query function for put_call_ratio_historical using QueryManager"""
        return SyncQueryFunctions.options.put_call_ratio_historical(
            self.__query_manager__, symbol, limit, orderBy, orderDir
        )

    def historical_iv_by_days_to_exp(
        self,
        symbol: str = "AAPL",
        limit: int = 999,
        orderBy: str = "date",
        orderDir: str = "desc",
        groupBy: str = "date",
    ):
        """Query function for dte_histo_iv using QueryManager"""
        return SyncQueryFunctions.options.dte_histo_iv(
            self.__query_manager__, symbol, limit, orderBy, orderDir, groupBy
        )

    def historical_iv_by_exp_dates(
        self, symbol: str = "AAPL", expirations=None, groupBy: str = "date"
    ):
        """Query function for ex_histo_iv using QueryManager"""
        return SyncQueryFunctions.options.ex_histo_iv(
            self.__query_manager__, symbol, expirations, groupBy
        )

    def historical_volatility(
        self,
        symbols: str = "AAPL",
        limit: int = 999,
        period: int = 30,
        orderBy: str = "tradeTime",
        orderDir: str = "desc",
        raw: int = 1,
    ):
        """Query function for historical_volatility using QueryManager"""
        return SyncQueryFunctions.options.historical_volatility(
            self.__query_manager__,
            symbols,
            limit,
            period,
            orderBy,
            orderDir,
            raw,
        )

    def historical_iv_rank_percentile(
        self,
        symbol: str = "AAPL",
        limit: int = 360,
        orderBy: str = "date",
        orderDir: str = "desc",
        raw: int = 1,
    ):
        """Query function for iv_rank_percentile using QueryManager"""
        return SyncQueryFunctions.options.iv_rank_percentile(
            self.__query_manager__, symbol, limit, orderBy, orderDir, raw
        )
