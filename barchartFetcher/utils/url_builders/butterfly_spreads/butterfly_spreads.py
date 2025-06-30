# Module: butterfly_spreads
from urllib.parse import urlencode


def long_call_butterfly(
    baseSymbol: str = "AAPL",
    orderBy: str = "breakEvenProbability",
    orderDir: str = "desc",
    expirationDate=None,
    expirationType=None,
    page: int = 1,
    limit: int = 100,
    raw: int = 1,
) -> str:
    """URL builder for long_call_butterfly"""
    base_url = "https://www.barchart.com/proxies/core-api/v1/options/long-call-butterfly-spread"
    params = {
        "baseSymbol": baseSymbol,
        "orderBy": orderBy,
        "orderDir": orderDir,
        "page": page,
        "limit": limit,
        "raw": raw,
        "fields": "baseSymbol,underlyingLastPrice,expirationDate,daysToExpiration,strikeLeg1,askPriceLeg1,strikeLeg2,bidPriceLeg2,strikeLeg3,askPriceLeg3,upperBreakEven,upperBreakEvenPercent,lowerBreakEven,lowerBreakEvenPercent,maxProfit,maxLoss,riskRewardRatio,breakEven,breakEvenProbability,baseNextEarningsDate,timeCode,dividendExDate,historicVolatility30d,impliedVolatilityRank1y,averageVolatility,baseTrendSpotterSignal,baseTrendSpotterStrength,symbolCode,symbolType",
        "meta": "expirations,field.shortName,field.type,field.description",
    }
    if expirationDate is not None:
        params["expirationDate"] = expirationDate
    if expirationType is not None:
        params["expirationType"] = expirationType

    query = urlencode(params)
    url = base_url + "?" + query
    return url


def long_iron_butterfly(
    baseSymbol: str = "AAPL",
    orderBy: str = "breakEvenProbability",
    orderDir: str = "desc",
    expirationDate=None,
    expirationType=None,
    page: int = 1,
    limit: int = 100,
    raw: int = 1,
) -> str:
    """URL builder for long_iron_butterfly"""
    base_url = "https://www.barchart.com/proxies/core-api/v1/options/long-iron-butterfly-spread"
    params = {
        "baseSymbol": baseSymbol,
        "orderBy": orderBy,
        "orderDir": orderDir,
        "page": page,
        "limit": limit,
        "raw": raw,
        "fields": "baseSymbol,underlyingLastPrice,expirationDate,daysToExpiration,strikeLeg1,bidPriceLeg1,strikeLeg2,askPriceLeg2,strikeLeg3,askPriceLeg3,strikeLeg4,bidPriceLeg4,upperBreakEven,upperBreakEvenPercent,lowerBreakEven,lowerBreakEvenPercent,maxProfit,maxLoss,riskRewardRatio,breakEvenProbability,baseNextEarningsDate,timeCode,dividendExDate,historicVolatility30d,impliedVolatilityRank1y,averageVolatility,baseTrendSpotterSignal,baseTrendSpotterStrength,symbolCode,symbolType",
        "meta": "expirations,field.shortName,field.type,field.description",
    }
    if expirationDate is not None:
        params["expirationDate"] = expirationDate
    if expirationType is not None:
        params["expirationType"] = expirationType
    query = urlencode(params)
    url = base_url + "?" + query
    return url


def long_put_butterfly(
    baseSymbol: str = "AAPL",
    orderBy: str = "breakEvenProbability",
    orderDir: str = "desc",
    expirationDate=None,
    expirationType=None,
    page: int = 1,
    limit: int = 100,
    raw: int = 1,
) -> str:
    """URL builder for long_put_butterfly"""
    base_url = "https://www.barchart.com/proxies/core-api/v1/options/long-put-butterfly-spread"
    params = {
        "baseSymbol": baseSymbol,
        "orderBy": orderBy,
        "orderDir": orderDir,
        "page": page,
        "limit": limit,
        "raw": raw,
        "fields": "baseSymbol,underlyingLastPrice,expirationDate,daysToExpiration,strikeLeg1,askPriceLeg1,strikeLeg2,bidPriceLeg2,strikeLeg3,askPriceLeg3,upperBreakEven,upperBreakEvenPercent,lowerBreakEven,lowerBreakEvenPercent,maxProfit,maxLoss,riskRewardRatio,breakEven,breakEvenProbability,baseNextEarningsDate,timeCode,dividendExDate,historicVolatility30d,impliedVolatilityRank1y,averageVolatility,baseTrendSpotterSignal,baseTrendSpotterStrength,symbolCode,symbolType",
        "meta": "expirations,field.shortName,field.type,field.description",
    }
    if expirationDate is not None:
        params["expirationDate"] = expirationDate
    if expirationType is not None:
        params["expirationType"] = expirationType

    query = urlencode(params)
    url = base_url + "?" + query
    return url


def short_call_butterfly(
    baseSymbol: str = "AAPL",
    orderBy: str = "lossProbability",
    orderDir: str = "asc",
    expirationDate=None,
    expirationType=None,
    page: int = 1,
    limit: int = 100,
    raw: int = 1,
) -> str:
    """URL builder for short_call_butterfly"""
    base_url = "https://www.barchart.com/proxies/core-api/v1/options/short-call-butterfly-spread"
    params = {
        "baseSymbol": baseSymbol,
        "orderBy": orderBy,
        "orderDir": orderDir,
        "page": page,
        "limit": limit,
        "raw": raw,
        "fields": "baseSymbol,underlyingLastPrice,expirationDate,daysToExpiration,strikeLeg1,bidPriceLeg1,strikeLeg2,askPriceLeg2,strikeLeg3,bidPriceLeg3,upperBreakEven,upperBreakEvenPercent,lowerBreakEven,lowerBreakEvenPercent,maxProfit,maxLoss,riskRewardRatio,breakEven,lossProbability,baseNextEarningsDate,timeCode,dividendExDate,historicVolatility30d,impliedVolatilityRank1y,averageVolatility,baseTrendSpotterSignal,baseTrendSpotterStrength,symbolCode,symbolType",
        "meta": "expirations,field.shortName,field.type,field.description",
    }
    if expirationDate is not None:
        params["expirationDate"] = expirationDate
    if expirationType is not None:
        params["expirationType"] = expirationType

    query = urlencode(params)
    url = base_url + "?" + query
    return url


def short_iron_butterfly(
    baseSymbol: str = "AAPL",
    orderBy: str = "lossProbability",
    orderDir: str = "asc",
    expirationDate=None,
    expirationType=None,
    page: int = 1,
    limit: int = 100,
    raw: int = 1,
) -> str:
    """URL builder for short_iron_butterfly"""
    base_url = "https://www.barchart.com/proxies/core-api/v1/options/short-iron-butterfly-spread"
    params = {
        "baseSymbol": baseSymbol,
        "orderBy": orderBy,
        "orderDir": orderDir,
        "page": page,
        "limit": limit,
        "raw": raw,
        "fields": "baseSymbol,underlyingLastPrice,expirationDate,daysToExpiration,strikeLeg1,askPriceLeg1,strikeLeg2,bidPriceLeg2,strikeLeg3,bidPriceLeg3,strikeLeg4,askPriceLeg4,upperBreakEven,upperBreakEvenPercent,lowerBreakEven,lowerBreakEvenPercent,maxProfit,maxLoss,riskRewardRatio,breakEven,lossProbability,baseNextEarningsDate,timeCode,dividendExDate,historicVolatility30d,impliedVolatilityRank1y,averageVolatility,baseTrendSpotterSignal,baseTrendSpotterStrength,symbolCode,symbolType",
        "meta": "expirations,field.shortName,field.type,field.description",
    }
    if expirationDate is not None:
        params["expirationDate"] = expirationDate
    if expirationType is not None:
        params["expirationType"] = expirationType

    query = urlencode(params)
    url = base_url + "?" + query
    return url


def short_put_butterfly(
    baseSymbol: str = "AAPL",
    orderBy: str = "lossProbability",
    orderDir: str = "asc",
    expirationDate=None,
    expirationType=None,
    page: int = 1,
    limit: int = 100,
    raw: int = 1,
) -> str:
    """URL builder for short_put_butterfly"""
    base_url = "https://www.barchart.com/proxies/core-api/v1/options/short-put-butterfly-spread"
    params = {
        "baseSymbol": baseSymbol,
        "orderBy": orderBy,
        "orderDir": orderDir,
        "page": page,
        "limit": limit,
        "raw": raw,
        "fields": "baseSymbol,underlyingLastPrice,expirationDate,daysToExpiration,strikeLeg1,bidPriceLeg1,strikeLeg2,askPriceLeg2,strikeLeg3,bidPriceLeg3,upperBreakEven,upperBreakEvenPercent,lowerBreakEven,lowerBreakEvenPercent,maxProfit,maxLoss,riskRewardRatio,breakEven,lossProbability,baseNextEarningsDate,timeCode,dividendExDate,historicVolatility30d,impliedVolatilityRank1y,averageVolatility,baseTrendSpotterSignal,baseTrendSpotterStrength,symbolCode,symbolType",
        "meta": "expirations,field.shortName,field.type,field.description",
    }
    if expirationDate is not None:
        params["expirationDate"] = expirationDate
    if expirationType is not None:
        params["expirationType"] = expirationType

    query = urlencode(params)
    url = base_url + "?" + query
    return url
