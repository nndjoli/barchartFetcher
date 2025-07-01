from barchartFetcher.utils import QueryManager, SyncQueryFunctions


class OptionsStrategies:
    def __init__(self):
        self.__query_manager__ = QueryManager()

    def long_call_butterfly(
        self,
        baseSymbol: str = "AAPL",
        orderBy: str = "breakEvenProbability",
        orderDir: str = "desc",
        expirationDate=None,
        expirationType=None,
        page: int = 1,
        limit: int = 100,
        raw: int = 1,
    ):
        """Search for long call butterfly setups on barchart.com.

        Parameters
        ----------
        baseSymbol : str, default "AAPL"
            Underlying ticker symbol.
        orderBy : str, default "breakEvenProbability"
            Field used to sort results.
        orderDir : str, default "desc"
            Sorting direction.
        expirationDate : str or None
            Optional expiration date filter.
        expirationType : str or None
            Expiration type such as `monthly`.
        page : int, default 1
            Page number to return.
        limit : int, default 100
            Maximum number of strategies.
        raw : int, default 1
            `1` to request raw values from the API.
        """
        return SyncQueryFunctions.options_strategies.long_call_butterfly(
            self.__query_manager__,
            baseSymbol,
            orderBy,
            orderDir,
            expirationDate,
            expirationType,
            page,
            limit,
            raw,
        )

    def long_iron_butterfly(
        self,
        baseSymbol: str = "AAPL",
        orderBy: str = "breakEvenProbability",
        orderDir: str = "desc",
        expirationDate=None,
        expirationType=None,
        page: int = 1,
        limit: int = 100,
        raw: int = 1,
    ):
        """Search for long iron butterfly strategies on barchart.com.

        Parameters
        ----------
        baseSymbol : str, default "AAPL"
            Underlying ticker symbol.
        orderBy : str, default "breakEvenProbability"
            Field used to sort results.
        orderDir : str, default "desc"
            Sorting direction.
        expirationDate : str or None
            Optional expiration date filter.
        expirationType : str or None
            Expiration type such as `monthly`.
        page : int, default 1
            Page number to return.
        limit : int, default 100
            Maximum number of strategies.
        raw : int, default 1
            `1` to request raw values from the API.
        """
        return SyncQueryFunctions.options_strategies.long_iron_butterfly(
            self.__query_manager__,
            baseSymbol,
            orderBy,
            orderDir,
            expirationDate,
            expirationType,
            page,
            limit,
            raw,
        )

    def long_put_butterfly(
        self,
        baseSymbol: str = "AAPL",
        orderBy: str = "breakEvenProbability",
        orderDir: str = "desc",
        expirationDate=None,
        expirationType=None,
        page: int = 1,
        limit: int = 100,
        raw: int = 1,
    ):
        """Search for long put butterfly strategies on barchart.com.

        Parameters
        ----------
        baseSymbol : str, default "AAPL"
            Underlying ticker symbol.
        orderBy : str, default "breakEvenProbability"
            Field used to sort results.
        orderDir : str, default "desc"
            Sorting direction.
        expirationDate : str or None
            Optional expiration date filter.
        expirationType : str or None
            Expiration type such as `monthly`.
        page : int, default 1
            Page number to return.
        limit : int, default 100
            Maximum number of strategies.
        raw : int, default 1
            `1` to request raw values from the API.
        """
        return SyncQueryFunctions.options_strategies.long_put_butterfly(
            self.__query_manager__,
            baseSymbol,
            orderBy,
            orderDir,
            expirationDate,
            expirationType,
            page,
            limit,
            raw,
        )

    def short_call_butterfly(
        self,
        baseSymbol: str = "AAPL",
        orderBy: str = "lossProbability",
        orderDir: str = "asc",
        expirationDate=None,
        expirationType=None,
        page: int = 1,
        limit: int = 100,
        raw: int = 1,
    ):
        """Search for short call butterfly strategies on barchart.com.

        Parameters
        ----------
        baseSymbol : str, default "AAPL"
            Underlying ticker symbol.
        orderBy : str, default "lossProbability"
            Field used to sort results.
        orderDir : str, default "asc"
            Sorting direction.
        expirationDate : str or None
            Optional expiration date filter.
        expirationType : str or None
            Expiration type such as `monthly`.
        page : int, default 1
            Page number to return.
        limit : int, default 100
            Maximum number of strategies.
        raw : int, default 1
            `1` to request raw values from the API.
        """
        return SyncQueryFunctions.options_strategies.short_call_butterfly(
            self.__query_manager__,
            baseSymbol,
            orderBy,
            orderDir,
            expirationDate,
            expirationType,
            page,
            limit,
            raw,
        )

    def short_iron_butterfly(
        self,
        baseSymbol: str = "AAPL",
        orderBy: str = "lossProbability",
        orderDir: str = "asc",
        expirationDate=None,
        expirationType=None,
        page: int = 1,
        limit: int = 100,
        raw: int = 1,
    ):
        """Search for short iron butterfly strategies on barchart.com.

        Parameters
        ----------
        baseSymbol : str, default "AAPL"
            Underlying ticker symbol.
        orderBy : str, default "lossProbability"
            Field used to sort results.
        orderDir : str, default "asc"
            Sorting direction.
        expirationDate : str or None
            Optional expiration date filter.
        expirationType : str or None
            Expiration type such as `monthly`.
        page : int, default 1
            Page number to return.
        limit : int, default 100
            Maximum number of strategies.
        raw : int, default 1
            `1` to request raw values from the API.
        """
        return SyncQueryFunctions.options_strategies.short_iron_butterfly(
            self.__query_manager__,
            baseSymbol,
            orderBy,
            orderDir,
            expirationDate,
            expirationType,
            page,
            limit,
            raw,
        )

    def short_put_butterfly(
        self,
        baseSymbol: str = "AAPL",
        orderBy: str = "lossProbability",
        orderDir: str = "asc",
        expirationDate=None,
        expirationType=None,
        page: int = 1,
        limit: int = 100,
        raw: int = 1,
    ):
        """Search for short put butterfly strategies on barchart.com.

        Parameters
        ----------
        baseSymbol : str, default "AAPL"
            Underlying ticker symbol.
        orderBy : str, default "lossProbability"
            Field used to sort results.
        orderDir : str, default "asc"
            Sorting direction.
        expirationDate : str or None
            Optional expiration date filter.
        expirationType : str or None
            Expiration type such as `monthly`.
        page : int, default 1
            Page number to return.
        limit : int, default 100
            Maximum number of strategies.
        raw : int, default 1
            `1` to request raw values from the API.
        """
        return SyncQueryFunctions.options_strategies.short_put_butterfly(
            self.__query_manager__,
            baseSymbol,
            orderBy,
            orderDir,
            expirationDate,
            expirationType,
            page,
            limit,
            raw,
        )

    def long_call_condor(
        self,
        baseSymbol: str = "AAPL",
        orderBy: str = "breakEvenProbability",
        orderDir: str = "desc",
        expirationDate=None,
        expirationType=None,
        page: int = 1,
        limit: int = 100,
        raw: int = 1,
    ):
        """Search for long call condor strategies on barchart.com.

        Parameters
        ----------
        baseSymbol : str, default "AAPL"
            Underlying ticker symbol.
        orderBy : str, default "breakEvenProbability"
            Field used to sort results.
        orderDir : str, default "desc"
            Sorting direction.
        expirationDate : str or None
            Optional expiration date filter.
        expirationType : str or None
            Expiration type such as `monthly`.
        page : int, default 1
            Page number to return.
        limit : int, default 100
            Maximum number of strategies.
        raw : int, default 1
            `1` to request raw values from the API.
        """
        return SyncQueryFunctions.options_strategies.long_call_condor(
            self.__query_manager__,
            baseSymbol,
            orderBy,
            orderDir,
            expirationDate,
            expirationType,
            page,
            limit,
            raw,
        )

    def long_iron_condor(
        self,
        baseSymbol: str = "AAPL",
        orderBy: str = "breakEvenProbability",
        orderDir: str = "desc",
        expirationDate=None,
        expirationType=None,
        page: int = 1,
        limit: int = 100,
        raw: int = 1,
    ):
        """Search for long iron condor strategies on barchart.com.

        Parameters
        ----------
        baseSymbol : str, default "AAPL"
            Underlying ticker symbol.
        orderBy : str, default "breakEvenProbability"
            Field used to sort results.
        orderDir : str, default "desc"
            Sorting direction.
        expirationDate : str or None
            Optional expiration date filter.
        expirationType : str or None
            Expiration type such as `monthly`.
        page : int, default 1
            Page number to return.
        limit : int, default 100
            Maximum number of strategies.
        raw : int, default 1
            `1` to request raw values from the API.
        """
        return SyncQueryFunctions.options_strategies.long_iron_condor(
            self.__query_manager__,
            baseSymbol,
            orderBy,
            orderDir,
            expirationDate,
            expirationType,
            page,
            limit,
            raw,
        )

    def long_put_condor(
        self,
        baseSymbol: str = "AAPL",
        orderBy: str = "breakEvenProbability",
        orderDir: str = "desc",
        expirationDate=None,
        expirationType=None,
        page: int = 1,
        limit: int = 100,
        raw: int = 1,
    ):
        """Search for long put condor strategies on barchart.com.

        Parameters
        ----------
        baseSymbol : str, default "AAPL"
            Underlying ticker symbol.
        orderBy : str, default "breakEvenProbability"
            Field used to sort results.
        orderDir : str, default "desc"
            Sorting direction.
        expirationDate : str or None
            Optional expiration date filter.
        expirationType : str or None
            Expiration type such as `monthly`.
        page : int, default 1
            Page number to return.
        limit : int, default 100
            Maximum number of strategies.
        raw : int, default 1
            `1` to request raw values from the API.
        """
        return SyncQueryFunctions.options_strategies.long_put_condor(
            self.__query_manager__,
            baseSymbol,
            orderBy,
            orderDir,
            expirationDate,
            expirationType,
            page,
            limit,
            raw,
        )

    def short_call_condor(
        self,
        baseSymbol: str = "AAPL",
        orderBy: str = "lossProbability",
        orderDir: str = "asc",
        expirationDate=None,
        expirationType=None,
        page: int = 1,
        limit: int = 100,
        raw: int = 1,
    ):
        """Search for short call condor strategies on barchart.com.

        Parameters
        ----------
        baseSymbol : str, default "AAPL"
            Underlying ticker symbol.
        orderBy : str, default "lossProbability"
            Field used to sort results.
        orderDir : str, default "asc"
            Sorting direction.
        expirationDate : str or None
            Optional expiration date filter.
        expirationType : str or None
            Expiration type such as `monthly`.
        page : int, default 1
            Page number to return.
        limit : int, default 100
            Maximum number of strategies.
        raw : int, default 1
            `1` to request raw values from the API.
        """
        return SyncQueryFunctions.options_strategies.short_call_condor(
            self.__query_manager__,
            baseSymbol,
            orderBy,
            orderDir,
            expirationDate,
            expirationType,
            page,
            limit,
            raw,
        )

    def short_iron_condor(
        self,
        baseSymbol: str = "AAPL",
        orderBy: str = "lossProbability",
        orderDir: str = "asc",
        expirationDate=None,
        expirationType=None,
        page: int = 1,
        limit: int = 100,
        raw: int = 1,
    ):
        """Search for short iron condor strategies on barchart.com.

        Parameters
        ----------
        baseSymbol : str, default "AAPL"
            Underlying ticker symbol.
        orderBy : str, default "lossProbability"
            Field used to sort results.
        orderDir : str, default "asc"
            Sorting direction.
        expirationDate : str or None
            Optional expiration date filter.
        expirationType : str or None
            Expiration type such as `monthly`.
        page : int, default 1
            Page number to return.
        limit : int, default 100
            Maximum number of strategies.
        raw : int, default 1
            `1` to request raw values from the API.
        """
        return SyncQueryFunctions.options_strategies.short_iron_condor(
            self.__query_manager__,
            baseSymbol,
            orderBy,
            orderDir,
            expirationDate,
            expirationType,
            page,
            limit,
            raw,
        )

    def short_put_condor(
        self,
        baseSymbol: str = "AAPL",
        orderBy: str = "lossProbability",
        orderDir: str = "asc",
        expirationDate=None,
        expirationType=None,
        page: int = 1,
        limit: int = 100,
        raw: int = 1,
    ):
        """Search for short put condor strategies on barchart.com.

        Parameters
        ----------
        baseSymbol : str, default "AAPL"
            Underlying ticker symbol.
        orderBy : str, default "lossProbability"
            Field used to sort results.
        orderDir : str, default "asc"
            Sorting direction.
        expirationDate : str or None
            Optional expiration date filter.
        expirationType : str or None
            Expiration type such as `monthly`.
        page : int, default 1
            Page number to return.
        limit : int, default 100
            Maximum number of strategies.
        raw : int, default 1
            `1` to request raw values from the API.
        """
        return SyncQueryFunctions.options_strategies.short_put_condor(
            self.__query_manager__,
            baseSymbol,
            orderBy,
            orderDir,
            expirationDate,
            expirationType,
            page,
            limit,
            raw,
        )

    def covered_calls(
        self,
        baseSymbol: str = "AAPL",
        delta_low: int | float = 0.1,
        delta_high: int | float = 0.6,
        expirationDate=None,
        expirationType=None,
        orderBy: str = "strike",
        orderDir: str = "desc",
        page: int = 1,
        raw: int = 1,
    ):
        """Screen for covered call candidates on barchart.com.

        Parameters
        ----------
        baseSymbol : str, default "AAPL"
            Underlying ticker symbol.
        delta_low : float, default 0.1
            Minimum option delta.
        delta_high : float, default 0.6
            Maximum option delta.
        expirationDate : str or None
            Optional expiration date filter.
        expirationType : str or None
            Expiration type filter.
        orderBy : str, default "strike"
            Field used to sort results.
        orderDir : str, default "desc"
            Sorting direction.
        page : int, default 1
            Page number to return.
        raw : int, default 1
            `1` to request raw values from the API.
        """
        return SyncQueryFunctions.options_strategies.covered_calls(
            self.__query_manager__,
            baseSymbol,
            delta_low,
            delta_high,
            expirationDate,
            expirationType,
            orderBy,
            orderDir,
            page,
            raw,
        )

    def long_call_calendar(
        self,
        baseSymbol: str = "AAPL",
        orderBy: str = "ivSkew",
        orderDir: str = "desc",
        expirationDate=None,
        expirationType=None,
        page: int = 1,
        limit: int = 100,
        raw: int = 1,
    ):
        """Search for long call calendar spreads on barchart.com.

        Parameters
        ----------
        baseSymbol : str, default "AAPL"
            Underlying ticker symbol.
        orderBy : str, default "ivSkew"
            Field used to sort results.
        orderDir : str, default "desc"
            Sorting direction.
        expirationDate : str or None
            Optional expiration date filter.
        expirationType : str or None
            Expiration type filter.
        page : int, default 1
            Page number to return.
        limit : int, default 100
            Maximum number of strategies.
        raw : int, default 1
            `1` to request raw values from the API.
        """
        return SyncQueryFunctions.options_strategies.long_call_calendar(
            self.__query_manager__,
            baseSymbol,
            orderBy,
            orderDir,
            expirationDate,
            expirationType,
            page,
            limit,
            raw,
        )

    def long_call_diagonal(
        self,
        baseSymbol: str = "AAPL",
        orderBy: str = "ivSkewInverse",
        orderDir: str = "desc",
        expirationDate=None,
        expirationType=None,
        page: int = 1,
        limit: int = 100,
        raw: int = 1,
    ):
        """Search for long call diagonal spreads on barchart.com.

        Parameters
        ----------
        baseSymbol : str, default "AAPL"
            Underlying ticker symbol.
        orderBy : str, default "ivSkewInverse"
            Field used to sort results.
        orderDir : str, default "desc"
            Sorting direction.
        expirationDate : str or None
            Optional expiration date filter.
        expirationType : str or None
            Expiration type filter.
        page : int, default 1
            Page number to return.
        limit : int, default 100
            Maximum number of strategies.
        raw : int, default 1
            `1` to request raw values from the API.
        """
        return SyncQueryFunctions.options_strategies.long_call_diagonal(
            self.__query_manager__,
            baseSymbol,
            orderBy,
            orderDir,
            expirationDate,
            expirationType,
            page,
            limit,
            raw,
        )

    def long_put_calendar(
        self,
        baseSymbol: str = "AAPL",
        orderBy: str = "ivSkew",
        orderDir: str = "desc",
        expirationDate=None,
        expirationType=None,
        page: int = 1,
        limit: int = 100,
        raw: int = 1,
    ):
        """Search for long put calendar spreads on barchart.com.

        Parameters
        ----------
        baseSymbol : str, default "AAPL"
            Underlying ticker symbol.
        orderBy : str, default "ivSkew"
            Field used to sort results.
        orderDir : str, default "desc"
            Sorting direction.
        expirationDate : str or None
            Optional expiration date filter.
        expirationType : str or None
            Expiration type filter.
        page : int, default 1
            Page number to return.
        limit : int, default 100
            Maximum number of strategies.
        raw : int, default 1
            `1` to request raw values from the API.
        """
        return SyncQueryFunctions.options_strategies.long_put_calendar(
            self.__query_manager__,
            baseSymbol,
            orderBy,
            orderDir,
            expirationDate,
            expirationType,
            page,
            limit,
            raw,
        )

    def long_put_diagonal(
        self,
        baseSymbol: str = "AAPL",
        orderBy: str = "ivSkew",
        orderDir: str = "desc",
        expirationDate=None,
        expirationType=None,
        page: int = 1,
        limit: int = 100,
        raw: int = 1,
    ):
        """Search for long put diagonal spreads on barchart.com.

        Parameters
        ----------
        baseSymbol : str, default "AAPL"
            Underlying ticker symbol.
        orderBy : str, default "ivSkew"
            Field used to sort results.
        orderDir : str, default "desc"
            Sorting direction.
        expirationDate : str or None
            Optional expiration date filter.
        expirationType : str or None
            Expiration type filter.
        page : int, default 1
            Page number to return.
        limit : int, default 100
            Maximum number of strategies.
        raw : int, default 1
            `1` to request raw values from the API.
        """
        return SyncQueryFunctions.options_strategies.long_put_diagonal(
            self.__query_manager__,
            baseSymbol,
            orderBy,
            orderDir,
            expirationDate,
            expirationType,
            page,
            limit,
            raw,
        )

    def short_call_diagonal(
        self,
        baseSymbol: str = "AAPL",
        orderBy: str = "ivSkew",
        orderDir: str = "desc",
        expirationDate=None,
        expirationType=None,
        page: int = 1,
        limit: int = 100,
        raw: int = 1,
    ):
        """Search for short call diagonal spreads on barchart.com.

        Parameters
        ----------
        baseSymbol : str, default "AAPL"
            Underlying ticker symbol.
        orderBy : str, default "ivSkew"
            Field used to sort results.
        orderDir : str, default "desc"
            Sorting direction.
        expirationDate : str or None
            Optional expiration date filter.
        expirationType : str or None
            Expiration type filter.
        page : int, default 1
            Page number to return.
        limit : int, default 100
            Maximum number of strategies.
        raw : int, default 1
            `1` to request raw values from the API.
        """
        return SyncQueryFunctions.options_strategies.short_call_diagonal(
            self.__query_manager__,
            baseSymbol,
            orderBy,
            orderDir,
            expirationDate,
            expirationType,
            page,
            limit,
            raw,
        )

    def short_put_diagonal(
        self,
        baseSymbol: str = "AAPL",
        orderBy: str = "ivSkewInverse",
        orderDir: str = "desc",
        expirationDate=None,
        expirationType=None,
        page: int = 1,
        limit: int = 100,
        raw: int = 1,
    ):
        """Search for short put diagonal spreads on barchart.com.

        Parameters
        ----------
        baseSymbol : str, default "AAPL"
            Underlying ticker symbol.
        orderBy : str, default "ivSkewInverse"
            Field used to sort results.
        orderDir : str, default "desc"
            Sorting direction.
        expirationDate : str or None
            Optional expiration date filter.
        expirationType : str or None
            Expiration type filter.
        page : int, default 1
            Page number to return.
        limit : int, default 100
            Maximum number of strategies.
        raw : int, default 1
            `1` to request raw values from the API.
        """
        return SyncQueryFunctions.options_strategies.short_put_diagonal(
            self.__query_manager__,
            baseSymbol,
            orderBy,
            orderDir,
            expirationDate,
            expirationType,
            page,
            limit,
            raw,
        )

    def long_call(
        self,
        baseSymbol: str = "AAPL",
        delta_low: int | float = 0.2,
        delta_high: int | float = 0.9,
        orderBy: str = "strikePrice",
        orderDir: str = "desc",
        expirationDate=None,
        expirationType=None,
        page: int = 1,
        limit: int = 100,
        raw: int = 1,
    ):
        """Look for long call opportunities on barchart.com.

        Parameters
        ----------
        baseSymbol : str, default "AAPL"
            Underlying ticker symbol.
        delta_low : float, default 0.2
            Minimum option delta.
        delta_high : float, default 0.9
            Maximum option delta.
        orderBy : str, default "strikePrice"
            Field used to sort results.
        orderDir : str, default "desc"
            Sorting direction.
        expirationDate : str or None
            Optional expiration date filter.
        expirationType : str or None
            Expiration type filter.
        page : int, default 1
            Page number to return.
        limit : int, default 100
            Maximum number of strategies.
        raw : int, default 1
            `1` to request raw values from the API.
        """
        return SyncQueryFunctions.options_strategies.long_call(
            self.__query_manager__,
            baseSymbol,
            delta_low,
            delta_high,
            orderBy,
            orderDir,
            expirationDate,
            expirationType,
            page,
            limit,
            raw,
        )

    def long_put(
        self,
        delta_low: str = "-0.9",
        delta_high: str = "-0.2",
        baseSymbol: str = "AAPL",
        orderBy: str = "strikePrice",
        orderDir: str = "desc",
        expirationDate=None,
        expirationType=None,
        page: int = 1,
        limit: int = 100,
        raw: int = 1,
    ):
        """Look for long put opportunities on barchart.com.

        Parameters
        ----------
        delta_low : str, default "-0.9"
            Minimum option delta.
        delta_high : str, default "-0.2"
            Maximum option delta.
        baseSymbol : str, default "AAPL"
            Underlying ticker symbol.
        orderBy : str, default "strikePrice"
            Field used to sort results.
        orderDir : str, default "desc"
            Sorting direction.
        expirationDate : str or None
            Optional expiration date filter.
        expirationType : str or None
            Expiration type filter.
        page : int, default 1
            Page number to return.
        limit : int, default 100
            Maximum number of strategies.
        raw : int, default 1
            `1` to request raw values from the API.
        """
        return SyncQueryFunctions.options_strategies.long_put(
            self.__query_manager__,
            delta_low,
            delta_high,
            baseSymbol,
            orderBy,
            orderDir,
            expirationDate,
            expirationType,
            page,
            limit,
            raw,
        )

    def naked_puts(
        self,
        delta_low: str = "-0.6",
        delta_high: str = "-0.1",
        baseSymbol: str = "AAPL",
        orderBy: str = "strike",
        orderDir: str = "asc",
        expirationDate=None,
        expirationType=None,
        page: int = 1,
        raw: int = 1,
    ):
        """Return naked put ideas from Barchart.

        Parameters
        ----------
        delta_low : str, default "-0.6"
            Minimum option delta.
        delta_high : str, default "-0.1"
            Maximum option delta.
        baseSymbol : str, default "AAPL"
            Underlying ticker symbol.
        orderBy : str, default "strike"
            Field used to sort results.
        orderDir : str, default "asc"
            Sorting direction.
        expirationDate : str or None
            Optional expiration date filter.
        expirationType : str or None
            Expiration type filter.
        page : int, default 1
            Page number to return.
        raw : int, default 1
            `1` to request raw values from the API.
        """
        return SyncQueryFunctions.options_strategies.naked_puts(
            self.__query_manager__,
            delta_low,
            delta_high,
            baseSymbol,
            orderBy,
            orderDir,
            expirationDate,
            expirationType,
            page,
            raw,
        )

    def long_collar_spread(
        self,
        baseSymbol: str = "AAPL",
        orderBy: str = "strikeLeg1",
        orderDir: str = "asc",
        expirationDate=None,
        expirationType=None,
        page: int = 1,
        limit: int = 100,
        raw: int = 1,
    ):
        """Search for long collar spreads on barchart.com.

        Parameters
        ----------
        baseSymbol : str, default "AAPL"
            Underlying ticker symbol.
        orderBy : str, default "strikeLeg1"
            Field used to sort results.
        orderDir : str, default "asc"
            Sorting direction.
        expirationDate : str or None
            Optional expiration date filter.
        expirationType : str or None
            Expiration type filter.
        page : int, default 1
            Page number to return.
        limit : int, default 100
            Maximum number of strategies.
        raw : int, default 1
            `1` to request raw values from the API.
        """
        return SyncQueryFunctions.options_strategies.long_collar_spread(
            self.__query_manager__,
            baseSymbol,
            orderBy,
            orderDir,
            expirationDate,
            expirationType,
            page,
            limit,
            raw,
        )

    def married_puts(
        self,
        baseSymbol: str = "AAPL",
        orderBy: str = "strikePrice",
        orderDir: str = "asc",
        expirationDate=None,
        expirationType=None,
        page: int = 1,
        limit: int = 100,
        raw: int = 1,
    ):
        """Return married put strategies from Barchart.

        Parameters
        ----------
        baseSymbol : str, default "AAPL"
            Underlying ticker symbol.
        orderBy : str, default "strikePrice"
            Field used to sort results.
        orderDir : str, default "asc"
            Sorting direction.
        expirationDate : str or None
            Optional expiration date filter.
        expirationType : str or None
            Expiration type filter.
        page : int, default 1
            Page number to return.
        limit : int, default 100
            Maximum number of strategies.
        raw : int, default 1
            `1` to request raw values from the API.
        """
        return SyncQueryFunctions.options_strategies.married_puts(
            self.__query_manager__,
            baseSymbol,
            orderBy,
            orderDir,
            expirationDate,
            expirationType,
            page,
            limit,
            raw,
        )

    def long_straddle(
        self,
        baseSymbol: str = "AAPL",
        orderBy: str = "strikeLeg1",
        orderDir: str = "asc",
        expirationDate=None,
        expirationType=None,
        page: int = 1,
        limit: int = 100,
        raw: int = 1,
    ):
        """Search for long straddle setups on barchart.com.

        Parameters
        ----------
        baseSymbol : str, default "AAPL"
            Underlying ticker symbol.
        orderBy : str, default "strikeLeg1"
            Field used to sort results.
        orderDir : str, default "asc"
            Sorting direction.
        expirationDate : str or None
            Optional expiration date filter.
        expirationType : str or None
            Expiration type filter.
        page : int, default 1
            Page number to return.
        limit : int, default 100
            Maximum number of strategies.
        raw : int, default 1
            `1` to request raw values from the API.
        """
        return SyncQueryFunctions.options_strategies.long_straddle(
            self.__query_manager__,
            baseSymbol,
            orderBy,
            orderDir,
            expirationDate,
            expirationType,
            page,
            limit,
            raw,
        )

    def long_strangle(
        self,
        baseSymbol: str = "AAPL",
        orderBy: str = "strikeLeg1",
        orderDir: str = "asc",
        expirationDate=None,
        expirationType=None,
        page: int = 1,
        limit: int = 100,
        raw: int = 1,
    ):
        """Search for long strangle setups on barchart.com.

        Parameters
        ----------
        baseSymbol : str, default "AAPL"
            Underlying ticker symbol.
        orderBy : str, default "strikeLeg1"
            Field used to sort results.
        orderDir : str, default "asc"
            Sorting direction.
        expirationDate : str or None
            Optional expiration date filter.
        expirationType : str or None
            Expiration type filter.
        page : int, default 1
            Page number to return.
        limit : int, default 100
            Maximum number of strategies.
        raw : int, default 1
            `1` to request raw values from the API.
        """
        return SyncQueryFunctions.options_strategies.long_strangle(
            self.__query_manager__,
            baseSymbol,
            orderBy,
            orderDir,
            expirationDate,
            expirationType,
            page,
            limit,
            raw,
        )

    def short_straddle(
        self,
        baseSymbol: str = "AAPL",
        orderBy: str = "strikeLeg1",
        orderDir: str = "asc",
        expirationDate=None,
        expirationType=None,
        page: int = 1,
        limit: int = 100,
        raw: int = 1,
    ):
        """Search for short straddle setups on barchart.com.

        Parameters
        ----------
        baseSymbol : str, default "AAPL"
            Underlying ticker symbol.
        orderBy : str, default "strikeLeg1"
            Field used to sort results.
        orderDir : str, default "asc"
            Sorting direction.
        expirationDate : str or None
            Optional expiration date filter.
        expirationType : str or None
            Expiration type filter.
        page : int, default 1
            Page number to return.
        limit : int, default 100
            Maximum number of strategies.
        raw : int, default 1
            `1` to request raw values from the API.
        """
        return SyncQueryFunctions.options_strategies.short_straddle(
            self.__query_manager__,
            baseSymbol,
            orderBy,
            orderDir,
            expirationDate,
            expirationType,
            page,
            limit,
            raw,
        )

    def short_strangle(
        self,
        baseSymbol: str = "AAPL",
        orderBy: str = "strikeLeg1",
        orderDir: str = "asc",
        expirationDate=None,
        expirationType=None,
        page: int = 1,
        limit: int = 100,
        raw: int = 1,
    ):
        """Search for short strangle setups on barchart.com.

        Parameters
        ----------
        baseSymbol : str, default "AAPL"
            Underlying ticker symbol.
        orderBy : str, default "strikeLeg1"
            Field used to sort results.
        orderDir : str, default "asc"
            Sorting direction.
        expirationDate : str or None
            Optional expiration date filter.
        expirationType : str or None
            Expiration type filter.
        page : int, default 1
            Page number to return.
        limit : int, default 100
            Maximum number of strategies.
        raw : int, default 1
            `1` to request raw values from the API.
        """
        return SyncQueryFunctions.options_strategies.short_strangle(
            self.__query_manager__,
            baseSymbol,
            orderBy,
            orderDir,
            expirationDate,
            expirationType,
            page,
            limit,
            raw,
        )

    def bear_call_spreads(
        self,
        baseSymbol: str = "AAPL",
        abs_deltaLeg1_low: int | float = 0,
        abs_deltaLeg1_high: int | float = 0.6,
        abs_deltaLeg2_low: str = "",
        abs_deltaLeg2_high: int | float = 0.3,
        riskRewardRatio_low: int | float = 2,
        riskRewardRatio_high: int | float = 5,
        orderBy: str = "strikeLeg1",
        orderDir: str = "desc",
        expirationDate=None,
        expirationType=None,
        raw: int = 1,
    ):
        """Bear call spread ideas sourced from Barchart.

        Parameters
        ----------
        baseSymbol : str, default "AAPL"
            Underlying ticker symbol.
        abs_deltaLeg1_low : float, default 0
            Minimum absolute delta for the first leg.
        abs_deltaLeg1_high : float, default 0.6
            Maximum absolute delta for the first leg.
        abs_deltaLeg2_low : str, default ""
            Minimum absolute delta for the second leg.
        abs_deltaLeg2_high : float, default 0.3
            Maximum absolute delta for the second leg.
        riskRewardRatio_low : float, default 2
            Minimum risk/reward ratio.
        riskRewardRatio_high : float, default 5
            Maximum risk/reward ratio.
        orderBy : str, default "strikeLeg1"
            Field used to sort results.
        orderDir : str, default "desc"
            Sorting direction.
        expirationDate : str or None
            Optional expiration date filter.
        expirationType : str or None
            Expiration type filter.
        raw : int, default 1
            `1` to request raw values from the API.
        """
        return SyncQueryFunctions.options_strategies.bear_call_spreads(
            self.__query_manager__,
            baseSymbol,
            abs_deltaLeg1_low,
            abs_deltaLeg1_high,
            abs_deltaLeg2_low,
            abs_deltaLeg2_high,
            riskRewardRatio_low,
            riskRewardRatio_high,
            orderBy,
            orderDir,
            expirationDate,
            expirationType,
            raw,
        )

    def bear_put_spreads(
        self,
        baseSymbol: str = "AAPL",
        riskRewardRatio_low: int | float = 0.33,
        riskRewardRatio_high: int | float = 1.5,
        orderBy: str = "strikeLeg1",
        orderDir: str = "desc",
        expirationDate=None,
        expirationType=None,
        raw: int = 1,
    ):
        """Bear put spread opportunities from Barchart.

        Parameters
        ----------
        baseSymbol : str, default "AAPL"
            Underlying ticker symbol.
        riskRewardRatio_low : float, default 0.33
            Minimum risk/reward ratio.
        riskRewardRatio_high : float, default 1.5
            Maximum risk/reward ratio.
        orderBy : str, default "strikeLeg1"
            Field used to sort results.
        orderDir : str, default "desc"
            Sorting direction.
        expirationDate : str or None
            Optional expiration date filter.
        expirationType : str or None
            Expiration type filter.
        raw : int, default 1
            `1` to request raw values from the API.
        """
        return SyncQueryFunctions.options_strategies.bear_put_spreads(
            self.__query_manager__,
            baseSymbol,
            riskRewardRatio_low,
            riskRewardRatio_high,
            orderBy,
            orderDir,
            expirationDate,
            expirationType,
            raw,
        )

    def bull_call_spreads(
        self,
        baseSymbol: str = "AAPL",
        riskRewardRatio_low: int | float = 0.33,
        riskRewardRatio_high: int | float = 1.5,
        orderBy: str = "strikeLeg1",
        orderDir: str = "asc",
        expirationDate=None,
        expirationType=None,
        raw: int = 1,
    ):
        """Bull call spread ideas sourced from Barchart.

        Parameters
        ----------
        baseSymbol : str, default "AAPL"
            Underlying ticker symbol.
        riskRewardRatio_low : float, default 0.33
            Minimum risk/reward ratio.
        riskRewardRatio_high : float, default 1.5
            Maximum risk/reward ratio.
        orderBy : str, default "strikeLeg1"
            Field used to sort results.
        orderDir : str, default "asc"
            Sorting direction.
        expirationDate : str or None
            Optional expiration date filter.
        expirationType : str or None
            Expiration type filter.
        raw : int, default 1
            `1` to request raw values from the API.
        """
        return SyncQueryFunctions.options_strategies.bull_call_spreads(
            self.__query_manager__,
            baseSymbol,
            riskRewardRatio_low,
            riskRewardRatio_high,
            orderBy,
            orderDir,
            expirationDate,
            expirationType,
            raw,
        )

    def bull_put_spreads(
        self,
        abs_deltaLeg1_low: str = "",
        abs_deltaLeg1_high: int | float = 0.6,
        abs_deltaLeg2_low: int | float = 0,
        abs_deltaLeg2_high: int | float = 0.3,
        riskRewardRatio_low: int | float = 2,
        riskRewardRatio_high: int | float = 5,
        baseSymbol: str = "AAPL",
        orderBy: str = "strikeLeg1",
        orderDir: str = "asc",
        expirationDate=None,
        expirationType=None,
        raw: int = 1,
    ):
        """Bull put spread opportunities from Barchart.

        Parameters
        ----------
        abs_deltaLeg1_low : str, default ""
            Minimum absolute delta for the first leg.
        abs_deltaLeg1_high : float, default 0.6
            Maximum absolute delta for the first leg.
        abs_deltaLeg2_low : float, default 0
            Minimum absolute delta for the second leg.
        abs_deltaLeg2_high : float, default 0.3
            Maximum absolute delta for the second leg.
        riskRewardRatio_low : float, default 2
            Minimum risk/reward ratio.
        riskRewardRatio_high : float, default 5
            Maximum risk/reward ratio.
        baseSymbol : str, default "AAPL"
            Underlying ticker symbol.
        orderBy : str, default "strikeLeg1"
            Field used to sort results.
        orderDir : str, default "asc"
            Sorting direction.
        expirationDate : str or None
            Optional expiration date filter.
        expirationType : str or None
            Expiration type filter.
        raw : int, default 1
            `1` to request raw values from the API.
        """
        return SyncQueryFunctions.options_strategies.bull_put_spreads(
            self.__query_manager__,
            abs_deltaLeg1_low,
            abs_deltaLeg1_high,
            abs_deltaLeg2_low,
            abs_deltaLeg2_high,
            riskRewardRatio_low,
            riskRewardRatio_high,
            baseSymbol,
            orderBy,
            orderDir,
            expirationDate,
            expirationType,
            raw,
        )
