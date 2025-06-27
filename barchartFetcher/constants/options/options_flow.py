# Options Flow Fields
OPTIONS_FLOW_FIELDS = (
    "symbol,baseSymbol,lastPrice,symbolType,strikePrice,expiration,dte,bidXSize,"
    "askXSize,tradePrice,tradeSize,side,premium,volume,openInterest,volatility,"
    "delta,tradeCondition,label,tradeTime.format(H:i:s \\E\\T),expirationType,"
    "askPrice,bidPrice,baseSymbolType,symbolCode"
)

# Bullish/ Bearish Sentiment Fields
BULLISH_BEARISH_SENTIMENT_FIELDS = (
    "symbolType,sentiment,premium,tradeSize,delta,symbolCode"
)


class OptionsFlowFields:
    def __init__(self):
        self.options_flow_fields = {
            "endpoint": "options_flow",
            "symbol_param": "symbol",
            "fields": OPTIONS_FLOW_FIELDS,
            "orderBy": "premium",
            "orderDir": "desc",
            "limit": 3,
            "gt(tradeSize,10)": "",
            "meta": "field.shortName,field.description,field.type",
            "raw": 1,
        }

        self.bullish_bearish_sentiment_fields = {
            "endpoint": "options_flow",
            "symbol_param": "symbol",
            "fields": BULLISH_BEARISH_SENTIMENT_FIELDS,
            "in(sentiment,(Bearish,Bullish))": "",
            "raw": 1,
            "meta": "field.shortName,field.description,field.type",
        }
