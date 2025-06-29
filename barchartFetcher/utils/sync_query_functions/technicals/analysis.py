def moving_averages(query_manager, symbols: str = "AAPL", raw: int = 1):
    """Query function for moving_averages using QueryManager"""
    from barchartFetcher.utils.url_builders.technical_analysis import (
        technical_analysis,
    )

    url = technical_analysis.moving_averages(symbols=symbols, raw=raw)
    return query_manager.sync_query(url=url)


def stochastics(query_manager, symbols: str = "AAPL", raw: int = 1):
    """Query function for stochastics using QueryManager"""
    from barchartFetcher.utils.url_builders.technical_analysis import (
        technical_analysis,
    )

    url = technical_analysis.stochastics(symbols=symbols, raw=raw)
    return query_manager.sync_query(url=url)


def strength(query_manager, symbols: str = "AAPL", raw: int = 1):
    """Query function for strength using QueryManager"""
    from barchartFetcher.utils.url_builders.technical_analysis import (
        technical_analysis,
    )

    url = technical_analysis.strength(symbols=symbols, raw=raw)
    return query_manager.sync_query(url=url)
