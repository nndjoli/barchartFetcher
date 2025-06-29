def earnings_estimates(query_manager, symbols: str = "AAPL", raw: int = 1):
    """Query function for earnings_estimates using QueryManager"""
    from barchartFetcher.utils.url_builders.earnings_estimates import (
        earnings_estimates,
    )

    url = earnings_estimates(symbols=symbols, raw=raw)
    return query_manager.sync_query(url=url)
