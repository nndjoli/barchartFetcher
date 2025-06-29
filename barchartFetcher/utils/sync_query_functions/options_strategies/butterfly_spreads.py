def long_call_butterfly(
    query_manager,
    baseSymbol: str = "AAPL",
    orderBy: str = "breakEvenProbability",
    orderDir: str = "desc",
    expirationDate=None,
    expirationType=None,
    page: int = 1,
    limit: int = 100,
    raw: int = 1,
):
    """Query function for long_call_butterfly using QueryManager"""
    from barchartFetcher.utils.url_builders.butterfly_spreads import (
        butterfly_spreads,
    )

    url = butterfly_spreads.long_call_butterfly(
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


def long_iron_butterfly(
    query_manager,
    baseSymbol: str = "AAPL",
    orderBy: str = "breakEvenProbability",
    orderDir: str = "desc",
    expirationDate=None,
    expirationType=None,
    page: int = 1,
    limit: int = 100,
    raw: int = 1,
):
    """Query function for long_iron_butterfly using QueryManager"""
    from barchartFetcher.utils.url_builders.butterfly_spreads import (
        butterfly_spreads,
    )

    url = butterfly_spreads.long_iron_butterfly(
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


def long_put_butterfly(
    query_manager,
    baseSymbol: str = "AAPL",
    orderBy: str = "breakEvenProbability",
    orderDir: str = "desc",
    expirationDate=None,
    expirationType=None,
    page: int = 1,
    limit: int = 100,
    raw: int = 1,
):
    """Query function for long_put_butterfly using QueryManager"""
    from barchartFetcher.utils.url_builders.butterfly_spreads import (
        butterfly_spreads,
    )

    url = butterfly_spreads.long_put_butterfly(
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


def short_call_butterfly(
    query_manager,
    baseSymbol: str = "AAPL",
    orderBy: str = "lossProbability",
    orderDir: str = "asc",
    expirationDate=None,
    expirationType=None,
    page: int = 1,
    limit: int = 100,
    raw: int = 1,
):
    """Query function for short_call_butterfly using QueryManager"""
    from barchartFetcher.utils.url_builders.butterfly_spreads import (
        butterfly_spreads,
    )

    url = butterfly_spreads.short_call_butterfly(
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


def short_iron_butterfly(
    query_manager,
    baseSymbol: str = "AAPL",
    orderBy: str = "lossProbability",
    orderDir: str = "asc",
    expirationDate=None,
    expirationType=None,
    page: int = 1,
    limit: int = 100,
    raw: int = 1,
):
    """Query function for short_iron_butterfly using QueryManager"""
    from barchartFetcher.utils.url_builders.butterfly_spreads import (
        butterfly_spreads,
    )

    url = butterfly_spreads.short_iron_butterfly(
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


def short_put_butterfly(
    query_manager,
    baseSymbol: str = "AAPL",
    orderBy: str = "lossProbability",
    orderDir: str = "asc",
    expirationDate=None,
    expirationType=None,
    page: int = 1,
    limit: int = 100,
    raw: int = 1,
):
    """Query function for short_put_butterfly using QueryManager"""
    from barchartFetcher.utils.url_builders.butterfly_spreads import (
        butterfly_spreads,
    )

    url = butterfly_spreads.short_put_butterfly(
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
