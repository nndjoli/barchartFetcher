# Module: covered_calls
from urllib.parse import urlencode


def covered_calls(
    baseSymbol: str = "AAPL",
    delta_low: int | float = 0.1,
    delta_high: int | float = 0.6,
    expirationDate=None,
    expirationType=None,
    orderBy: str = "strike",
    orderDir: str = "desc",
    page: int = 1,
    raw: int = 1,
) -> str:
    """URL builder for covered_calls"""
    base_url = (
        "https://www.barchart.com/proxies/core-api/v1/options/covered-calls"
    )
    params = {
        f"between(delta,{delta_low},{delta_high})": f"{delta_low},{delta_high}",
        "baseSymbol": baseSymbol,
        "orderBy": orderBy,
        "orderDir": orderDir,
        "expirationDate": expirationDate,
        "ge(tradeTime,previousTradingDay)": "",
        "expirationType": expirationType,
        "page": page,
        "raw": raw,
        "fields": "symbol,baseSymbol,underlyingLastPrice,expirationDate,daysToExpiration,strike,moneyness,bidPrice,breakEvenBid,percentToBreakEvenBid,volume,openInterest,impliedVolatilityRank1y,delta,flat,flatAnnual,potentialReturn,breakEvenProbability,tradeTime,averageVolatility,baseNextEarningsDate,timeCode,dividendExDate,historicVolatility30d,impliedVolatilityRank1y,baseTrendSpotterSignal,baseTrendSpotterStrength,symbolCode,symbolType",
        "meta": "expirations,field.shortName,field.type,field.description",
    }
    query = urlencode(params)
    url = base_url + "?" + query
    return url
