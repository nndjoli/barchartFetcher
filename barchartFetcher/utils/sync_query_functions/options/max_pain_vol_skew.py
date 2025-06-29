def max_pain_vol_skew(
    query_manager,
    symbols: str = "AAPL",
    raw: int = 1,
    expirations=None,
    groupBy: str = "expirationDate",
    max_strike_spot_distance: int = 40,
):
    """Query function for max_pain_vol_skew using QueryManager"""
    from barchartFetcher.utils.url_builders.max_pain_vol_skew import (
        max_pain_vol_skew,
    )

    url = max_pain_vol_skew(
        symbols=symbols,
        raw=raw,
        expirations=expirations,
        groupBy=groupBy,
        max_strike_spot_distance=max_strike_spot_distance,
    )
    return query_manager.sync_query(url=url)
