# Module: sec_filings
from urllib.parse import urlencode
import re

def sec_filings(symbol: str = 'AAPL', transactions: str = '1', limit: str = '20') -> str:
    """URL builder for sec_filings"""
    base_url = 'https://www.barchart.com/proxies/core-api/v1/sec-filings/get'
    params = {
        'symbol': symbol,
        'transactions': transactions,
        'limit': limit,
        'fields': 'date,formName,description,htmlUrl,wordUrl,pdfUrl,excelUrl',
    }
    query = urlencode(params)
    return base_url + '?' + query
