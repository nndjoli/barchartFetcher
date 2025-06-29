def naked_puts(
    query_manager,
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
    from barchartFetcher.utils.url_builders.naked_puts import naked_puts

    url = naked_puts(
        delta_low=delta_low,
        delta_high=delta_high,
        baseSymbol=baseSymbol,
        orderBy=orderBy,
        orderDir=orderDir,
        expirationDate=expirationDate,
        expirationType=expirationType,
        page=page,
        raw=raw,
    )
    return query_manager.sync_query(url=url)
