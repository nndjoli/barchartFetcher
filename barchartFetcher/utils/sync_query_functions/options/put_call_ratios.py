def put_call_ratio(
    query_manager,
    symbol: str = "AAPL",
    raw: int = 1,
    page: int = 1,
    limit: int = 100,
):
    """Query function for put_call_ratio using QueryManager"""
    from barchartFetcher.utils.url_builders.put_call_ratios import (
        put_call_ratios,
    )

    url = put_call_ratios.put_call_ratio(
        symbol=symbol, raw=raw, page=page, limit=limit
    )
    return query_manager.sync_query(url=url)


def put_call_ratio_historical(
    query_manager,
    symbol: str = "AAPL",
    limit: int = 200,
    orderBy: str = "date",
    orderDir: str = "desc",
):
    """Query function for put_call_ratio_historical using QueryManager"""
    from barchartFetcher.utils.url_builders.put_call_ratios import (
        put_call_ratios,
    )

    url = put_call_ratios.put_call_ratio_historical(
        symbol=symbol, limit=limit, orderBy=orderBy, orderDir=orderDir
    )
    return query_manager.sync_query(url=url)
