# Module: naked_puts
from urllib.parse import urlencode


def naked_puts(
    delta_low: str = "-0.6",
    delta_high: str = "-0.1",
    baseSymbol: str = "AAPL",
    orderBy: str = "strike",
    orderDir: str = "asc",
    expirationDate: str = "<expiration_date>",
    expirationType: str = "weekly",
    page: str = "1",
    raw: str = "1",
) -> str:
    """URL builder for naked_puts"""
    base_url = (
        "https://www.barchart.com/proxies/core-api/v1/options/naked-puts"
    )
    params = {
        f"between(delta,{delta_low},{delta_high})": f"{delta_low},{delta_high}",
        "baseSymbol": baseSymbol,
        "orderBy": orderBy,
        "orderDir": orderDir,
        "expirationDate": expirationDate,
        "expirationType": expirationType,
        "page": page,
        "raw": raw,
        "fields": "symbol,symbolType,symbolCode,baseSymbol,underlyingLastPrice,expirationDate,daysToExpiration,strike,moneyness,bidPrice,breakEvenBid,percentToBreakEvenBid,volume,openInterest,impliedVolatilityRank1y,delta,potentialReturn,potentialReturnAnnual,breakEvenProbability,tradeTime,averageVolatility,baseNextEarningsDate,timeCode,dividendExDate,historicVolatility30d,baseTrendSpotterSignal,baseTrendSpotterStrength",
        "meta": "expirations,field.shortName,field.type,field.description",
    }
    query = urlencode(params)
    return base_url + "?" + query
