def dte_histo_iv(
    query_manager,
    symbol: str = "AAPL",
    limit: int = 999,
    orderBy: str = "date",
    orderDir: str = "desc",
    groupBy: str = "date",
):
    """Query function for dte_histo_iv using QueryManager"""
    from barchartFetcher.utils.url_builders.volatility_charts import (
        volatility_charts,
    )

    url = volatility_charts.dte_histo_iv(
        symbol=symbol,
        limit=limit,
        orderBy=orderBy,
        orderDir=orderDir,
        groupBy=groupBy,
    )
    return query_manager.sync_query(url=url)


def ex_histo_iv(
    query_manager,
    symbol: str = "AAPL",
    expirations=None,
    groupBy: str = "date",
):
    """Query function for ex_histo_iv using QueryManager"""
    from barchartFetcher.utils.url_builders.volatility_charts import (
        volatility_charts,
    )

    url = volatility_charts.ex_histo_iv(
        symbol=symbol, expirations=expirations, groupBy=groupBy
    )
    return query_manager.sync_query(url=url)


def historical_volatility(
    query_manager,
    symbols: str = "AAPL",
    limit: int = 999,
    period: int = 30,
    orderBy: str = "tradeTime",
    orderDir: str = "desc",
    raw: int = 1,
):
    """Query function for historical_volatility using QueryManager"""
    from barchartFetcher.utils.url_builders.volatility_charts import (
        volatility_charts,
    )

    url = volatility_charts.historical_volatility(
        symbols=symbols,
        limit=limit,
        period=period,
        orderBy=orderBy,
        orderDir=orderDir,
        raw=raw,
    )
    return query_manager.sync_query(url=url)


def iv_rank_percentile(
    query_manager,
    symbol: str = "AAPL",
    limit: int = 360,
    orderBy: str = "date",
    orderDir: str = "desc",
    raw: int = 1,
):
    """Query function for iv_rank_percentile using QueryManager"""
    from barchartFetcher.utils.url_builders.volatility_charts import (
        volatility_charts,
    )

    url = volatility_charts.iv_rank_percentile(
        symbol=symbol, limit=limit, orderBy=orderBy, orderDir=orderDir, raw=raw
    )
    return query_manager.sync_query(url=url)
