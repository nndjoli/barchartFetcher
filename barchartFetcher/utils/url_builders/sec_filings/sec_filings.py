# Module: sec_filings
from urllib.parse import urlencode


def sec_filings(
    symbol: str = "AAPL",
    transactions: int | float = 1,
    limit: int = 20,
) -> str:
    """URL builder for sec_filings"""
    base_url = "https://www.barchart.com/proxies/core-api/v1/sec-filings/get"
    params = {
        "symbol": symbol,
        "transactions": transactions,
        "limit": limit,
        "fields": "symbol,date,formName,description,htmlUrl,wordUrl,pdfUrl,excelUrl",
    }
    query = urlencode(params)
    url = base_url + "?" + query
    return url
