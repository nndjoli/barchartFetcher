LONG_STRADDLE_FIELDS = (
    "underlyingLastPrice,expirationDate,daysToExpiration,strikeLeg1,"
    "askPriceLeg1,strikeLeg2,askPriceLeg2,upperBreakEven,upperBreakEvenPercent,"
    "lowerBreakEven,lowerBreakEvenPercent,netCredit,netDebit,percentOfStock,"
    "impliedVolatilityRank1y,intradayVs30dHistoricIV,netDelta,"
    "breakEvenProbability,baseNextEarningsDate,timeCode,dividendExDate,"
    "historicVolatility30d,baseTrendSpotterSignal,baseTrendSpotterStrength,"
    "averageVolatility,symbolCode,symbolType"
)

SHORT_STRADDLE_FIELDS = (
    "underlyingLastPrice,expirationDate,daysToExpiration,strikeLeg1,"
    "bidPriceLeg1,strikeLeg2,bidPriceLeg2,upperBreakEven,upperBreakEvenPercent,"
    "lowerBreakEven,lowerBreakEvenPercent,netCredit,netDebit,percentOfStock,"
    "impliedVolatilityRank1y,intradayVs30dHistoricIV,netDelta,lossProbability,"
    "baseNextEarningsDate,timeCode,dividendExDate,historicVolatility30d,"
    "baseTrendSpotterSignal,baseTrendSpotterStrength,averageVolatility,"
    "symbolCode,symbolType"
)

LONG_STRANGLE_FIELDS = (
    "underlyingLastPrice,expirationDate,daysToExpiration,strikeLeg1,"
    "askPriceLeg1,strikeLeg2,askPriceLeg2,upperBreakEven,upperBreakEvenPercent,"
    "lowerBreakEven,lowerBreakEvenPercent,netCredit,netDebit,percentOfStock,"
    "impliedVolatilityRank1y,intradayVs30dHistoricIV,netDelta,"
    "breakEvenProbability,baseNextEarningsDate,timeCode,dividendExDate,"
    "historicVolatility30d,baseTrendSpotterSignal,baseTrendSpotterStrength,"
    "averageVolatility,symbolCode,symbolType"
)

SHORT_STRANGLE_FIELDS = (
    "underlyingLastPrice,expirationDate,daysToExpiration,strikeLeg1,"
    "bidPriceLeg1,strikeLeg2,bidPriceLeg2,upperBreakEven,upperBreakEvenPercent,"
    "lowerBreakEven,lowerBreakEvenPercent,netCredit,netDebit,percentOfStock,"
    "impliedVolatilityRank1y,intradayVs30dHistoricIV,netDelta,lossProbability,"
    "maxProfitProbability,baseNextEarningsDate,timeCode,dividendExDate,"
    "historicVolatility30d,baseTrendSpotterSignal,baseTrendSpotterStrength,"
    "averageVolatility,symbolCode,symbolType"
)


class StraddlesStranglesFields:
    def __init__(self):
        self.long_straddle_fields = {
            "endpoint": "long_straddle",
            "symbol_param": "baseSymbol",
            "fields": LONG_STRADDLE_FIELDS,
            "orderBy": "strikeLeg1",
            "orderDir": "asc",
            "expirationDate": "Example: 2025-06-27",
            "expirationType": "weekly",
            "meta": "expirations,field.shortName,field.type,field.description",
            "page": 1,
            "limit": 100,
            "raw": 1,
        }

        self.short_straddle_fields = {
            "endpoint": "short_straddle",
            "symbol_param": "baseSymbol",
            "fields": SHORT_STRADDLE_FIELDS,
            "orderBy": "strikeLeg1",
            "orderDir": "asc",
            "expirationDate": "Example: 2025-06-27",
            "expirationType": "weekly",
            "meta": "expirations,field.shortName,field.type,field.description",
            "page": 1,
            "limit": 100,
            "raw": 1,
        }

        self.long_strangle_fields = {
            "endpoint": "long_strangle",
            "symbol_param": "baseSymbol",
            "fields": LONG_STRANGLE_FIELDS,
            "orderBy": "strikeLeg1",
            "orderDir": "asc",
            "expirationDate": "Example: 2025-06-27",
            "expirationType": "weekly",
            "meta": "expirations,field.shortName,field.type,field.description",
            "page": 1,
            "limit": 100,
            "raw": 1,
        }

        self.short_strangle_fields = {
            "endpoint": "short_strangle",
            "symbol_param": "baseSymbol",
            "fields": SHORT_STRANGLE_FIELDS,
            "orderBy": "strikeLeg1",
            "orderDir": "asc",
            "expirationDate": "Example: 2025-06-27",
            "expirationType": "weekly",
            "meta": "expirations,field.shortName,field.type,field.description",
            "page": 1,
            "limit": 100,
            "raw": 1,
        }
