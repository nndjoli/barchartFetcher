# Module: options_flow
from urllib.parse import urlencode
import re

def bullish_bearish_sentiment(symbol: str = 'AAPL', in_sentiment_Bearish_Bullish: str = '', raw: str = '1') -> str:
    """URL builder for bullish_bearish_sentiment"""
    base_url = 'https://www.barchart.com/proxies/core-api/v1/options/flow'
    params = {
        'symbol': symbol,
        'in(sentiment,(Bearish,Bullish))': in_sentiment_Bearish_Bullish,
        'raw': raw,
        'fields': 'symbolType,sentiment,premium,tradeSize,delta,symbolCode',
        'meta': 'field.shortName,field.description,field.type',
    }
    query = urlencode(params)
    return base_url + '?' + query

def options_flow(symbol: str = 'AAPL', orderBy: str = 'premium', orderDir: str = 'desc', limit: str = '3', gt_tradeSize_10: str = '', raw: str = '1') -> str:
    """URL builder for options_flow"""
    base_url = 'https://www.barchart.com/proxies/core-api/v1/options/flow'
    params = {
        'symbol': symbol,
        'orderBy': orderBy,
        'orderDir': orderDir,
        'limit': limit,
        'gt(tradeSize,10)': gt_tradeSize_10,
        'raw': raw,
        'fields': 'symbol,baseSymbol,lastPrice,symbolType,strikePrice,expiration,dte,bidXSize,askXSize,tradePrice,tradeSize,side,premium,volume,openInterest,volatility,delta,tradeCondition,label,tradeTime.format(H:i:s \E\T),expirationType,askPrice,bidPrice,baseSymbolType,symbolCode',
        'meta': 'field.shortName,field.description,field.type',
    }
    query = urlencode(params)
    return base_url + '?' + query
