def income_statement(
    query_manager,
    symbol: str = "AAPL",
    frequency: str = "annual",
    page: int = 1,
):
    """Query function for income_statement using QueryManager

    frequency == "annual" or frequency == "quarterly"

    """
    if frequency not in ["annual", "quarterly"]:
        raise ValueError("Frequency must be 'annual' or 'quarterly'.")

    if format not in ["dataframe", "dict"]:
        raise ValueError("Format must be 'dataframe' or 'dict'.")

    url = f"https://www.barchart.com/stocks/quotes/{symbol}/income-statement/{frequency}?reportPage={page}"

    data = query_manager.sync_query(url=url, output_format="html")

    return data
