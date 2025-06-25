LONG_CALL_CONDOR_FIELDS = (
    "underlyingLastPrice,expirationDate,daysToExpiration,strikeLeg1,"
    "askPriceLeg1,strikeLeg2,bidPriceLeg2,strikeLeg3,bidPriceLeg3,strikeLeg4,"
    "askPriceLeg4,upperBreakEven,upperBreakEvenPercent,lowerBreakEven,"
    "lowerBreakEvenPercent,maxProfit,maxLoss,riskRewardRatio,"
    "impliedVolatilityRank1y,breakEvenProbability,baseNextEarningsDate,"
    "timeCode,dividendExDate,historicVolatility30d,averageVolatility,"
    "baseTrendSpotterSignal,baseTrendSpotterStrength,symbolCode,symbolType,"
    "&orderBy=breakEvenProbability&orderDir=desc"
)

SHORT_CALL_CONDOR_FIELDS = (
    "underlyingLastPrice,expirationDate,daysToExpiration,strikeLeg1,"
    "bidPriceLeg1,strikeLeg2,askPriceLeg2,strikeLeg3,askPriceLeg3,strikeLeg4,"
    "bidPriceLeg4,upperBreakEven,upperBreakEvenPercent,lowerBreakEven,"
    "lowerBreakEvenPercent,maxProfit,maxLoss,riskRewardRatio,"
    "impliedVolatilityRank1y,lossProbability,baseNextEarningsDate,timeCode,"
    "dividendExDate,historicVolatility30d,averageVolatility,"
    "baseTrendSpotterSignal,baseTrendSpotterStrength,symbolCode,symbolType,"
    "&orderBy=lossProbability&orderDir=asc"
)

LONG_PUT_CONDOR_FIELDS = (
    "underlyingLastPrice,expirationDate,daysToExpiration,strikeLeg1,"
    "askPriceLeg1,strikeLeg2,bidPriceLeg2,strikeLeg3,bidPriceLeg3,strikeLeg4,"
    "askPriceLeg4,upperBreakEven,upperBreakEvenPercent,lowerBreakEven,"
    "lowerBreakEvenPercent,maxProfit,maxLoss,riskRewardRatio,"
    "impliedVolatilityRank1y,breakEvenProbability,baseNextEarningsDate,"
    "timeCode,dividendExDate,historicVolatility30d,averageVolatility,"
    "baseTrendSpotterSignal,baseTrendSpotterStrength,symbolCode,symbolType,"
    "&orderBy=breakEvenProbability&orderDir=desc"
)

SHORT_PUT_CONDOR_FIELDS = (
    "underlyingLastPrice,expirationDate,daysToExpiration,strikeLeg1,"
    "bidPriceLeg1,strikeLeg2,askPriceLeg2,strikeLeg3,askPriceLeg3,strikeLeg4,"
    "bidPriceLeg4,upperBreakEven,upperBreakEvenPercent,lowerBreakEven,"
    "lowerBreakEvenPercent,maxProfit,maxLoss,riskRewardRatio,"
    "impliedVolatilityRank1y,lossProbability,baseNextEarningsDate,timeCode,"
    "dividendExDate,historicVolatility30d,averageVolatility,"
    "baseTrendSpotterSignal,baseTrendSpotterStrength,symbolCode,symbolType,"
    "&orderBy=lossProbability&orderDir=asc"
)

LONG_IRON_CONDOR_FIELDS = (
    "underlyingLastPrice,expirationDate,daysToExpiration,strikeLeg1,"
    "bidPriceLeg1,strikeLeg2,askPriceLeg2,strikeLeg3,askPriceLeg3,strikeLeg4,"
    "bidPriceLeg4,upperBreakEven,upperBreakEvenPercent,lowerBreakEven,"
    "lowerBreakEvenPercent,maxProfit,maxLoss,riskRewardRatio,"
    "impliedVolatilityRank1y,breakEvenProbability,baseNextEarningsDate,"
    "timeCode,dividendExDate,historicVolatility30d,averageVolatility,"
    "baseTrendSpotterSignal,baseTrendSpotterStrength,symbolCode,symbolType,"
    "&orderBy=breakEvenProbability&orderDir=desc"
)

SHORT_IRON_CONDOR_FIELDS = (
    "underlyingLastPrice,expirationDate,daysToExpiration,strikeLeg1,"
    "askPriceLeg1,strikeLeg2,bidPriceLeg2,strikeLeg3,bidPriceLeg3,strikeLeg4,"
    "askPriceLeg4,upperBreakEven,upperBreakEvenPercent,lowerBreakEven,"
    "lowerBreakEvenPercent,maxProfit,maxLoss,riskRewardRatio,"
    "impliedVolatilityRank1y,lossProbability,baseNextEarningsDate,timeCode,"
    "dividendExDate,historicVolatility30d,averageVolatility,"
    "baseTrendSpotterSignal,baseTrendSpotterStrength,symbolCode,symbolType,"
    "&orderBy=lossProbability&orderDir=asc"
)


class CondorFields:
    def __init__(self):
        self.long_call_condor_fields = LONG_CALL_CONDOR_FIELDS
        self.short_call_condor_fields = SHORT_CALL_CONDOR_FIELDS
        self.long_put_condor_fields = LONG_PUT_CONDOR_FIELDS
        self.short_put_condor_fields = SHORT_PUT_CONDOR_FIELDS
        self.long_iron_condor_fields = LONG_IRON_CONDOR_FIELDS
        self.short_iron_condor_fields = SHORT_IRON_CONDOR_FIELDS
        self.additional_infos = print(
            """
            Each condor strategy has its own endpoint/ fields combination;
            Add symbol field via `baseSymbol`;
            meta: expirations,field.shortName,field.type,field.description;
            expirationDate: 'nearest' (default_value);
            expirationType: 'weekly' (default_value);
            page: 1 (default_value);
            pageSize: 100 (default_value);
            raw: 1
            """
        )
