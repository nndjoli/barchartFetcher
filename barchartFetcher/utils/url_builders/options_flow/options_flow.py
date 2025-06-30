# Module: options_flow
from urllib.parse import urlencode


def bullish_bearish_sentiment(
    symbol: str = "AAPL",
    raw: int = 1,
) -> str:
    """URL builder for bullish_bearish_sentiment"""
    base_url = "https://www.barchart.com/proxies/core-api/v1/options/flow"
    params = {
        "symbol": symbol,
        "in(sentiment,(Bearish,Bullish))": "",
        "raw": raw,
        "fields": "symbol,symbolType,sentiment,premium,tradeSize,delta,symbolCode",
        "meta": "field.shortName,field.description,field.type",
    }
    query = urlencode(params)
    url = base_url + "?" + query
    return url


def options_flow(
    symbol: str = "AAPL",
    orderBy: str = "premium",
    orderDir: str = "desc",
    limit: int = 3,
    min_trade_size: int = 10,
    raw: int = 1,
) -> str:
    """URL builder for options_flow"""
    base_url = "https://www.barchart.com/proxies/core-api/v1/options/flow"
    params = {
        "symbol": symbol,
        "orderBy": orderBy,
        "orderDir": orderDir,
        "limit": limit,
        f"gt(tradeSize,{min_trade_size})": "",
        "raw": raw,
        "fields": "symbol,baseSymbol,lastPrice,symbolType,strikePrice,expiration,dte,bidXSize,askXSize,tradePrice,tradeSize,side,premium,volume,openInterest,volatility,delta,tradeCondition,label,tradeTime.format(H:i:s \E\T),expirationType,askPrice,bidPrice,baseSymbolType,symbolCode",
        "meta": "field.shortName,field.description,field.type",
    }
    query = urlencode(params)
    url = base_url + "?" + query
    return url
