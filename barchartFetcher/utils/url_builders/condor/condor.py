# Module: condor
from urllib.parse import urlencode


def long_call_condor(
    baseSymbol: str = "AAPL",
    orderBy: str = "breakEvenProbability",
    orderDir: str = "desc",
    expirationDate: str = "<expiration_date>",
    expirationType: str = "weekly",
    page: str = "1",
    limit: str = "100",
    raw: str = "1",
) -> str:
    """URL builder for long_call_condor"""
    base_url = "https://www.barchart.com/proxies/core-api/v1/options/long-call-condors"
    params = {
        "baseSymbol": baseSymbol,
        "orderBy": orderBy,
        "orderDir": orderDir,
        "expirationDate": expirationDate,
        "expirationType": expirationType,
        "page": page,
        "limit": limit,
        "raw": raw,
        "fields": "underlyingLastPrice,expirationDate,daysToExpiration,strikeLeg1,askPriceLeg1,strikeLeg2,bidPriceLeg2,strikeLeg3,bidPriceLeg3,strikeLeg4,askPriceLeg4,upperBreakEven,upperBreakEvenPercent,lowerBreakEven,lowerBreakEvenPercent,maxProfit,maxLoss,riskRewardRatio,impliedVolatilityRank1y,breakEvenProbability,baseNextEarningsDate,timeCode,dividendExDate,historicVolatility30d,averageVolatility,baseTrendSpotterSignal,baseTrendSpotterStrength,symbolCode,symbolType",
        "meta": "expirations,field.shortName,field.type,field.description",
    }
    query = urlencode(params)
    return base_url + "?" + query


def long_iron_condor(
    baseSymbol: str = "AAPL",
    orderBy: str = "breakEvenProbability",
    orderDir: str = "desc",
    expirationDate: str = "<expiration_date>",
    expirationType: str = "weekly",
    page: str = "1",
    limit: str = "100",
    raw: str = "1",
) -> str:
    """URL builder for long_iron_condor"""
    base_url = (
        "https://www.barchart.com/proxies/core-api/v1/options/long-condors"
    )
    params = {
        "baseSymbol": baseSymbol,
        "orderBy": orderBy,
        "orderDir": orderDir,
        "expirationDate": expirationDate,
        "expirationType": expirationType,
        "page": page,
        "limit": limit,
        "raw": raw,
        "fields": "underlyingLastPrice,expirationDate,daysToExpiration,strikeLeg1,bidPriceLeg1,strikeLeg2,askPriceLeg2,strikeLeg3,askPriceLeg3,strikeLeg4,bidPriceLeg4,upperBreakEven,upperBreakEvenPercent,lowerBreakEven,lowerBreakEvenPercent,maxProfit,maxLoss,riskRewardRatio,impliedVolatilityRank1y,breakEvenProbability,baseNextEarningsDate,timeCode,dividendExDate,historicVolatility30d,averageVolatility,baseTrendSpotterSignal,baseTrendSpotterStrength,symbolCode,symbolType",
        "meta": "expirations,field.shortName,field.type,field.description",
    }
    query = urlencode(params)
    return base_url + "?" + query


def long_put_condor(
    baseSymbol: str = "AAPL",
    orderBy: str = "breakEvenProbability",
    orderDir: str = "desc",
    expirationDate: str = "<expiration_date>",
    expirationType: str = "weekly",
    page: str = "1",
    limit: str = "100",
    raw: str = "1",
) -> str:
    """URL builder for long_put_condor"""
    base_url = (
        "https://www.barchart.com/proxies/core-api/v1/options/long-put-condors"
    )
    params = {
        "baseSymbol": baseSymbol,
        "orderBy": orderBy,
        "orderDir": orderDir,
        "expirationDate": expirationDate,
        "expirationType": expirationType,
        "page": page,
        "limit": limit,
        "raw": raw,
        "fields": "underlyingLastPrice,expirationDate,daysToExpiration,strikeLeg1,askPriceLeg1,strikeLeg2,bidPriceLeg2,strikeLeg3,bidPriceLeg3,strikeLeg4,askPriceLeg4,upperBreakEven,upperBreakEvenPercent,lowerBreakEven,lowerBreakEvenPercent,maxProfit,maxLoss,riskRewardRatio,impliedVolatilityRank1y,breakEvenProbability,baseNextEarningsDate,timeCode,dividendExDate,historicVolatility30d,averageVolatility,baseTrendSpotterSignal,baseTrendSpotterStrength,symbolCode,symbolType",
        "meta": "expirations,field.shortName,field.type,field.description",
    }
    query = urlencode(params)
    return base_url + "?" + query


def short_call_condor(
    baseSymbol: str = "AAPL",
    orderBy: str = "lossProbability",
    orderDir: str = "asc",
    expirationDate: str = "<expiration_date>",
    expirationType: str = "weekly",
    page: str = "1",
    limit: str = "100",
    raw: str = "1",
) -> str:
    """URL builder for short_call_condor"""
    base_url = "https://www.barchart.com/proxies/core-api/v1/options/short-call-condors"
    params = {
        "baseSymbol": baseSymbol,
        "orderBy": orderBy,
        "orderDir": orderDir,
        "expirationDate": expirationDate,
        "expirationType": expirationType,
        "page": page,
        "limit": limit,
        "raw": raw,
        "fields": "underlyingLastPrice,expirationDate,daysToExpiration,strikeLeg1,bidPriceLeg1,strikeLeg2,askPriceLeg2,strikeLeg3,askPriceLeg3,strikeLeg4,bidPriceLeg4,upperBreakEven,upperBreakEvenPercent,lowerBreakEven,lowerBreakEvenPercent,maxProfit,maxLoss,riskRewardRatio,impliedVolatilityRank1y,lossProbability,baseNextEarningsDate,timeCode,dividendExDate,historicVolatility30d,averageVolatility,baseTrendSpotterSignal,baseTrendSpotterStrength,symbolCode,symbolType",
        "meta": "expirations,field.shortName,field.type,field.description",
    }
    query = urlencode(params)
    return base_url + "?" + query


def short_iron_condor(
    baseSymbol: str = "AAPL",
    orderBy: str = "lossProbability",
    orderDir: str = "asc",
    expirationDate: str = "<expiration_date>",
    expirationType: str = "weekly",
    page: str = "1",
    limit: str = "100",
    raw: str = "1",
) -> str:
    """URL builder for short_iron_condor"""
    base_url = (
        "https://www.barchart.com/proxies/core-api/v1/options/short-condors"
    )
    params = {
        "baseSymbol": baseSymbol,
        "orderBy": orderBy,
        "orderDir": orderDir,
        "expirationDate": expirationDate,
        "expirationType": expirationType,
        "page": page,
        "limit": limit,
        "raw": raw,
        "fields": "underlyingLastPrice,expirationDate,daysToExpiration,strikeLeg1,askPriceLeg1,strikeLeg2,bidPriceLeg2,strikeLeg3,bidPriceLeg3,strikeLeg4,askPriceLeg4,upperBreakEven,upperBreakEvenPercent,lowerBreakEven,lowerBreakEvenPercent,maxProfit,maxLoss,riskRewardRatio,impliedVolatilityRank1y,lossProbability,baseNextEarningsDate,timeCode,dividendExDate,historicVolatility30d,averageVolatility,baseTrendSpotterSignal,baseTrendSpotterStrength,symbolCode,symbolType",
        "meta": "expirations,field.shortName,field.type,field.description",
    }
    query = urlencode(params)
    return base_url + "?" + query


def short_put_condor(
    baseSymbol: str = "AAPL",
    orderBy: str = "lossProbability",
    orderDir: str = "asc",
    expirationDate: str = "<expiration_date>",
    expirationType: str = "weekly",
    page: str = "1",
    limit: str = "100",
    raw: str = "1",
) -> str:
    """URL builder for short_put_condor"""
    base_url = "https://www.barchart.com/proxies/core-api/v1/options/short-put-condors"
    params = {
        "baseSymbol": baseSymbol,
        "orderBy": orderBy,
        "orderDir": orderDir,
        "expirationDate": expirationDate,
        "expirationType": expirationType,
        "page": page,
        "limit": limit,
        "raw": raw,
        "fields": "underlyingLastPrice,expirationDate,daysToExpiration,strikeLeg1,bidPriceLeg1,strikeLeg2,askPriceLeg2,strikeLeg3,askPriceLeg3,strikeLeg4,bidPriceLeg4,upperBreakEven,upperBreakEvenPercent,lowerBreakEven,lowerBreakEvenPercent,maxProfit,maxLoss,riskRewardRatio,impliedVolatilityRank1y,lossProbability,baseNextEarningsDate,timeCode,dividendExDate,historicVolatility30d,averageVolatility,baseTrendSpotterSignal,baseTrendSpotterStrength,symbolCode,symbolType",
        "meta": "expirations,field.shortName,field.type,field.description",
    }
    query = urlencode(params)
    return base_url + "?" + query
