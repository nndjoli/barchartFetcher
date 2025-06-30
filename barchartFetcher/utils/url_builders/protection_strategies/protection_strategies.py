# Module: protection_strategies
from urllib.parse import urlencode


def long_collar_spread(
    baseSymbol: str = "AAPL",
    orderBy: str = "strikeLeg1",
    orderDir: str = "asc",
    expirationDate=None,
    expirationType=None,
    page: int = 1,
    limit: int = 100,
    raw: int = 1,
) -> str:
    """URL builder for long_collar_spread"""
    base_url = "https://www.barchart.com/proxies/core-api/v1/options/long-collar-spread"
    params = {
        "baseSymbol": baseSymbol,
        "orderBy": orderBy,
        "orderDir": orderDir,
        "page": page,
        "limit": limit,
        "raw": raw,
        "fields": "baseSymbol,baseSymbolType,underlyingLastPrice,expirationDate,daysToExpiration,strikeLeg1,bidPriceLeg1,strikeLeg2,askPriceLeg2,breakEven,netDebitCredit,percentOfCost,maxProfit,maxLoss,maxRisk,upside,downside,overallDelta,breakEvenProbability,symbolCode,symbolType,expirationType,legs,daysToExpiration,averageVolatility,baseNextEarningsDate,timeCode,dividendExDate,historicVolatility30d,impliedVolatilityRank1y,baseTrendSpotterSignal,baseTrendSpotterStrength",
        "meta": "expirations,field.shortName,field.type,field.description",
    }
    if expirationDate:
        params["expirationDate"] = expirationDate
    if expirationType:
        params["expirationType"] = expirationType
    query = urlencode(params)
    url = base_url + "?" + query
    return url


def married_puts(
    baseSymbol: str = "AAPL",
    orderBy: str = "strikePrice",
    orderDir: str = "asc",
    expirationDate=None,
    expirationType=None,
    page: int = 1,
    limit: int = 100,
    raw: int = 1,
) -> str:
    """URL builder for married_puts"""
    base_url = (
        "https://www.barchart.com/proxies/core-api/v1/options/married-put"
    )
    params = {
        "baseSymbol": baseSymbol,
        "orderBy": orderBy,
        "orderDir": orderDir,
        "page": page,
        "limit": limit,
        "raw": raw,
        "fields": "baseSymbol,baseSymbolType,symbol,underlyingLastPrice,expirationDate,daysToExpiration,strike,strikePrice,moneyness,askPrice,breakEvenAsk,breakEvenPercentAsk,maxRisk,downside,volume,openInterest,impliedVolatilityRank1y,overallDelta,breakEvenProbability,tradeTime,symbolCode,symbolType,expirationType,daysToExpiration,impliedVolatilityRank1y,baseNextEarningsDate,timeCode,dividendExDate,historicVolatility30d,baseTrendSpotterSignal,baseTrendSpotterStrength,averageVolatility",
        "meta": "expirations,field.shortName,field.type,field.description",
    }
    if expirationDate:
        params["expirationDate"] = expirationDate
    if expirationType:
        params["expirationType"] = expirationType

    query = urlencode(params)
    url = base_url + "?" + query
    return url
