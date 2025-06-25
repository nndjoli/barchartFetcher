LONG_CALL_BUTTERFLY_FIELDS = (
    "underlyingLastPrice,expirationDate,daysToExpiration,strikeLeg1,"
    "askPriceLeg1,strikeLeg2,bidPriceLeg2,strikeLeg3,askPriceLeg3,"
    "upperBreakEven,upperBreakEvenPercent,lowerBreakEven,"
    "lowerBreakEvenPercent,maxProfit,maxLoss,riskRewardRatio,"
    "breakEven,breakEvenProbability,baseNextEarningsDate,timeCode,"
    "dividendExDate,historicVolatility30d,impliedVolatilityRank1y,"
    "averageVolatility,baseTrendSpotterSignal,baseTrendSpotterStrength,"
    "symbolCode,symbolType&orderBy=breakEvenProbability&orderDir=desc"
)

SHORT_CALL_BUTTERFLY_FIELDS = (
    "underlyingLastPrice,expirationDate,daysToExpiration,strikeLeg1,"
    "bidPriceLeg1,strikeLeg2,askPriceLeg2,strikeLeg3,bidPriceLeg3,"
    "upperBreakEven,upperBreakEvenPercent,lowerBreakEven,"
    "lowerBreakEvenPercent,maxProfit,maxLoss,riskRewardRatio,breakEven,"
    "lossProbability,baseNextEarningsDate,timeCode,dividendExDate,"
    "historicVolatility30d,impliedVolatilityRank1y,averageVolatility,"
    "baseTrendSpotterSignal,baseTrendSpotterStrength,symbolCode,symbolType"
    "&orderBy=lossProbability&orderDir=asc"
)

LONG_PUT_BUTTERFLY_FIELDS = (
    "underlyingLastPrice,expirationDate,daysToExpiration,strikeLeg1,askPriceLeg1,"
    "strikeLeg2,bidPriceLeg2,strikeLeg3,askPriceLeg3,upperBreakEven,"
    "upperBreakEvenPercent,lowerBreakEven,lowerBreakEvenPercent,maxProfit,"
    "maxLoss,riskRewardRatio,breakEven,breakEvenProbability,baseNextEarningsDate,"
    "timeCode,dividendExDate,historicVolatility30d,impliedVolatilityRank1y,"
    "averageVolatility,baseTrendSpotterSignal,baseTrendSpotterStrength,symbolCode,"
    "symbolType&orderBy=breakEvenProbability&orderDir=desc"
)

SHORT_PUT_BUTTERFLY_FIELDS = (
    "underlyingLastPrice,expirationDate,daysToExpiration,strikeLeg1,bidPriceLeg1,"
    "strikeLeg2,askPriceLeg2,strikeLeg3,bidPriceLeg3,upperBreakEven,"
    "upperBreakEvenPercent,lowerBreakEven,lowerBreakEvenPercent,maxProfit,"
    "maxLoss,riskRewardRatio,breakEven,lossProbability,baseNextEarningsDate,"
    "timeCode,dividendExDate,historicVolatility30d,impliedVolatilityRank1y,"
    "averageVolatility,baseTrendSpotterSignal,baseTrendSpotterStrength,"
    "symbolCode,symbolType&orderBy=lossProbability&orderDir=asc"
)

LONG_IRON_BUTTERFLY_FIELDS = (
    "underlyingLastPrice,expirationDate,daysToExpiration,strikeLeg1,bidPriceLeg1,"
    "strikeLeg2,askPriceLeg2,strikeLeg3,askPriceLeg3,strikeLeg4,bidPriceLeg4,"
    "upperBreakEven,upperBreakEvenPercent,lowerBreakEven,lowerBreakEvenPercent,"
    "maxProfit,maxLoss,riskRewardRatio,breakEvenProbability,baseNextEarningsDate,"
    "timeCode,dividendExDate,historicVolatility30d,impliedVolatilityRank1y,"
    "averageVolatility,baseTrendSpotterSignal,baseTrendSpotterStrength,symbolCode,"
    "symbolType&orderBy=breakEvenProbability&orderDir=desc"
)

SHORT_IRON_BUTTERFLY_FIELDS = (
    "underlyingLastPrice,expirationDate,daysToExpiration,strikeLeg1,askPriceLeg1,"
    "strikeLeg2,bidPriceLeg2,strikeLeg3,bidPriceLeg3,strikeLeg4,askPriceLeg4,"
    "upperBreakEven,upperBreakEvenPercent,lowerBreakEven,lowerBreakEvenPercent,"
    "maxProfit,maxLoss,riskRewardRatio,breakEven,lossProbability,"
    "baseNextEarningsDate,timeCode,dividendExDate,historicVolatility30d,"
    "impliedVolatilityRank1y,averageVolatility,baseTrendSpotterSignal,"
    "baseTrendSpotterStrength,symbolCode,symbolType&orderBy=lossProbability&orderDir=asc"
)


class ButterflySpreadsFields:
    def __init__(self):
        self.long_call_butterfly_fields = LONG_CALL_BUTTERFLY_FIELDS
        self.short_call_butterfly_fields = SHORT_CALL_BUTTERFLY_FIELDS
        self.long_put_butterfly_fields = LONG_PUT_BUTTERFLY_FIELDS
        self.short_put_butterfly_fields = SHORT_PUT_BUTTERFLY_FIELDS
        self.long_iron_butterfly_fields = LONG_IRON_BUTTERFLY_FIELDS
        self.short_iron_butterfly_fields = SHORT_IRON_BUTTERFLY_FIELDS
        self.additional_infos = print(
            """
            Add symbol via `baseSymbol`;
            meta: expirations,field.shortName,field.type,field.description;
            expirationDate: "nearest" (default_value)
            expirationType: "weekly" (default_value)
            page: 1 (default_value)
            limit: 100 (default_value)
            raw: 1 (default_value)
            """
        )
