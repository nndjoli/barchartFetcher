# Module: insider_trades
from urllib.parse import urlencode


def insider_trades(
    symbol: str,
    orderBy: str = "transactionDate",
    orderDir: str = "desc",
    page: str = "1",
    limit: str = "100",
    raw: str = "1",
) -> str:
    """URL builder for insider_trades"""
    base_url = "https://www.barchart.com/proxies/core-api/v1/insiderTrades/get"
    params = {
        f"eq(symbol,{symbol})": "",
        "orderBy": orderBy,
        "orderDir": orderDir,
        "page": page,
        "limit": limit,
        "raw": raw,
        "fields": "fullName,shortJobTitle,transactionType,transactionDate,amount,reportedPrice,usdValue,eodHolding,eodHoldingPercentage,symbolCode,hasOptions,symbolType,lastPrice,dailyLastPrice",
        "meta": "field.shortName,field.type,field.description",
    }
    query = urlencode(params)
    return base_url + "?" + query
