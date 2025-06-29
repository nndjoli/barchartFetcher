def composite_indicator(query_manager, symbols: str = "AAPL", raw: int = 1):
    """Query function for composite_indicator using QueryManager"""
    from barchartFetcher.utils.url_builders.opinion import composite_indicator

    url = composite_indicator(symbols=symbols, raw=raw)
    return query_manager.sync_query(url=url)


def long_term_indicators(query_manager, symbols: str = "AAPL", raw: int = 1):
    """Query function for long_term_indicators using QueryManager"""
    from barchartFetcher.utils.url_builders.opinion import long_term_indicators

    url = long_term_indicators(symbols=symbols, raw=raw)
    return query_manager.sync_query(url=url)


def medium_term_indicators(query_manager, symbols: str = "AAPL", raw: int = 1):
    """Query function for medium_term_indicators using QueryManager"""
    from barchartFetcher.utils.url_builders.opinion import (
        medium_term_indicators,
    )

    url = medium_term_indicators(symbols=symbols, raw=raw)
    return query_manager.sync_query(url=url)


def opinion(query_manager, symbols: str = "AAPL", raw: int = 1):
    """Query function for opinion using QueryManager"""
    from barchartFetcher.utils.url_builders.opinion import opinion

    url = opinion(symbols=symbols, raw=raw)
    return query_manager.sync_query(url=url)


def short_term_indicators(query_manager, symbols: str = "AAPL", raw: int = 1):
    """Query function for short_term_indicators using QueryManager"""
    from barchartFetcher.utils.url_builders.opinion import (
        short_term_indicators,
    )

    url = short_term_indicators(symbols=symbols, raw=raw)
    return query_manager.sync_query(url=url)
