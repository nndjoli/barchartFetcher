def long_call(
    query_manager,
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
    from barchartFetcher.utils.url_builders.long_call_put import long_call_put

    url = long_call_put.long_call(
        baseSymbol=baseSymbol,
        delta_low=delta_low,
        delta_high=delta_high,
        orderBy=orderBy,
        orderDir=orderDir,
        expirationDate=expirationDate,
        expirationType=expirationType,
        page=page,
        limit=limit,
        raw=raw,
    )
    return query_manager.sync_query(url=url)


def long_put(
    query_manager,
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
    from barchartFetcher.utils.url_builders.long_call_put import long_call_put

    url = long_call_put.long_put(
        delta_low=delta_low,
        delta_high=delta_high,
        baseSymbol=baseSymbol,
        orderBy=orderBy,
        orderDir=orderDir,
        expirationDate=expirationDate,
        expirationType=expirationType,
        page=page,
        limit=limit,
        raw=raw,
    )
    return query_manager.sync_query(url=url)
