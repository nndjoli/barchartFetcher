# Module: long_call_put
from urllib.parse import urlencode


def long_call(
    baseSymbol: str = "AAPL",
    delta_low: int | float = 0.2,
    delta_high: int | float = 0.9,
    orderBy: str = "strikePrice",
    orderDir: str = "desc",
    expirationDate=None,
    expirationType=None,
    page: int = 1,
    limit: int = 100,
    raw: int = 1,
) -> str:
    """URL builder for long_call"""
    base_url = "https://www.barchart.com/proxies/core-api/v1/options/get"
    params = {
        f"between(delta,{delta_low},{delta_high})": "",
        "baseSymbol": baseSymbol,
        "orderBy": orderBy,
        "orderDir": orderDir,
        "ge(tradeTime,previousTradingDay)": "",
        "eq(symbolType,call)": "",
        "page": page,
        "limit": limit,
        "raw": raw,
        "fields": "baseSymbol,underlyingLastPrice,expirationDate,daysToExpiration,strike,moneyness,symbol,baseSymbol,askPrice,timePremiumAskPercent,breakEvenAsk,percentToBreakEvenAsk,netDebit,daysToExpiration,volume,openInterest,impliedVolatilityRank1y,delta,breakEvenProbability,tradeTime,otmProbability,averageVolatility,baseNextEarningsDate,timeCode,dividendExDate,historicVolatility30d,baseTrendSpotterSignal,baseTrendSpotterStrength,symbolCode,symbolType",
        "meta": "expirations,field.shortName,field.type,field.description",
    }
    if expirationDate:
        params["expirationDate"] = expirationDate
    if expirationType:
        params["expirationType"] = expirationType

    query = urlencode(params)
    url = base_url + "?" + query
    return url


def long_put(
    delta_low: str = "-0.9",
    delta_high: str = "-0.2",
    baseSymbol: str = "AAPL",
    orderBy: str = "strikePrice",
    orderDir: str = "desc",
    expirationDate=None,
    expirationType=None,
    page: int = 1,
    limit: int = 100,
    raw: int = 1,
) -> str:
    """URL builder for long_put"""
    base_url = "https://www.barchart.com/proxies/core-api/v1/options/get"
    params = {
        f"between(delta,{delta_low},{delta_high})": f"{delta_low},{delta_high}",
        "baseSymbol": baseSymbol,
        "orderBy": orderBy,
        "orderDir": orderDir,
        "ge(tradeTime,previousTradingDay)": "",
        "eq(symbolType,put)": "",
        "page": page,
        "limit": limit,
        "raw": raw,
        "fields": "baseSymbol,underlyingLastPrice,expirationDate,daysToExpiration,strike,moneyness,symbol,baseSymbol,askPrice,timePremiumAskPercent,breakEvenAsk,percentToBreakEvenAsk,netDebit,daysToExpiration,volume,openInterest,impliedVolatilityRank1y,delta,breakEvenProbability,tradeTime,otmProbability,averageVolatility,baseNextEarningsDate,timeCode,dividendExDate,historicVolatility30d,baseTrendSpotterSignal,baseTrendSpotterStrength,symbolCode,symbolType",
        "meta": "expirations,field.shortName,field.type,field.description",
    }
    if expirationDate:
        params["expirationDate"] = expirationDate
    if expirationType:
        params["expirationType"] = expirationType
    query = urlencode(params)
    url = base_url + "?" + query
    return url
