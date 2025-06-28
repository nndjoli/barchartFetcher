# Module: max_pain_vol_skew
from urllib.parse import urlencode


def max_pain_vol_skew(
    symbols: str = "AAPL",
    raw: int = 1,
    expirations=None,
    groupBy: str = "expirationDate",
    max_strike_spot_distance: int = 40,
) -> str:
    """URL builder for max_pain_vol_skew"""
    base_url = "https://www.barchart.com/proxies/core-api/v1/options/get"
    params = {
        "symbols": symbols,
        "raw": raw,
        "groupBy": groupBy,
        f"le(nearestToLast,{max_strike_spot_distance})": "",
        "fields": "symbol,strikePrice,optionType,baseLastPrice,openInterest,volume,volatility,daysToExpiration,expirationDate,tradeTime.format(m/d/y)",
    }
    if expirations:
        params["expirations"] = expirations
    query = urlencode(params)
    return base_url + "?" + query
