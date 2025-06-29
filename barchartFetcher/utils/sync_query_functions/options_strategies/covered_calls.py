def covered_calls(
    query_manager,
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
    from barchartFetcher.utils.url_builders.covered_calls import covered_calls

    url = covered_calls(
        baseSymbol=baseSymbol,
        delta_low=delta_low,
        delta_high=delta_high,
        expirationDate=expirationDate,
        expirationType=expirationType,
        orderBy=orderBy,
        orderDir=orderDir,
        page=page,
        raw=raw,
    )
    return query_manager.sync_query(url=url)
