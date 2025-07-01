def insider_trades(
    query_manager,
    symbol: str,
    orderBy: str = "transactionDate",
    orderDir: str = "desc",
    page: int = 1,
    limit: int = 100,
    raw: int = 1,
):
    """Query function for overview using QueryManager"""
    from barchartFetcher.utils.url_builders.insider_trades import (
        insider_trades,
    )

    url = insider_trades(
        symbol=symbol,
        orderBy=orderBy,
        orderDir=orderDir,
        page=page,
        limit=limit,
        raw=raw,
    )
    return query_manager.sync_query(url=url)
