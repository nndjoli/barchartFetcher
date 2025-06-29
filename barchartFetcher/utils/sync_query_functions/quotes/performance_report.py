def lows_highs(query_manager, symbols: str = "AAPL", raw: int = 1):
    """Query function for lows_highs using QueryManager"""
    from barchartFetcher.utils.url_builders.performance_report import (
        performance_report,
    )

    url = performance_report.lows_highs(symbols=symbols, raw=raw)
    return query_manager.sync_query(url=url)


def past_5d(query_manager, symbols: str = "AAPL", raw: int = 1):
    """Query function for past_5d using QueryManager"""
    from barchartFetcher.utils.url_builders.performance_report import (
        performance_report,
    )

    url = performance_report.past_5d(symbols=symbols, raw=raw)
    return query_manager.sync_query(url=url)


def past_5m(query_manager, symbols: str = "AAPL", raw: int = 1):
    """Query function for past_5m using QueryManager"""
    from barchartFetcher.utils.url_builders.performance_report import (
        performance_report,
    )

    url = performance_report.past_5m(symbols=symbols, raw=raw)
    return query_manager.sync_query(url=url)


def past_5w(query_manager, symbols: str = "AAPL", raw: int = 1):
    """Query function for past_5w using QueryManager"""
    from barchartFetcher.utils.url_builders.performance_report import (
        performance_report,
    )

    url = performance_report.past_5w(symbols=symbols, raw=raw)
    return query_manager.sync_query(url=url)


def price_perf(query_manager, symbols: str = "AAPL", raw: int = 1):
    """Query function for price_perf using QueryManager"""
    from barchartFetcher.utils.url_builders.performance_report import (
        performance_report,
    )

    url = performance_report.price_perf(symbols=symbols, raw=raw)
    return query_manager.sync_query(url=url)
