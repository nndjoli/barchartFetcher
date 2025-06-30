# Module: insider_trades
from urllib.parse import urlencode


def insider_trades(
    symbol: str,
    orderBy: str = "transactionDate",
    orderDir: str = "desc",
    page: int = 1,
    limit: int = 100,
    raw: int = 1,
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
        "fields": "symbol,fullName,shortJobTitle,transactionType,transactionDate,amount,reportedPrice,usdValue,eodHolding,eodHoldingPercentage,symbolCode,hasOptions,symbolType,lastPrice,dailyLastPrice",
        "meta": "field.shortName,field.type,field.description",
    }
    query = urlencode(params)
    url = base_url + "?" + query
    return url
