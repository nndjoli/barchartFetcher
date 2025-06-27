MARRIED_PUTS_FIELDS = (
    "baseSymbol,baseSymbolType,symbol,underlyingLastPrice,expirationDate,"
    "daysToExpiration,strike,strikePrice,moneyness,askPrice,breakEvenAsk,"
    "breakEvenPercentAsk,maxRisk,downside,volume,openInterest,"
    "impliedVolatilityRank1y,overallDelta,breakEvenProbability,tradeTime,"
    "symbolCode,symbolType,expirationType,daysToExpiration,"
    "impliedVolatilityRank1y,baseNextEarningsDate,timeCode,dividendExDate,"
    "historicVolatility30d,baseTrendSpotterSignal,baseTrendSpotterStrength,"
    "averageVolatility"
)

LONG_COLLAR_SPREAD_FIELDS = (
    "baseSymbol,baseSymbolType,underlyingLastPrice,expirationDate,"
    "daysToExpiration,strikeLeg1,bidPriceLeg1,strikeLeg2,askPriceLeg2,breakEven,"
    "netDebitCredit,percentOfCost,maxProfit,maxLoss,maxRisk,upside,downside,"
    "overallDelta,breakEvenProbability,symbolCode,symbolType,expirationType,"
    "legs,daysToExpiration,averageVolatility,baseNextEarningsDate,timeCode,"
    "dividendExDate,historicVolatility30d,impliedVolatilityRank1y,"
    "baseTrendSpotterSignal,baseTrendSpotterStrength"
)


class ProtectionStrategiesFields:
    def __init__(self):
        self.married_puts_fields = {
            "endpoint": "options/married-put",
            "symbol_param": "baseSymbol",
            "fields": MARRIED_PUTS_FIELDS,
            "orderBy": "strikePrice",
            "orderDir": "asc",
            "expirationDate": "Example: 2025-06-27",
            "expirationType": "weekly",
            "meta": "expirations,field.shortName,field.type,field.description",
            "page": 1,
            "limit": 100,
            "raw": 1,
        }

        self.long_collar_spread_fields = {
            "endpoint": "options/long-collar-spread",
            "symbol_param": "baseSymbol",
            "fields": LONG_COLLAR_SPREAD_FIELDS,
            "orderBy": "strikeLeg1",
            "orderDir": "asc",
            "expirationDate": "Example: 2025-06-27",
            "expirationType": "weekly",
            "meta": "expirations,field.shortName,field.type,field.description",
            "page": 1,
            "limit": 100,
            "raw": 1,
        }
