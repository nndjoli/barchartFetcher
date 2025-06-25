LONG_STRADDLE_FIELDS = (
    "underlyingLastPrice,expirationDate,daysToExpiration,strikeLeg1,askPriceLeg1,strikeLeg2,"
    "askPriceLeg2,upperBreakEven,upperBreakEvenPercent,lowerBreakEven,lowerBreakEvenPercent,"
    "netCredit,netDebit,percentOfStock,impliedVolatilityRank1y,intradayVs30dHistoricIV,netDelta,"
    "breakEvenProbability,baseNextEarningsDate,timeCode,dividendExDate,historicVolatility30d,"
    "baseTrendSpotterSignal,baseTrendSpotterStrength,averageVolatility,symbolCode,"
    "symbolType&orderBy=strikeLeg1&orderDir=asc"
)

SHORT_STRADDLE_FIELDS = (
    "underlyingLastPrice,expirationDate,daysToExpiration,strikeLeg1,bidPriceLeg1,strikeLeg2,"
    "bidPriceLeg2,upperBreakEven,upperBreakEvenPercent,lowerBreakEven,lowerBreakEvenPercent,"
    "netCredit,netDebit,percentOfStock,impliedVolatilityRank1y,intradayVs30dHistoricIV,netDelta,"
    "lossProbability,baseNextEarningsDate,timeCode,dividendExDate,historicVolatility30d,"
    "baseTrendSpotterSignal,baseTrendSpotterStrength,averageVolatility,symbolCode,symbolType"
    "&orderBy=strikeLeg1&orderDir=asc"
)

LONG_STRANGLE_FIELDS = (
    "underlyingLastPrice,expirationDate,daysToExpiration,strikeLeg1,askPriceLeg1,strikeLeg2,"
    "askPriceLeg2,upperBreakEven,upperBreakEvenPercent,lowerBreakEven,lowerBreakEvenPercent,"
    "netCredit,netDebit,percentOfStock,impliedVolatilityRank1y,intradayVs30dHistoricIV,netDelta,"
    "breakEvenProbability,baseNextEarningsDate,timeCode,dividendExDate,historicVolatility30d,"
    "baseTrendSpotterSignal,baseTrendSpotterStrength,averageVolatility,symbolCode,symbolType"
    "&orderBy=strikeLeg1&orderDir=asc"
)

SHORT_STRANGLE_FIELDS = (
    "underlyingLastPrice,expirationDate,daysToExpiration,strikeLeg1,bidPriceLeg1,strikeLeg2,"
    "bidPriceLeg2,upperBreakEven,upperBreakEvenPercent,lowerBreakEven,lowerBreakEvenPercent,"
    "netCredit,netDebit,percentOfStock,impliedVolatilityRank1y,intradayVs30dHistoricIV,netDelta,"
    "lossProbability,maxProfitProbability,baseNextEarningsDate,timeCode,dividendExDate,"
    "historicVolatility30d,baseTrendSpotterSignal,baseTrendSpotterStrength,averageVolatility,"
    "symbolCode,symbolType&orderBy=strikeLeg1&orderDir=asc"
)


class StraddlesStranglesFields:
    def __init__(self):
        self.long_straddle_fields = LONG_STRADDLE_FIELDS
        self.short_straddle_fields = SHORT_STRADDLE_FIELDS
        self.long_strangle_fields = LONG_STRANGLE_FIELDS
        self.short_strangle_fields = SHORT_STRANGLE_FIELDS
        self.additional_infos = print(
            """
            Each strategy has its own endpoint:
            - Long Straddle: "long_straddle"
            - Short Straddle: "short_straddle"
            - Long Strangle: "long_strangle"
            - Short Strangle: "short_strangle"
            
            Pass symbol via `baseSymbol`;
            Default `meta` = "expirations,field.shortName,field.type,field.description"
            Default `raw` = 1
            Optional: [expirationDate(default="nearest"), expirationType(default="weekly"), page(default=1), limit(default=100)] parameters
            
            """
        )
