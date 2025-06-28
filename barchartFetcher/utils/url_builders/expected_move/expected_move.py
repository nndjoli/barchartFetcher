# Module: expected_move
from urllib.parse import urlencode


def earnings(
    symbol: str = "AAPL", type: str = "events", events: str = "earnings"
) -> str:
    """URL builder for earnings"""
    base_url = "https://www.barchart.com/proxies/core-api/v1/historical/get"
    params = {
        "symbol": symbol,
        "type": type,
        "events": events,
        "fields": "tradeTime.format(Y-m-d),value,event",
    }
    query = urlencode(params)
    return base_url + "?" + query


def expected_move(
    symbol: str = "AAPL",
    orderBy: str = "expirationDate",
    orderDir: str = "asc",
    raw: int = 1,
    page: int = 1,
    limit: int = 100,
) -> str:
    """URL builder for expected_move"""
    base_url = (
        "https://www.barchart.com/proxies/core-api/v1/options-expirations/get"
    )
    params = {
        "symbol": symbol,
        "orderBy": orderBy,
        "orderDir": orderDir,
        "raw": raw,
        "page": page,
        "limit": limit,
        "fields": "expirationDate,expirationType,daysToExpiration,baseLastPrice,impliedMove,impliedMovePercent,baseUpperPrice,baseLowerPrice,averageVolatility,baseNextEarningsDate,baseTimeCode,symbolCode,symbolType",
        "meta": "field.shortName,field.description,field.type",
    }
    query = urlencode(params)
    return base_url + "?" + query
