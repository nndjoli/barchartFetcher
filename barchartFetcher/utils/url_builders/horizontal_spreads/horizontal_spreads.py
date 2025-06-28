# Module: horizontal_spreads
from urllib.parse import urlencode


def long_call_calendar(
    baseSymbol: str = "AAPL",
    orderBy: str = "ivSkew",
    orderDir: str = "desc",
    expirationDate=None,
    expirationType=None,
    page: int = 1,
    limit: int = 100,
    raw: int = 1,
) -> str:
    """URL builder for long_call_calendar"""
    base_url = "https://www.barchart.com/proxies/core-api/v1/options/long-call-calendar-spread"
    params = {
        "baseSymbol": baseSymbol,
        "orderBy": orderBy,
        "orderDir": orderDir,
        "page": page,
        "limit": limit,
        "raw": raw,
        "fields": "baseSymbol,baseSymbolType,underlyingLastPrice,expirationDateLeg1,strikeLeg1,bidPriceLeg1,expirationDateLeg2,askPriceLeg2,netDebit,volatilityLeg1,volatilityLeg2,ivSkew,impliedVolatilityRank1y,intradayVs30dHistoricIV,netDelta,netVega,expirationType,averageVolatility,daysToExpiration,expirationDate,baseNextEarningsDate,timeCode,dividendExDate,historicVolatility30d,baseTrendSpotterSignal,baseTrendSpotterStrength,symbolCode,symbolType",
        "meta": "expirations,field.shortName,field.type,field.description",
    }
    if expirationDate:
        params["expirationDate"] = expirationDate
    if expirationType:
        params["expirationType"] = expirationType

    query = urlencode(params)
    return base_url + "?" + query


def long_call_diagonal(
    baseSymbol: str = "AAPL",
    orderBy: str = "ivSkewInverse",
    orderDir: str = "desc",
    expirationDate=None,
    expirationType=None,
    page: int = 1,
    limit: int = 100,
    raw: int = 1,
) -> str:
    """URL builder for long_call_diagonal"""
    base_url = "https://www.barchart.com/proxies/core-api/v1/options/bull-calls-diagonal-spread"
    params = {
        "baseSymbol": baseSymbol,
        "orderBy": orderBy,
        "orderDir": orderDir,
        "page": page,
        "limit": limit,
        "raw": raw,
        "fields": "baseSymbol,baseSymbolType,underlyingLastPrice,expirationDateLeg1,strikeLeg1,askPriceLeg1,expirationDateLeg2,strikeLeg2,bidPriceLeg2,netDebit,volatilityLeg1,volatilityLeg2,ivSkewInverse,impliedVolatilityRank1y,intradayVs30dHistoricIV,netDelta,netVega,expirationType,averageVolatility,daysToExpiration,expirationDate,baseNextEarningsDate,timeCode,dividendExDate,historicVolatility30d,baseTrendSpotterSignal,baseTrendSpotterStrength,symbolCode,symbolType",
        "meta": "expirations,field.shortName,field.type,field.description",
    }
    if expirationDate:
        params["expirationDate"] = expirationDate
    if expirationType:
        params["expirationType"] = expirationType

    query = urlencode(params)
    return base_url + "?" + query


def long_put_calendar(
    baseSymbol: str = "AAPL",
    orderBy: str = "ivSkew",
    orderDir: str = "desc",
    expirationDate=None,
    expirationType=None,
    page: int = 1,
    limit: int = 100,
    raw: int = 1,
) -> str:
    """URL builder for long_put_calendar"""
    base_url = "https://www.barchart.com/proxies/core-api/v1/options/long-put-calendar-spread"
    params = {
        "baseSymbol": baseSymbol,
        "orderBy": orderBy,
        "orderDir": orderDir,
        "eq(type,put)": "",
        "page": page,
        "limit": limit,
        "raw": raw,
        "fields": "baseSymbol,baseSymbolType,underlyingLastPrice,expirationDateLeg1,strikeLeg1,bidPriceLeg1,expirationDateLeg2,askPriceLeg2,netDebit,volatilityLeg1,volatilityLeg2,ivSkew,impliedVolatilityRank1y,intradayVs30dHistoricIV,netDelta,netVega,expirationType,averageVolatility,daysToExpiration,expirationDate,baseNextEarningsDate,timeCode,dividendExDate,historicVolatility30d,baseTrendSpotterSignal,baseTrendSpotterStrength,symbolCode,symbolType",
        "meta": "expirations,field.shortName,field.type,field.description",
    }
    if expirationDate:
        params["expirationDate"] = expirationDate
    if expirationType:
        params["expirationType"] = expirationType
    query = urlencode(params)
    return base_url + "?" + query


def long_put_diagonal(
    baseSymbol: str = "AAPL",
    orderBy: str = "ivSkew",
    orderDir: str = "desc",
    expirationDate=None,
    expirationType=None,
    page: int = 1,
    limit: int = 100,
    raw: int = 1,
) -> str:
    """URL builder for long_put_diagonal"""
    base_url = "https://www.barchart.com/proxies/core-api/v1/options/bull-puts-diagonal-spread"
    params = {
        "baseSymbol": baseSymbol,
        "orderBy": orderBy,
        "orderDir": orderDir,
        "page": page,
        "limit": limit,
        "raw": raw,
        "fields": "baseSymbol,baseSymbolType,underlyingLastPrice,expirationDateLeg1,strikeLeg1,bidPriceLeg1,expirationDateLeg2,strikeLeg2,askPriceLeg2,netDebit,volatilityLeg1,volatilityLeg2,ivSkew,impliedVolatilityRank1y,intradayVs30dHistoricIV,netDelta,netVega,expirationType,averageVolatility,daysToExpiration,expirationDate,baseNextEarningsDate,timeCode,dividendExDate,historicVolatility30d,baseTrendSpotterSignal,baseTrendSpotterStrength,symbolCode,symbolType",
        "meta": "expirations,field.shortName,field.type,field.description",
    }
    if expirationDate:
        params["expirationDate"] = expirationDate
    if expirationType:
        params["expirationType"] = expirationType
    query = urlencode(params)
    return base_url + "?" + query


def short_call_diagonal(
    baseSymbol: str = "AAPL",
    orderBy: str = "ivSkew",
    orderDir: str = "desc",
    expirationDate=None,
    expirationType=None,
    page: int = 1,
    limit: int = 100,
    raw: int = 1,
) -> str:
    """URL builder for short_call_diagonal"""
    base_url = "https://www.barchart.com/proxies/core-api/v1/options/bear-calls-diagonal-spread"
    params = {
        "baseSymbol": baseSymbol,
        "orderBy": orderBy,
        "orderDir": orderDir,
        "page": page,
        "limit": limit,
        "raw": raw,
        "fields": "baseSymbol,baseSymbolType,underlyingLastPrice,expirationDateLeg1,strikeLeg1,bidPriceLeg1,expirationDateLeg2,strikeLeg2,askPriceLeg2,netCredit,volatilityLeg1,volatilityLeg2,ivSkew,impliedVolatilityRank1y,intradayVs30dHistoricIV,netDelta,netVega,expirationType,averageVolatility,daysToExpiration,expirationDate,baseNextEarningsDate,timeCode,dividendExDate,historicVolatility30d,baseTrendSpotterSignal,baseTrendSpotterStrength,symbolCode,symbolType",
        "meta": "expirations,field.shortName,field.type,field.description",
    }
    if expirationDate:
        params["expirationDate"] = expirationDate
    if expirationType:
        params["expirationType"] = expirationType
    query = urlencode(params)

    return base_url + "?" + query


def short_put_diagonal(
    baseSymbol: str = "AAPL",
    orderBy: str = "ivSkewInverse",
    orderDir: str = "desc",
    expirationDate=None,
    expirationType=None,
    page: int = 1,
    limit: int = 100,
    raw: int = 1,
) -> str:
    """URL builder for short_put_diagonal"""
    base_url = "https://www.barchart.com/proxies/core-api/v1/options/bear-puts-diagonal-spread"
    params = {
        "baseSymbol": baseSymbol,
        "orderBy": orderBy,
        "orderDir": orderDir,
        "page": page,
        "limit": limit,
        "raw": raw,
        "fields": "baseSymbol,baseSymbolType,underlyingLastPrice,expirationDateLeg1,strikeLeg1,askPriceLeg1,expirationDateLeg2,strikeLeg2,bidPriceLeg2,netDebit,volatilityLeg1,volatilityLeg2,ivSkewInverse,impliedVolatilityRank1y,intradayVs30dHistoricIV,netDelta,netVega,expirationType,averageVolatility,daysToExpiration,expirationDate,baseNextEarningsDate,timeCode,dividendExDate,baseTrendSpotterSignal,baseTrendSpotterStrength,symbolCode,symbolType",
        "meta": "expirations,field.shortName,field.type,field.description",
    }
    if expirationDate:
        params["expirationDate"] = expirationDate
    if expirationType:
        params["expirationType"] = expirationType

    query = urlencode(params)
    return base_url + "?" + query
