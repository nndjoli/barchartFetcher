def options_expirations(query_manager, symbols: str = "AAPL", raw: int = 1):
    """Query function for expirations using QueryManager"""
    from barchartFetcher.utils.url_builders.expirations import expirations

    url = expirations(symbols=symbols, raw=raw)
    return query_manager.sync_query(url=url)
