def bear_call_spreads(
    query_manager,
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
    from barchartFetcher.utils.url_builders.vertical_spreads import (
        vertical_spreads,
    )

    url = vertical_spreads.bear_call_spreads(
        baseSymbol=baseSymbol,
        abs_deltaLeg1_low=abs_deltaLeg1_low,
        abs_deltaLeg1_high=abs_deltaLeg1_high,
        abs_deltaLeg2_low=abs_deltaLeg2_low,
        abs_deltaLeg2_high=abs_deltaLeg2_high,
        riskRewardRatio_low=riskRewardRatio_low,
        riskRewardRatio_high=riskRewardRatio_high,
        orderBy=orderBy,
        orderDir=orderDir,
        expirationDate=expirationDate,
        expirationType=expirationType,
        raw=raw,
    )
    return query_manager.sync_query(url=url)


def bear_put_spreads(
    query_manager,
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
    from barchartFetcher.utils.url_builders.vertical_spreads import (
        vertical_spreads,
    )

    url = vertical_spreads.bear_put_spreads(
        baseSymbol=baseSymbol,
        riskRewardRatio_low=riskRewardRatio_low,
        riskRewardRatio_high=riskRewardRatio_high,
        orderBy=orderBy,
        orderDir=orderDir,
        expirationDate=expirationDate,
        expirationType=expirationType,
        raw=raw,
    )
    return query_manager.sync_query(url=url)


def bull_call_spreads(
    query_manager,
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
    from barchartFetcher.utils.url_builders.vertical_spreads import (
        vertical_spreads,
    )

    url = vertical_spreads.bull_call_spreads(
        baseSymbol=baseSymbol,
        riskRewardRatio_low=riskRewardRatio_low,
        riskRewardRatio_high=riskRewardRatio_high,
        orderBy=orderBy,
        orderDir=orderDir,
        expirationDate=expirationDate,
        expirationType=expirationType,
        raw=raw,
    )
    return query_manager.sync_query(url=url)


def bull_put_spreads(
    query_manager,
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
    from barchartFetcher.utils.url_builders.vertical_spreads import (
        vertical_spreads,
    )

    url = vertical_spreads.bull_put_spreads(
        abs_deltaLeg1_low=abs_deltaLeg1_low,
        abs_deltaLeg1_high=abs_deltaLeg1_high,
        abs_deltaLeg2_low=abs_deltaLeg2_low,
        abs_deltaLeg2_high=abs_deltaLeg2_high,
        riskRewardRatio_low=riskRewardRatio_low,
        riskRewardRatio_high=riskRewardRatio_high,
        baseSymbol=baseSymbol,
        orderBy=orderBy,
        orderDir=orderDir,
        expirationDate=expirationDate,
        expirationType=expirationType,
        raw=raw,
    )
    return query_manager.sync_query(url=url)
