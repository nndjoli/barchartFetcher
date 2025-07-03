def cash_flow(
    query_manager,
    symbol: str = "AAPL",
    frequency: str = "annual",
    page: int = 1,
):
    """Query function for balance_sheet using QueryManager

    frequency == "annual" or frequency == "quarterly"

    """
    if frequency not in ["annual", "quarterly"]:
        raise ValueError("Frequency must be 'annual' or 'quarterly'.")

    url = f"https://www.barchart.com/stocks/quotes/{symbol}/cash-flow/{frequency}?reportPage={page}"
    data = query_manager.sync_query(url=url, output_format="html")

    return data
