# Module: put_call_ratios
from urllib.parse import urlencode


def put_call_ratio(
    symbol: str = "AAPL",
    raw: int = 1,
    page: int = 1,
    limit: int = 100,
) -> str:
    """URL builder for put_call_ratio"""
    base_url = (
        "https://www.barchart.com/proxies/core-api/v1/options-expirations/get"
    )
    params = {
        "symbol": symbol,
        "raw": raw,
        "page": page,
        "limit": limit,
        "fields": "expirationDate,expirationType,daysToExpiration,putVolume,callVolume,totalVolume,putCallVolumeRatio,putOpenInterest,callOpenInterest,totalOpenInterest,putCallOpenInterestRatio,averageVolatility,symbolCode,symbolType,lastPrice,dailyLastPrice",
        "meta": "field.shortName,field.description,field.type",
    }
    query = urlencode(params)
    return base_url + "?" + query


def put_call_ratio_historical(
    symbol: str = "AAPL",
    limit: int = 200,
    orderBy: str = "date",
    orderDir: str = "desc",
) -> str:
    """URL builder for put_call_ratio_historical"""
    base_url = (
        "https://www.barchart.com/proxies/core-api/v1/options-historical/get"
    )
    params = {
        "symbol": symbol,
        "limit": limit,
        "orderBy": orderBy,
        "orderDir": orderDir,
        "fields": "putCallVolumeRatio,putCallOpenInterestRatio,date",
    }
    query = urlencode(params)
    return base_url + "?" + query
