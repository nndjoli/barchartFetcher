def analyst_ratings(query_manager, symbol: str = "AAPL", raw: str = "1"):
    """Query function for analyst_ratings using QueryManager"""
    from barchartFetcher.utils.url_builders.analyst_ratings import (
        analyst_ratings,
    )

    url = analyst_ratings(symbol=symbol, raw=raw)
    return query_manager.sync_query(url=url)
