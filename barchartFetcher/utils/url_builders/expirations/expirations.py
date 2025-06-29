# Module: expirations
from urllib.parse import urlencode


def expirations(symbols: str = "AAPL", raw: int = 1) -> str:
    """URL builder for expirations"""
    base_url = (
        "https://www.barchart.com/proxies/core-api/v1/options-expirations/get"
    )
    params = {
        "symbols": symbols,
        "raw": raw,
        "fields": "symbol,callVolume,putVolume,putCallVolumeRatio,callOpenInterest,putOpenInterest,putCallOpenInterestRatio,expirationDate,expirationType",
        "meta": "field.shortName,field.description,field.type",
    }
    query = urlencode(params)
    return base_url + "?" + query
