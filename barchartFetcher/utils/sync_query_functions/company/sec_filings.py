def sec_filings(
    query_manager,
    symbol: str = "AAPL",
    transactions: int | float = 1,
    limit: int = 20,
):
    """Query function for sec_filings using QueryManager"""
    from barchartFetcher.utils.url_builders.sec_filings import sec_filings

    url = sec_filings(symbol=symbol, transactions=transactions, limit=limit)
    return query_manager.sync_query(url=url)
