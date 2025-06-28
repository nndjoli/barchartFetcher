LONG_CALL_CONDOR_FIELDS = (
    "underlyingLastPrice,expirationDate,daysToExpiration,strikeLeg1,"
    "askPriceLeg1,strikeLeg2,bidPriceLeg2,strikeLeg3,bidPriceLeg3,strikeLeg4,"
    "askPriceLeg4,upperBreakEven,upperBreakEvenPercent,lowerBreakEven,"
    "lowerBreakEvenPercent,maxProfit,maxLoss,riskRewardRatio,"
    "impliedVolatilityRank1y,breakEvenProbability,baseNextEarningsDate,timeCode,"
    "dividendExDate,historicVolatility30d,averageVolatility,"
    "baseTrendSpotterSignal,baseTrendSpotterStrength,symbolCode,symbolType"
)

SHORT_CALL_CONDOR_FIELDS = (
    "underlyingLastPrice,expirationDate,daysToExpiration,strikeLeg1,"
    "bidPriceLeg1,strikeLeg2,askPriceLeg2,strikeLeg3,askPriceLeg3,strikeLeg4,"
    "bidPriceLeg4,upperBreakEven,upperBreakEvenPercent,lowerBreakEven,"
    "lowerBreakEvenPercent,maxProfit,maxLoss,riskRewardRatio,"
    "impliedVolatilityRank1y,lossProbability,baseNextEarningsDate,timeCode,"
    "dividendExDate,historicVolatility30d,averageVolatility,"
    "baseTrendSpotterSignal,baseTrendSpotterStrength,symbolCode,symbolType"
)

LONG_PUT_CONDOR_FIELDS = (
    "underlyingLastPrice,expirationDate,daysToExpiration,strikeLeg1,"
    "askPriceLeg1,strikeLeg2,bidPriceLeg2,strikeLeg3,bidPriceLeg3,strikeLeg4,"
    "askPriceLeg4,upperBreakEven,upperBreakEvenPercent,lowerBreakEven,"
    "lowerBreakEvenPercent,maxProfit,maxLoss,riskRewardRatio,"
    "impliedVolatilityRank1y,breakEvenProbability,baseNextEarningsDate,timeCode,"
    "dividendExDate,historicVolatility30d,averageVolatility,"
    "baseTrendSpotterSignal,baseTrendSpotterStrength,symbolCode,symbolType"
)

SHORT_PUT_CONDOR_FIELDS = (
    "underlyingLastPrice,expirationDate,daysToExpiration,strikeLeg1,"
    "bidPriceLeg1,strikeLeg2,askPriceLeg2,strikeLeg3,askPriceLeg3,strikeLeg4,"
    "bidPriceLeg4,upperBreakEven,upperBreakEvenPercent,lowerBreakEven,"
    "lowerBreakEvenPercent,maxProfit,maxLoss,riskRewardRatio,"
    "impliedVolatilityRank1y,lossProbability,baseNextEarningsDate,timeCode,"
    "dividendExDate,historicVolatility30d,averageVolatility,"
    "baseTrendSpotterSignal,baseTrendSpotterStrength,symbolCode,symbolType"
)

LONG_IRON_CONDOR_FIELDS = (
    "underlyingLastPrice,expirationDate,daysToExpiration,strikeLeg1,"
    "bidPriceLeg1,strikeLeg2,askPriceLeg2,strikeLeg3,askPriceLeg3,strikeLeg4,"
    "bidPriceLeg4,upperBreakEven,upperBreakEvenPercent,lowerBreakEven,"
    "lowerBreakEvenPercent,maxProfit,maxLoss,riskRewardRatio,"
    "impliedVolatilityRank1y,breakEvenProbability,baseNextEarningsDate,timeCode,"
    "dividendExDate,historicVolatility30d,averageVolatility,"
    "baseTrendSpotterSignal,baseTrendSpotterStrength,symbolCode,symbolType"
)

SHORT_IRON_CONDOR_FIELDS = (
    "underlyingLastPrice,expirationDate,daysToExpiration,strikeLeg1,"
    "askPriceLeg1,strikeLeg2,bidPriceLeg2,strikeLeg3,bidPriceLeg3,strikeLeg4,"
    "askPriceLeg4,upperBreakEven,upperBreakEvenPercent,lowerBreakEven,"
    "lowerBreakEvenPercent,maxProfit,maxLoss,riskRewardRatio,"
    "impliedVolatilityRank1y,lossProbability,baseNextEarningsDate,timeCode,"
    "dividendExDate,historicVolatility30d,averageVolatility,"
    "baseTrendSpotterSignal,baseTrendSpotterStrength,symbolCode,symbolType"
)


class CondorFields:
    def __init__(self):
        self.long_call_condor_fields = {
            "endpoint": "long_call_condor",
            "symbol_param": "baseSymbol",
            "fields": LONG_CALL_CONDOR_FIELDS,
            "orderBy": "breakEvenProbability",
            "orderDir": "desc",
            "expirationDate": "<expiration_date>",
            "expirationType": "weekly",  # or "monthly"
            "meta": "expirations,field.shortName,field.type,field.description",
            "page": 1,
            "limit": 100,
            "raw": 1,
        }

        self.short_call_condor_fields = {
            "endpoint": "short_call_condor",
            "symbol_param": "baseSymbol",
            "fields": SHORT_CALL_CONDOR_FIELDS,
            "orderBy": "lossProbability",
            "orderDir": "asc",
            "expirationDate": "<expiration_date>",
            "expirationType": "weekly",  # or "monthly"
            "meta": "expirations,field.shortName,field.type,field.description",
            "page": 1,
            "limit": 100,
            "raw": 1,
        }

        self.long_put_condor_fields = {
            "endpoint": "long_put_condor",
            "symbol_param": "baseSymbol",
            "fields": LONG_PUT_CONDOR_FIELDS,
            "orderBy": "breakEvenProbability",
            "orderDir": "desc",
            "expirationDate": "<expiration_date>",
            "expirationType": "weekly",  # or "monthly"
            "meta": "expirations,field.shortName,field.type,field.description",
            "page": 1,
            "limit": 100,
            "raw": 1,
        }

        self.short_put_condor_fields = {
            "endpoint": "short_put_condor",
            "symbol_param": "baseSymbol",
            "fields": SHORT_PUT_CONDOR_FIELDS,
            "orderBy": "lossProbability",
            "orderDir": "asc",
            "expirationDate": "<expiration_date>",
            "expirationType": "weekly",  # or "monthly"
            "meta": "expirations,field.shortName,field.type,field.description",
            "page": 1,
            "limit": 100,
            "raw": 1,
        }

        self.long_iron_condor_fields = {
            "endpoint": "long_iron_condor",
            "symbol_param": "baseSymbol",
            "fields": LONG_IRON_CONDOR_FIELDS,
            "orderBy": "breakEvenProbability",
            "orderDir": "desc",
            "expirationDate": "<expiration_date>",
            "expirationType": "weekly",  # or "monthly"
            "meta": "expirations,field.shortName,field.type,field.description",
            "page": 1,
            "limit": 100,
            "raw": 1,
        }

        self.short_iron_condor_fields = {
            "endpoint": "short_iron_condor",
            "symbol_param": "baseSymbol",
            "fields": SHORT_IRON_CONDOR_FIELDS,
            "orderBy": "lossProbability",
            "orderDir": "asc",
            "expirationDate": "<expiration_date>",
            "expirationType": "weekly",  # or "monthly"
            "meta": "expirations,field.shortName,field.type,field.description",
            "page": 1,
            "limit": 100,
            "raw": 1,
        }
