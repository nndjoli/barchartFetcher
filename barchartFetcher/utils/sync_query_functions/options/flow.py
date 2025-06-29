def bullish_bearish_sentiment(
    query_manager, symbol: str = "AAPL", raw: int = 1
):
    """Query function for bullish_bearish_sentiment using QueryManager"""
    from barchartFetcher.utils.url_builders.options_flow import (
        bullish_bearish_sentiment,
    )

    url = bullish_bearish_sentiment(symbol=symbol, raw=raw)
    return query_manager.sync_query(url=url)


def options_flow(
    query_manager,
    symbol: str = "AAPL",
    orderBy: str = "premium",
    orderDir: str = "desc",
    limit: int = 3,
    min_trade_size: int = 10,
    raw: int = 1,
):
    """Query function for options_flow using QueryManager"""
    from barchartFetcher.utils.url_builders.options_flow import options_flow

    url = options_flow(
        symbol=symbol,
        orderBy=orderBy,
        orderDir=orderDir,
        limit=limit,
        min_trade_size=min_trade_size,
        raw=raw,
    )
    return query_manager.sync_query(url=url)
