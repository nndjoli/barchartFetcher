# Long Call Fields
LONG_CALL_FIELDS = (
    "underlyingLastPrice,expirationDate,daysToExpiration,strike,moneyness,"
    "symbol,baseSymbol,askPrice,timePremiumAskPercent,breakEvenAsk,"
    "percentToBreakEvenAsk,netDebit,daysToExpiration,volume,openInterest,"
    "impliedVolatilityRank1y,delta,breakEvenProbability,tradeTime,"
    "otmProbability,averageVolatility,baseNextEarningsDate,timeCode,"
    "dividendExDate,historicVolatility30d,baseTrendSpotterSignal,"
    "baseTrendSpotterStrength,symbolCode,symbolType"
)

# Long Put Fields:
LONG_PUT_FIELDS = (
    "underlyingLastPrice,expirationDate,daysToExpiration,strike,moneyness,"
    "symbol,baseSymbol,askPrice,timePremiumAskPercent,breakEvenAsk,"
    "percentToBreakEvenAsk,netDebit,daysToExpiration,volume,openInterest,"
    "impliedVolatilityRank1y,delta,breakEvenProbability,tradeTime,"
    "otmProbability,averageVolatility,baseNextEarningsDate,timeCode,"
    "dividendExDate,historicVolatility30d,baseTrendSpotterSignal,"
    "baseTrendSpotterStrength,symbolCode,symbolType"
)


class LongCallPutFields:
    def __init__(self):
        self.long_call_fields = {
            "endpoint": "options",
            "symbol_param": "baseSymbol",
            "fields": LONG_CALL_FIELDS,
            "orderBy": "strikePrice",
            "orderDir": "desc",
            "expirationDate": "Example: 2025-06-27",
            "meta": "expirations,field.shortName,field.type,field.description",
            "ge(tradeTime,previousTradingDay)": "",
            "between(delta,0.2,0.9)": "",
            "eq(symbolType,call)": "",
            "expirationType": "weekly",
            "page": 1,
            "limit": 100,
            "raw": 1,
        }

        self.long_put_fields = {
            "endpoint": "options",
            "symbol_param": "baseSymbol",
            "fields": LONG_PUT_FIELDS,
            "orderBy": "strikePrice",
            "orderDir": "desc",
            "expirationDate": "Example: 2025-06-27",
            "meta": "expirations,field.shortName,field.type,field.description",
            "ge(tradeTime,previousTradingDay)": "",
            "between(delta,-0.9,-0.2)": "",
            "eq(symbolType,put)": "",
            "expirationType": "weekly",
            "page": 1,
            "limit": 100,
            "raw": 1,
        }
