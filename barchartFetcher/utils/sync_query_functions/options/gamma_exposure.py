def gamma_exposure(
    query_manager,
    symbols: str = "AAPL",
    expirations=None,
    groupBy: str = "strikePrice",
    max_strike_spot_distance: int = 100,
):
    """Query function for gamma_exposure using QueryManager"""
    from barchartFetcher.utils.url_builders.gex import gex

    url = gex.gamma_exposure(
        symbols=symbols,
        expirations=expirations,
        groupBy=groupBy,
        max_strike_spot_distance=max_strike_spot_distance,
    )
    return query_manager.sync_query(url=url)
