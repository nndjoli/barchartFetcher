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
        """Query function for long_call_butterfly using QueryManager"""
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
        """Query function for long_iron_butterfly using QueryManager"""
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
        """Query function for long_put_butterfly using QueryManager"""
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
        """Query function for short_call_butterfly using QueryManager"""
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
        """Query function for short_iron_butterfly using QueryManager"""
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
        """Query function for short_put_butterfly using QueryManager"""
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
        """Query function for long_call_condor using QueryManager"""
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
        """Query function for long_iron_condor using QueryManager"""
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
        """Query function for long_put_condor using QueryManager"""
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
        """Query function for short_call_condor using QueryManager"""
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
        """Query function for short_iron_condor using QueryManager"""
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
        """Query function for short_put_condor using QueryManager"""
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
        """Query function for covered_calls using QueryManager"""
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
        """Query function for long_call_calendar using QueryManager"""
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
        """Query function for long_call_diagonal using QueryManager"""
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
        """Query function for long_put_calendar using QueryManager"""
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
        """Query function for long_put_diagonal using QueryManager"""
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
        """Query function for short_call_diagonal using QueryManager"""
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
        """Query function for short_put_diagonal using QueryManager"""
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
        """Query function for long_call using QueryManager"""
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
        """Query function for long_put using QueryManager"""
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
        """Query function for naked_puts using QueryManager"""
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
        """Query function for long_collar_spread using QueryManager"""
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
        """Query function for married_puts using QueryManager"""
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
        """Query function for long_straddle using QueryManager"""
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
        """Query function for long_strangle using QueryManager"""
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
        """Query function for short_straddle using QueryManager"""
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
        """Query function for short_strangle using QueryManager"""
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
        """Query function for bear_call_spreads using QueryManager"""
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
        """Query function for bear_put_spreads using QueryManager"""
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
        """Query function for bull_call_spreads using QueryManager"""
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
        """Query function for bull_put_spreads using QueryManager"""
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
