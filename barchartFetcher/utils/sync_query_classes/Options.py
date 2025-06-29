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
        """Historical earnings or events information from Barchart.

        Parameters
        ----------
        symbol : str, default "AAPL"
            Ticker symbol to query.
        type : str, default "events"
            Data type requested by the API.
        events : str, default "earnings"
            Event filter sent to the API.
        """
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
        """Expected move and volatility data from Barchart.

        Parameters
        ----------
        symbol : str, default "AAPL"
            Underlying ticker symbol.
        orderBy : str, default "expirationDate"
            Field used to sort results.
        orderDir : str, default "asc"
            Sorting direction.
        raw : int, default 1
            `1` to request raw values from the API.
        page : int, default 1
            Page number of results.
        limit : int, default 100
            Maximum number of rows to return.
        """
        return SyncQueryFunctions.options.expected_move(
            self.__query_manager__, symbol, orderBy, orderDir, raw, page, limit
        )

    def options_expirations(self, symbols: str = "AAPL", raw: int = 1):
        """List available option expirations on barchart.com.

        Parameters
        ----------
        symbols : str, default "AAPL"
            Comma separated ticker symbols.
        raw : int, default 1
            `1` to request raw values from the API.
        """
        return SyncQueryFunctions.options.options_expirations(
            self.__query_manager__, symbols, raw
        )

    def bullish_bearish_sentiment(self, symbol: str = "AAPL", raw: int = 1):
        """Retrieve bullish/bearish sentiment for `symbol`.

        Parameters
        ----------
        symbol : str, default "AAPL"
            Ticker symbol.
        raw : int, default 1
            `1` to request raw values from the API.
        """
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
        """Fetch notable options flow for `symbol`.

        Parameters
        ----------
        symbol : str, default "AAPL"
            Ticker symbol.
        orderBy : str, default "premium"
            Field used for sorting.
        orderDir : str, default "desc"
            Sorting direction.
        limit : int, default 3
            Number of trades to return.
        min_trade_size : int, default 10
            Minimum trade size filter.
        raw : int, default 1
            `1` to request raw values from the API.
        """
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
        """Returns gamma exposure for `symbols` from Barchart.

        Parameters
        ----------
        symbols : str, default "AAPL"
            Comma separated ticker symbols.
        expirations : list[str] or None
            Expiration dates to include.
        groupBy : str, default "strikePrice"
            Field used for grouping the results.
        max_strike_spot_distance : int, default 100
            Maximum distance between strike price and spot price.
        """
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
        """Return max pain and volatility skew metrics from Barchart.

        Parameters
        ----------
        symbols : str, default "AAPL"
            Comma separated ticker symbols.
        raw : int, default 1
            `1` to request raw values from the API.
        expirations : list[str] or None
            Optional expiration dates filter.
        groupBy : str, default "expirationDate"
            Field used for grouping.
        max_strike_spot_distance : int, default 40
            Maximum distance between strike price and spot price.
        """
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
        """Retrieve option prices for `baseSymbol` from Barchart.

        Parameters
        ----------
        baseSymbol : str, default "AAPL"
            Underlying ticker symbol.
        groupBy : str, default "optionType"
            Field to group the prices by.
        expirationDate : str or None
            Expiration date filter.
        orderBy : str, default "strikePrice"
            Field used for sorting.
        orderDir : str, default "asc"
            Sorting direction.
        optionsOverview : str, default "true"
            Include option overview information.
        raw : int, default 1
            `1` to request raw values from the API.
        """
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
        """Current put/call ratio for `symbol` from Barchart.

        Parameters
        ----------
        symbol : str, default "AAPL"
            Ticker symbol.
        raw : int, default 1
            `1` to request raw values from the API.
        page : int, default 1
            Page number for paginated results.
        limit : int, default 100
            Maximum number of rows to return.
        """
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
        """Historical put/call ratios for `symbol` from Barchart.

        Parameters
        ----------
        symbol : str, default "AAPL"
            Ticker symbol.
        limit : int, default 200
            Maximum number of rows to return.
        orderBy : str, default "date"
            Field to sort by.
        orderDir : str, default "desc"
            Sorting direction.
        """
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
        """Implied volatility by days to expiration from Barchart.

        Parameters
        ----------
        symbol : str, default "AAPL"
            Ticker symbol.
        limit : int, default 999
            Maximum number of rows to return.
        orderBy : str, default "date"
            Field used for sorting.
        orderDir : str, default "desc"
            Sorting direction.
        groupBy : str, default "date"
            Field used for grouping data.
        """
        return SyncQueryFunctions.options.dte_histo_iv(
            self.__query_manager__, symbol, limit, orderBy, orderDir, groupBy
        )

    def historical_iv_by_exp_dates(
        self, symbol: str = "AAPL", expirations=None, groupBy: str = "date"
    ):
        """Implied volatility by expiration dates from Barchart.

        Parameters
        ----------
        symbol : str, default "AAPL"
            Ticker symbol.
        expirations : list[str] or None
            Optional expiration dates to include.
        groupBy : str, default "date"
            Field used to group the data.
        """
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
        """Historical volatility for `symbols` from Barchart.

        Parameters
        ----------
        symbols : str, default "AAPL"
            Comma separated ticker symbols.
        limit : int, default 999
            Maximum number of rows to return.
        period : int, default 30
            Lookback period in days.
        orderBy : str, default "tradeTime"
            Field to sort results by.
        orderDir : str, default "desc"
            Sorting direction.
        raw : int, default 1
            `1` to request raw values from the API.
        """
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
        """Implied volatility rank percentile for `symbol`.

        Parameters
        ----------
        symbol : str, default "AAPL"
            Ticker symbol.
        limit : int, default 360
            Maximum number of rows to return.
        orderBy : str, default "date"
            Field used for sorting.
        orderDir : str, default "desc"
            Sorting direction.
        raw : int, default 1
            `1` to request raw values from the API.
        """
        return SyncQueryFunctions.options.iv_rank_percentile(
            self.__query_manager__, symbol, limit, orderBy, orderDir, raw
        )
