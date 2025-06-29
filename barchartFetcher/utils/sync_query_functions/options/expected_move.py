def earnings(
    query_manager,
    symbol: str = "AAPL",
    type: str = "events",
    events: str = "earnings",
):
    """Query function for earnings using QueryManager"""
    from barchartFetcher.utils.url_builders.expected_move import earnings

    url = earnings(symbol=symbol, type=type, events=events)
    return query_manager.sync_query(url=url)


def expected_move(
    query_manager,
    symbol: str = "AAPL",
    orderBy: str = "expirationDate",
    orderDir: str = "asc",
    raw: int = 1,
    page: int = 1,
    limit: int = 100,
):
    """Query function for expected_move using QueryManager"""
    from barchartFetcher.utils.url_builders.expected_move import expected_move

    url = expected_move(
        symbol=symbol,
        orderBy=orderBy,
        orderDir=orderDir,
        raw=raw,
        page=page,
        limit=limit,
    )
    return query_manager.sync_query(url=url)
