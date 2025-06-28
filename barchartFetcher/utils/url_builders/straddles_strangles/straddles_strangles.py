# Module: straddles_strangles
from urllib.parse import urlencode


def long_straddle(
    baseSymbol: str = "AAPL",
    orderBy: str = "strikeLeg1",
    orderDir: str = "asc",
    expirationDate: str = "<expiration_date>",
    expirationType: str = "weekly",
    page: str = "1",
    limit: str = "100",
    raw: str = "1",
) -> str:
    """URL builder for long_straddle"""
    base_url = "https://www.barchart.com/proxies/core-api/v1/options/long-straddle-spread"
    params = {
        "baseSymbol": baseSymbol,
        "orderBy": orderBy,
        "orderDir": orderDir,
        "expirationDate": expirationDate,
        "expirationType": expirationType,
        "page": page,
        "limit": limit,
        "raw": raw,
        "fields": "underlyingLastPrice,expirationDate,daysToExpiration,strikeLeg1,askPriceLeg1,strikeLeg2,askPriceLeg2,upperBreakEven,upperBreakEvenPercent,lowerBreakEven,lowerBreakEvenPercent,netCredit,netDebit,percentOfStock,impliedVolatilityRank1y,intradayVs30dHistoricIV,netDelta,breakEvenProbability,baseNextEarningsDate,timeCode,dividendExDate,historicVolatility30d,baseTrendSpotterSignal,baseTrendSpotterStrength,averageVolatility,symbolCode,symbolType",
        "meta": "expirations,field.shortName,field.type,field.description",
    }
    query = urlencode(params)
    return base_url + "?" + query


def long_strangle(
    baseSymbol: str = "AAPL",
    orderBy: str = "strikeLeg1",
    orderDir: str = "asc",
    expirationDate: str = "<expiration_date>",
    expirationType: str = "weekly",
    page: str = "1",
    limit: str = "100",
    raw: str = "1",
) -> str:
    """URL builder for long_strangle"""
    base_url = "https://www.barchart.com/proxies/core-api/v1/options/long-strangle-spread"
    params = {
        "baseSymbol": baseSymbol,
        "orderBy": orderBy,
        "orderDir": orderDir,
        "expirationDate": expirationDate,
        "expirationType": expirationType,
        "page": page,
        "limit": limit,
        "raw": raw,
        "fields": "underlyingLastPrice,expirationDate,daysToExpiration,strikeLeg1,askPriceLeg1,strikeLeg2,askPriceLeg2,upperBreakEven,upperBreakEvenPercent,lowerBreakEven,lowerBreakEvenPercent,netCredit,netDebit,percentOfStock,impliedVolatilityRank1y,intradayVs30dHistoricIV,netDelta,breakEvenProbability,baseNextEarningsDate,timeCode,dividendExDate,historicVolatility30d,baseTrendSpotterSignal,baseTrendSpotterStrength,averageVolatility,symbolCode,symbolType",
        "meta": "expirations,field.shortName,field.type,field.description",
    }
    query = urlencode(params)
    return base_url + "?" + query


def short_straddle(
    baseSymbol: str = "AAPL",
    orderBy: str = "strikeLeg1",
    orderDir: str = "asc",
    expirationDate: str = "<expiration_date>",
    expirationType: str = "weekly",
    page: str = "1",
    limit: str = "100",
    raw: str = "1",
) -> str:
    """URL builder for short_straddle"""
    base_url = "https://www.barchart.com/proxies/core-api/v1/options/short-straddle-spread"
    params = {
        "baseSymbol": baseSymbol,
        "orderBy": orderBy,
        "orderDir": orderDir,
        "expirationDate": expirationDate,
        "expirationType": expirationType,
        "page": page,
        "limit": limit,
        "raw": raw,
        "fields": "underlyingLastPrice,expirationDate,daysToExpiration,strikeLeg1,bidPriceLeg1,strikeLeg2,bidPriceLeg2,upperBreakEven,upperBreakEvenPercent,lowerBreakEven,lowerBreakEvenPercent,netCredit,netDebit,percentOfStock,impliedVolatilityRank1y,intradayVs30dHistoricIV,netDelta,lossProbability,baseNextEarningsDate,timeCode,dividendExDate,historicVolatility30d,baseTrendSpotterSignal,baseTrendSpotterStrength,averageVolatility,symbolCode,symbolType",
        "meta": "expirations,field.shortName,field.type,field.description",
    }
    query = urlencode(params)
    return base_url + "?" + query


def short_strangle(
    baseSymbol: str = "AAPL",
    orderBy: str = "strikeLeg1",
    orderDir: str = "asc",
    expirationDate: str = "<expiration_date>",
    expirationType: str = "weekly",
    page: str = "1",
    limit: str = "100",
    raw: str = "1",
) -> str:
    """URL builder for short_strangle"""
    base_url = "https://www.barchart.com/proxies/core-api/v1/options/short-strangle-spread"
    params = {
        "baseSymbol": baseSymbol,
        "orderBy": orderBy,
        "orderDir": orderDir,
        "expirationDate": expirationDate,
        "expirationType": expirationType,
        "page": page,
        "limit": limit,
        "raw": raw,
        "fields": "underlyingLastPrice,expirationDate,daysToExpiration,strikeLeg1,bidPriceLeg1,strikeLeg2,bidPriceLeg2,upperBreakEven,upperBreakEvenPercent,lowerBreakEven,lowerBreakEvenPercent,netCredit,netDebit,percentOfStock,impliedVolatilityRank1y,intradayVs30dHistoricIV,netDelta,lossProbability,maxProfitProbability,baseNextEarningsDate,timeCode,dividendExDate,historicVolatility30d,baseTrendSpotterSignal,baseTrendSpotterStrength,averageVolatility,symbolCode,symbolType",
        "meta": "expirations,field.shortName,field.type,field.description",
    }
    query = urlencode(params)
    return base_url + "?" + query
