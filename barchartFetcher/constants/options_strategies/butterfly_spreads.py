LONG_CALL_BUTTERFLY_FIELDS = (
    "underlyingLastPrice,expirationDate,daysToExpiration,strikeLeg1,askPriceLeg1,"
    "strikeLeg2,bidPriceLeg2,strikeLeg3,askPriceLeg3,upperBreakEven,"
    "upperBreakEvenPercent,lowerBreakEven,lowerBreakEvenPercent,maxProfit,maxLoss,"
    "riskRewardRatio,breakEven,breakEvenProbability,baseNextEarningsDate,timeCode,"
    "dividendExDate,historicVolatility30d,impliedVolatilityRank1y,averageVolatility,"
    "baseTrendSpotterSignal,baseTrendSpotterStrength,symbolCode,symbolType"
)

SHORT_CALL_BUTTERFLY_FIELDS = (
    "underlyingLastPrice,expirationDate,daysToExpiration,strikeLeg1,"
    "bidPriceLeg1,strikeLeg2,askPriceLeg2,strikeLeg3,bidPriceLeg3,"
    "upperBreakEven,upperBreakEvenPercent,lowerBreakEven,"
    "lowerBreakEvenPercent,maxProfit,maxLoss,riskRewardRatio,breakEven,"
    "lossProbability,baseNextEarningsDate,timeCode,dividendExDate,"
    "historicVolatility30d,impliedVolatilityRank1y,averageVolatility,"
    "baseTrendSpotterSignal,baseTrendSpotterStrength,symbolCode,symbolType"
)

LONG_PUT_BUTTERFLY_FIELDS = (
    "underlyingLastPrice,expirationDate,daysToExpiration,strikeLeg1,askPriceLeg1,"
    "strikeLeg2,bidPriceLeg2,strikeLeg3,askPriceLeg3,upperBreakEven,"
    "upperBreakEvenPercent,lowerBreakEven,lowerBreakEvenPercent,maxProfit,"
    "maxLoss,riskRewardRatio,breakEven,breakEvenProbability,baseNextEarningsDate,"
    "timeCode,dividendExDate,historicVolatility30d,impliedVolatilityRank1y,"
    "averageVolatility,baseTrendSpotterSignal,baseTrendSpotterStrength,symbolCode,"
    "symbolType"
)

SHORT_PUT_BUTTERFLY_FIELDS = (
    "underlyingLastPrice,expirationDate,daysToExpiration,strikeLeg1,bidPriceLeg1,"
    "strikeLeg2,askPriceLeg2,strikeLeg3,bidPriceLeg3,upperBreakEven,"
    "upperBreakEvenPercent,lowerBreakEven,lowerBreakEvenPercent,maxProfit,"
    "maxLoss,riskRewardRatio,breakEven,lossProbability,baseNextEarningsDate,"
    "timeCode,dividendExDate,historicVolatility30d,impliedVolatilityRank1y,"
    "averageVolatility,baseTrendSpotterSignal,baseTrendSpotterStrength,"
    "symbolCode,symbolType"
)

LONG_IRON_BUTTERFLY_FIELDS = (
    "underlyingLastPrice,expirationDate,daysToExpiration,strikeLeg1,bidPriceLeg1,"
    "strikeLeg2,askPriceLeg2,strikeLeg3,askPriceLeg3,strikeLeg4,bidPriceLeg4,"
    "upperBreakEven,upperBreakEvenPercent,lowerBreakEven,lowerBreakEvenPercent,"
    "maxProfit,maxLoss,riskRewardRatio,breakEvenProbability,baseNextEarningsDate,"
    "timeCode,dividendExDate,historicVolatility30d,impliedVolatilityRank1y,"
    "averageVolatility,baseTrendSpotterSignal,baseTrendSpotterStrength,symbolCode,"
    "symbolType"
)

SHORT_IRON_BUTTERFLY_FIELDS = (
    "underlyingLastPrice,expirationDate,daysToExpiration,strikeLeg1,askPriceLeg1,"
    "strikeLeg2,bidPriceLeg2,strikeLeg3,bidPriceLeg3,strikeLeg4,askPriceLeg4,"
    "upperBreakEven,upperBreakEvenPercent,lowerBreakEven,lowerBreakEvenPercent,"
    "maxProfit,maxLoss,riskRewardRatio,breakEven,lossProbability,"
    "baseNextEarningsDate,timeCode,dividendExDate,historicVolatility30d,"
    "impliedVolatilityRank1y,averageVolatility,baseTrendSpotterSignal,"
    "baseTrendSpotterStrength,symbolCode,symbolType"
)


class ButterflySpreadsFields:
    def __init__(self):
        self.long_call_butterfly_fields = {
            "endpoint": "options/long-call-butterfly-spread",
            "symbol_param": "baseSymbol",
            "fields": LONG_CALL_BUTTERFLY_FIELDS,
            "orderBy": "breakEvenProbability",
            "orderDir": "desc",
            "expirationDate": "Example: 2025-06-27",
            "expirationType": "weekly",  # or "monthly"
            "page": 1,
            "limit": 100,
            "raw": 1,
            "meta": "expirations,field.shortName,field.type,field.description",
        }
        self.short_call_butterfly_fields = {
            "endpoint": "options/short-call-butterfly-spread",
            "symbol_param": "baseSymbol",
            "fields": SHORT_CALL_BUTTERFLY_FIELDS,
            "orderBy": "lossProbability",
            "orderDir": "asc",
            "expirationDate": "Example: 2025-06-27",
            "expirationType": "weekly",  # or "monthly"
            "page": 1,
            "limit": 100,
            "raw": 1,
            "meta": "expirations,field.shortName,field.type,field.description",
        }

        self.long_put_butterfly_fields = {
            "endpoint": "options/long-put-butterfly-spread",
            "symbol_param": "baseSymbol",
            "fields": LONG_PUT_BUTTERFLY_FIELDS,
            "orderBy": "breakEvenProbability",
            "orderDir": "desc",
            "expirationDate": "Example: 2025-06-27",
            "expirationType": "weekly",  # or "monthly"
            "page": 1,
            "limit": 100,
            "raw": 1,
            "meta": "expirations,field.shortName,field.type,field.description",
        }

        self.short_put_butterfly_fields = {
            "endpoint": "options/short-put-butterfly-spread",
            "symbol_param": "baseSymbol",
            "fields": SHORT_PUT_BUTTERFLY_FIELDS,
            "orderBy": "lossProbability",
            "orderDir": "asc",
            "expirationDate": "Example: 2025-06-27",
            "expirationType": "weekly",  # or "monthly"
            "page": 1,
            "limit": 100,
            "raw": 1,
            "meta": "expirations,field.shortName,field.type,field.description",
        }
        self.long_iron_butterfly_fields = {
            "endpoint": "options/long-iron-butterfly-spread",
            "symbol_param": "baseSymbol",
            "fields": LONG_IRON_BUTTERFLY_FIELDS,
            "orderBy": "breakEvenProbability",
            "orderDir": "desc",
            "expirationDate": "Example: 2025-06-27",
            "expirationType": "weekly",  # or "monthly"
            "page": 1,
            "limit": 100,
            "raw": 1,
            "meta": "expirations,field.shortName,field.type,field.description",
        }
        self.short_iron_butterfly_fields = {
            "endpoint": "options/short-iron-butterfly-spread",
            "symbol_param": "baseSymbol",
            "fields": SHORT_IRON_BUTTERFLY_FIELDS,
            "orderBy": "lossProbability",
            "orderDir": "asc",
            "expirationDate": "Example: 2025-06-27",
            "expirationType": "weekly",  # or "monthly"
            "page": 1,
            "limit": 100,
            "raw": 1,
            "meta": "expirations,field.shortName,field.type,field.description",
        }
