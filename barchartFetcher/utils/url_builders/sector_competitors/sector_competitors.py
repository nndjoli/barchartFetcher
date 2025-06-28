# Module: sector_competitors
from urllib.parse import urlencode
import re

def sector_competitors(symbol: str = 'AAPL', lists: str = 'stocks.inSector.all(<sector_symbol_from_key_statistics>)', orderBy: str = 'weightedAlpha', orderDir: str = 'desc', hasOptions: str = 'true', page: str = '1', limit: str = '100', raw: str = '1') -> str:
    """URL builder for sector_competitors"""
    base_url = 'https://www.barchart.com/proxies/core-api/v1/quotes/get'
    params = {
        'symbol': symbol,
        'lists': lists,
        'orderBy': orderBy,
        'orderDir': orderDir,
        'hasOptions': hasOptions,
        'page': page,
        'limit': limit,
        'raw': raw,
        'fields': 'weightedAlpha,lastPrice,priceChange,percentChange,highPrice1y,lowPrice1y,percentChange1y,tradeTime,symbolCode,symbolType,hasOptions',
        'meta': 'field.shortName,field.type,field.description,lists.lastUpdate',
    }
    query = urlencode(params)
    return base_url + '?' + query
