# Module: earnings_estimates
from urllib.parse import urlencode


def earnings_estimates(symbols: str = "AAPL", raw: int = 1) -> str:
    """URL builder for earnings_estimates"""
    base_url = "https://www.barchart.com/proxies/core-api/v1/quotes/get"
    params = {
        "symbols": symbols,
        "raw": raw,
        "fields": "estimatedEarnings,estimatedEarnings1qAgo,highTargetEstimate,meanTargetEstimate,lowTargetEstimate,estimatedEarnings2qAgo,estimatedEarnings3qAgo,estimatedEarnings4qAgo,reportedEarnings1qAgo,reportedEarnings2qAgo,reportedEarnings3qAgo,reportedEarnings4qAgo,earningsDifference1qAgo,earningsDifference2qAgo,earningsDifference3qAgo,earningsDifference4qAgo,earningsSurprise1qAgo,earningsSurprise2qAgo,earningsSurprise3qAgo,earningsSurprise4qAgo",
        "meta": "field.shortName,field.type,field.description",
    }
    query = urlencode(params)
    return base_url + "?" + query
