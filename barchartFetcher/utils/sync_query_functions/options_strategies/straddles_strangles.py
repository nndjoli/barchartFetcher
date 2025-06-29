def long_straddle(
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
    """Query function for long_straddle using QueryManager"""
    from barchartFetcher.utils.url_builders.straddles_strangles import (
        straddles_strangles,
    )

    url = straddles_strangles.long_straddle(
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


def long_strangle(
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
    """Query function for long_strangle using QueryManager"""
    from barchartFetcher.utils.url_builders.straddles_strangles import (
        straddles_strangles,
    )

    url = straddles_strangles.long_strangle(
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


def short_straddle(
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
    """Query function for short_straddle using QueryManager"""
    from barchartFetcher.utils.url_builders.straddles_strangles import (
        straddles_strangles,
    )

    url = straddles_strangles.short_straddle(
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


def short_strangle(
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
    """Query function for short_strangle using QueryManager"""
    from barchartFetcher.utils.url_builders.straddles_strangles import (
        straddles_strangles,
    )

    url = straddles_strangles.short_strangle(
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
