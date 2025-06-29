def analyst_rating(query_manager, symbols: str = "AAPL", raw: int = 1):
    """Query function for analyst_rating using QueryManager"""
    from barchartFetcher.utils.url_builders.overview import overview

    url = overview.analyst_rating(symbols=symbols, raw=raw)
    return query_manager.sync_query(url=url)


def fundamentals(query_manager, symbols: str = "AAPL", raw: int = 1):
    """Query function for fundamentals using QueryManager"""
    from barchartFetcher.utils.url_builders.overview import overview

    url = overview.fundamentals(symbols=symbols, raw=raw)
    return query_manager.sync_query(url=url)


def options_overview(query_manager, symbols: str = "AAPL", raw: int = 1):
    """Query function for options_overview using QueryManager"""
    from barchartFetcher.utils.url_builders.overview import overview

    url = overview.options_overview(symbols=symbols, raw=raw)
    return query_manager.sync_query(url=url)


def price_performance(query_manager, symbols: str = "AAPL", raw: int = 1):
    """Query function for price_performance using QueryManager"""
    from barchartFetcher.utils.url_builders.overview import overview

    url = overview.price_performance(symbols=symbols, raw=raw)
    return query_manager.sync_query(url=url)


def quote(query_manager, symbols: str = "AAPL", raw: int = 1):
    """Query function for quote using QueryManager"""
    from barchartFetcher.utils.url_builders.overview import overview

    url = overview.quote(symbols=symbols, raw=raw)
    return query_manager.sync_query(url=url)


def technical_opinion(query_manager, symbols: str = "AAPL", raw: int = 1):
    """Query function for technical_opinion using QueryManager"""
    from barchartFetcher.utils.url_builders.overview import overview

    url = overview.technical_opinion(symbols=symbols, raw=raw)
    return query_manager.sync_query(url=url)
