def options_prices(
    query_manager,
    baseSymbol: str = "AAPL",
    groupBy: str = "optionType",
    expirationDate=None,
    orderBy: str = "strikePrice",
    orderDir: str = "asc",
    optionsOverview: str = "true",
    raw: int = 1,
):
    """Query function for options_prices using QueryManager"""
    from barchartFetcher.utils.url_builders.options_prices import (
        options_prices,
    )

    url = options_prices(
        baseSymbol=baseSymbol,
        groupBy=groupBy,
        expirationDate=expirationDate,
        orderBy=orderBy,
        orderDir=orderDir,
        optionsOverview=optionsOverview,
        raw=raw,
    )
    return query_manager.sync_query(url=url)
