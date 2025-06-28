# Module: vertical_spreads
from urllib.parse import urlencode


def bear_call_spreads(
    abs_deltaLeg1_low: str = "0",
    abs_deltaLeg1_high: str = "0.6",
    abs_deltaLeg2_low: str = "",
    abs_deltaLeg2_high: str = "0.3",
    riskRewardRatio_low: str = "2",
    riskRewardRatio_high: str = "5",
    baseSymbol: str = "AAPL",
    orderBy: str = "strikeLeg1",
    orderDir: str = "desc",
    expirationDate: str = "<expiration_date>",
    expirationType: str = "weekly",
    raw: str = "1",
) -> str:
    """URL builder for bear_call_spreads"""
    base_url = "https://www.barchart.com/proxies/core-api/v1/options/bear-calls-spread"
    params = {
        f"between(abs(deltaLeg1),{abs_deltaLeg1_low},{abs_deltaLeg1_high})": f"{abs_deltaLeg1_low},{abs_deltaLeg1_high}",
        f"between(abs(deltaLeg2),{abs_deltaLeg2_low},{abs_deltaLeg2_high})": f"{abs_deltaLeg2_low},{abs_deltaLeg2_high}",
        f"between(riskRewardRatio,{riskRewardRatio_low},{riskRewardRatio_high})": f"{riskRewardRatio_low},{riskRewardRatio_high}",
        "baseSymbol": baseSymbol,
        "orderBy": orderBy,
        "orderDir": orderDir,
        "expirationDate": expirationDate,
        "expirationType": expirationType,
        "raw": raw,
        "fields": "underlyingLastPrice,expirationDate,daysToExpiration,strikeLeg1,bidPriceLeg1,strikeLeg2,askPriceLeg2,breakEven,breakEvenPercent,maxProfit,maxLoss,maxProfitPercent,riskRewardRatio,impliedVolatilityRank1y,lossProbability,time,averageVolatility,baseNextEarningsDate,timeCode,dividendExDate,historicVolatility30d,impliedVolatilityRank1y,baseTrendSpotterSignal,baseTrendSpotterStrength,symbolCode,symbolType",
        "meta": "expirations,field.shortName,field.type,field.description",
    }
    query = urlencode(params)
    return base_url + "?" + query


def bear_put_spreads(
    riskRewardRatio_low: str = "0.33",
    riskRewardRatio_high: str = "1.5",
    baseSymbol: str = "AAPL",
    orderBy: str = "strikeLeg1",
    orderDir: str = "desc",
    expirationDate: str = "<expiration_date>",
    expirationType: str = "weekly",
    between_abs_deltaLeg1_0_3: str = "",
    between_abs_deltaLeg2_0_1: str = "",
    raw: str = "1",
) -> str:
    """URL builder for bear_put_spreads"""
    base_url = (
        "https://www.barchart.com/proxies/core-api/v1/options/bear-puts-spread"
    )
    params = {
        f"between(riskRewardRatio,{riskRewardRatio_low},{riskRewardRatio_high})": f"{riskRewardRatio_low},{riskRewardRatio_high}",
        "baseSymbol": baseSymbol,
        "orderBy": orderBy,
        "orderDir": orderDir,
        "expirationDate": expirationDate,
        "expirationType": expirationType,
        "between(abs(deltaLeg1),0.3,)": between_abs_deltaLeg1_0_3,
        "between(abs(deltaLeg2),0.1,)": between_abs_deltaLeg2_0_1,
        "raw": raw,
        "fields": "underlyingLastPrice,expirationDate,daysToExpiration,strikeLeg1,askPriceLeg1,strikeLeg2,bidPriceLeg2,breakEven,breakEvenPercent,maxProfit,maxLoss,maxProfitPercent,riskRewardRatio,impliedVolatilityRank1y,breakEvenProbability,time,averageVolatility,baseNextEarningsDate,timeCode,dividendExDate,historicVolatility30d,impliedVolatilityRank1y,baseTrendSpotterSignal,baseTrendSpotterStrength,symbolCode,symbolType",
        "meta": "expirations,field.shortName,field.type,field.description",
    }
    query = urlencode(params)
    return base_url + "?" + query


def bull_call_spreads(
    riskRewardRatio_low: str = "0.33",
    riskRewardRatio_high: str = "1.5",
    baseSymbol: str = "AAPL",
    orderBy: str = "strikeLeg1",
    orderDir: str = "asc",
    expirationDate: str = "<expiration_date>",
    expirationType: str = "weekly",
    between_abs_deltaLeg1_0_3: str = "",
    between_abs_deltaLeg2_0_1: str = "",
    raw: str = "1",
) -> str:
    """URL builder for bull_call_spreads"""
    base_url = "https://www.barchart.com/proxies/core-api/v1/options/bull-calls-spread"
    params = {
        f"between(riskRewardRatio,{riskRewardRatio_low},{riskRewardRatio_high})": f"{riskRewardRatio_low},{riskRewardRatio_high}",
        "baseSymbol": baseSymbol,
        "orderBy": orderBy,
        "orderDir": orderDir,
        "expirationDate": expirationDate,
        "expirationType": expirationType,
        "between(abs(deltaLeg1),0.3,)": between_abs_deltaLeg1_0_3,
        "between(abs(deltaLeg2),0.1,)": between_abs_deltaLeg2_0_1,
        "raw": raw,
        "fields": "breakEven,breakEvenPercent,maxProfit,maxLoss,maxProfitPercent,riskRewardRatio,impliedVolatilityRank1y,breakEvenProbability,time,averageVolatility,baseNextEarningsDate,timeCode,dividendExDate,historicVolatility30d,impliedVolatilityRank1y,baseTrendSpotterSignal,baseTrendSpotterStrength,symbolCode,symbolType",
        "meta": "expirations,field.shortName,field.type,field.description",
    }
    query = urlencode(params)
    return base_url + "?" + query


def bull_put_spreads(
    abs_deltaLeg1_low: str = "",
    abs_deltaLeg1_high: str = "0.6",
    abs_deltaLeg2_low: str = "0",
    abs_deltaLeg2_high: str = "0.3",
    riskRewardRatio_low: str = "2",
    riskRewardRatio_high: str = "5",
    baseSymbol: str = "AAPL",
    orderBy: str = "strikeLeg1",
    orderDir: str = "asc",
    expirationDate: str = "<expiration_date>",
    expirationType: str = "weekly",
    raw: str = "1",
) -> str:
    """URL builder for bull_put_spreads"""
    base_url = (
        "https://www.barchart.com/proxies/core-api/v1/options/bull-puts-spread"
    )
    params = {
        f"between(abs(deltaLeg1),{abs_deltaLeg1_low},{abs_deltaLeg1_high})": f"{abs_deltaLeg1_low},{abs_deltaLeg1_high}",
        f"between(abs(deltaLeg2),{abs_deltaLeg2_low},{abs_deltaLeg2_high})": f"{abs_deltaLeg2_low},{abs_deltaLeg2_high}",
        f"between(riskRewardRatio,{riskRewardRatio_low},{riskRewardRatio_high})": f"{riskRewardRatio_low},{riskRewardRatio_high}",
        "baseSymbol": baseSymbol,
        "orderBy": orderBy,
        "orderDir": orderDir,
        "expirationDate": expirationDate,
        "expirationType": expirationType,
        "raw": raw,
        "fields": "underlyingLastPrice,expirationDate,daysToExpiration,strikeLeg1,bidPriceLeg1,strikeLeg2,askPriceLeg2,breakEven,breakEvenPercent,maxProfit,maxLoss,maxProfitPercent,riskRewardRatio,impliedVolatilityRank1y,lossProbability,time,averageVolatility,baseNextEarningsDate,timeCode,dividendExDate,historicVolatility30d,impliedVolatilityRank1y,baseTrendSpotterSignal,baseTrendSpotterStrength,symbolCode,symbolType",
        "meta": "expirations,field.shortName,field.type,field.description",
    }
    query = urlencode(params)
    return base_url + "?" + query
