def long_call_condor(
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
    """Query function for long_call_condor using QueryManager"""
    from barchartFetcher.utils.url_builders.condor import condor

    url = condor.long_call_condor(
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


def long_iron_condor(
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
    """Query function for long_iron_condor using QueryManager"""
    from barchartFetcher.utils.url_builders.condor import condor

    url = condor.long_iron_condor(
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


def long_put_condor(
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
    """Query function for long_put_condor using QueryManager"""
    from barchartFetcher.utils.url_builders.condor import condor

    url = condor.long_put_condor(
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


def short_call_condor(
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
    """Query function for short_call_condor using QueryManager"""
    from barchartFetcher.utils.url_builders.condor import condor

    url = condor.short_call_condor(
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


def short_iron_condor(
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
    """Query function for short_iron_condor using QueryManager"""
    from barchartFetcher.utils.url_builders.condor import condor

    url = condor.short_iron_condor(
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


def short_put_condor(
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
    """Query function for short_put_condor using QueryManager"""
    from barchartFetcher.utils.url_builders.condor import condor

    url = condor.short_put_condor(
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
