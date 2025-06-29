def financial_summary_q(query_manager, symbols: str = "AAPL", raw: int = 1):
    """Query function for financial_summary_q using QueryManager"""
    from barchartFetcher.utils.url_builders.financial_summary import (
        financial_summary,
    )

    url = financial_summary.financial_summary_q(symbols=symbols, raw=raw)
    return query_manager.sync_query(url=url)


def financial_summary_y(query_manager, symbols: str = "AAPL", raw: int = 1):
    """Query function for financial_summary_y using QueryManager"""
    from barchartFetcher.utils.url_builders.financial_summary import (
        financial_summary,
    )

    url = financial_summary.financial_summary_y(symbols=symbols, raw=raw)
    return query_manager.sync_query(url=url)
