def long_collar_spread(
    query_manager,
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
    from barchartFetcher.utils.url_builders.protection_strategies import (
        protection_strategies,
    )

    url = protection_strategies.long_collar_spread(
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


def married_puts(
    query_manager,
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
    from barchartFetcher.utils.url_builders.protection_strategies import (
        protection_strategies,
    )

    url = protection_strategies.married_puts(
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
