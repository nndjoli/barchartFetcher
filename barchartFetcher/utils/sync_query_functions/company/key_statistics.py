def company_informations(query_manager, symbols: str = "AAPL", raw: int = 1):
    """Query function for company_informations using QueryManager"""
    from barchartFetcher.utils.url_builders.key_statistics import (
        key_statistics,
    )

    url = key_statistics.company_informations(symbols=symbols, raw=raw)
    return query_manager.sync_query(url=url)


def growth(query_manager, symbols: str = "AAPL", raw: int = 1):
    """Query function for growth using QueryManager"""
    from barchartFetcher.utils.url_builders.key_statistics import (
        key_statistics,
    )

    url = key_statistics.growth(symbols=symbols, raw=raw)
    return query_manager.sync_query(url=url)


def overview(query_manager, symbols: str = "AAPL", raw: int = 1):
    """Query function for overview using QueryManager"""
    from barchartFetcher.utils.url_builders.key_statistics import (
        key_statistics,
    )

    url = key_statistics.overview(symbols=symbols, raw=raw)
    return query_manager.sync_query(url=url)


def per_share_information(query_manager, symbols: str = "AAPL", raw: int = 1):
    """Query function for per_share_information using QueryManager"""
    from barchartFetcher.utils.url_builders.key_statistics import (
        key_statistics,
    )

    url = key_statistics.per_share_information(symbols=symbols, raw=raw)
    return query_manager.sync_query(url=url)


def ratios(query_manager, symbols: str = "AAPL", raw: int = 1):
    """Query function for ratios using QueryManager"""
    from barchartFetcher.utils.url_builders.key_statistics import (
        key_statistics,
    )

    url = key_statistics.ratios(symbols=symbols, raw=raw)
    return query_manager.sync_query(url=url)
