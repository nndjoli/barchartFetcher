def long_call_calendar(
    query_manager,
    baseSymbol: str = "AAPL",
    orderBy: str = "ivSkew",
    orderDir: str = "desc",
    expirationDate=None,
    expirationType=None,
    page: int = 1,
    limit: int = 100,
    raw: int = 1,
):
    """Query function for long_call_calendar using QueryManager"""
    from barchartFetcher.utils.url_builders.horizontal_spreads import (
        horizontal_spreads,
    )

    url = horizontal_spreads.long_call_calendar(
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


def long_call_diagonal(
    query_manager,
    baseSymbol: str = "AAPL",
    orderBy: str = "ivSkewInverse",
    orderDir: str = "desc",
    expirationDate=None,
    expirationType=None,
    page: int = 1,
    limit: int = 100,
    raw: int = 1,
):
    """Query function for long_call_diagonal using QueryManager"""
    from barchartFetcher.utils.url_builders.horizontal_spreads import (
        horizontal_spreads,
    )

    url = horizontal_spreads.long_call_diagonal(
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


def long_put_calendar(
    query_manager,
    baseSymbol: str = "AAPL",
    orderBy: str = "ivSkew",
    orderDir: str = "desc",
    expirationDate=None,
    expirationType=None,
    page: int = 1,
    limit: int = 100,
    raw: int = 1,
):
    """Query function for long_put_calendar using QueryManager"""
    from barchartFetcher.utils.url_builders.horizontal_spreads import (
        horizontal_spreads,
    )

    url = horizontal_spreads.long_put_calendar(
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


def long_put_diagonal(
    query_manager,
    baseSymbol: str = "AAPL",
    orderBy: str = "ivSkew",
    orderDir: str = "desc",
    expirationDate=None,
    expirationType=None,
    page: int = 1,
    limit: int = 100,
    raw: int = 1,
):
    """Query function for long_put_diagonal using QueryManager"""
    from barchartFetcher.utils.url_builders.horizontal_spreads import (
        horizontal_spreads,
    )

    url = horizontal_spreads.long_put_diagonal(
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


def short_call_diagonal(
    query_manager,
    baseSymbol: str = "AAPL",
    orderBy: str = "ivSkew",
    orderDir: str = "desc",
    expirationDate=None,
    expirationType=None,
    page: int = 1,
    limit: int = 100,
    raw: int = 1,
):
    """Query function for short_call_diagonal using QueryManager"""
    from barchartFetcher.utils.url_builders.horizontal_spreads import (
        horizontal_spreads,
    )

    url = horizontal_spreads.short_call_diagonal(
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


def short_put_diagonal(
    query_manager,
    baseSymbol: str = "AAPL",
    orderBy: str = "ivSkewInverse",
    orderDir: str = "desc",
    expirationDate=None,
    expirationType=None,
    page: int = 1,
    limit: int = 100,
    raw: int = 1,
):
    """Query function for short_put_diagonal using QueryManager"""
    from barchartFetcher.utils.url_builders.horizontal_spreads import (
        horizontal_spreads,
    )

    url = horizontal_spreads.short_put_diagonal(
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
