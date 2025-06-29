# Module: analyst_ratings
from urllib.parse import urlencode


def analyst_ratings(symbol: str = "AAPL", raw: str = "1") -> str:
    """URL builder for analyst_ratings"""
    base_url = "https://www.barchart.com/proxies/core-api/v1/quotes/get"
    params = {
        "symbol": symbol,
        "raw": raw,
        "fields": "symbol,exchange,symbolName,previousPrice,previousHighPrice,previousLowPrice,weeklyPreviousPrice,weeklyPreviousHighPrice,weeklyPreviousLowPrice,monthlyPreviousPrice,monthlyPreviousHighPrice,monthlyPreviousLowPrice,lastPrice,percentChange,priceChange,openPrice,lowPrice,highPrice,lowPrice1y,highPrice1y,highPrice1y,lowPrice1y,weightedAlpha,meanTargetEstimate,highTargetEstimate,lowTargetEstimate,averageRecommendation,totalRecommendations",
        "meta": "field.shortName,field.type,field.description",
    }
    query = urlencode(params)
    return base_url + "?" + query
