def sector_competitors(
    query_manager,
    symbol: str = "AAPL",
    sector_symbol: str = "-COMC",
    orderBy: str = "weightedAlpha",
    orderDir: str = "desc",
    hasOptions: str = "true",
    page: int = 1,
    limit: int = 100,
    raw: int = 1,
):
    """Query function for sector_competitors using QueryManager"""
    from barchartFetcher.utils.url_builders.sector_competitors import (
        sector_competitors,
    )

    url = sector_competitors(
        symbol=symbol,
        sector_symbol=sector_symbol,
        orderBy=orderBy,
        orderDir=orderDir,
        hasOptions=hasOptions,
        page=page,
        limit=limit,
        raw=raw,
    )
    return query_manager.sync_query(url=url)
