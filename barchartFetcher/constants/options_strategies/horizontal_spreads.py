LONG_CALL_CALENDAR_FIELDS = (
    "baseSymbol,baseSymbolType,underlyingLastPrice,expirationDateLeg1,"
    "strikeLeg1,bidPriceLeg1,expirationDateLeg2,askPriceLeg2,netDebit,volatilityLeg1,"
    "volatilityLeg2,ivSkew,impliedVolatilityRank1y,intradayVs30dHistoricIV,netDelta,"
    "netVega,expirationType,averageVolatility,daysToExpiration,expirationDate,"
    "baseNextEarningsDate,timeCode,dividendExDate,historicVolatility30d,"
    "baseTrendSpotterSignal,baseTrendSpotterStrength,symbolCode,symbolType"
    "&orderBy=ivSkew&orderDir=desc&eq(type,call)="
)

LONG_PUT_CALENDAR_FIELDS = (
    "baseSymbol,baseSymbolType,underlyingLastPrice,expirationDateLeg1,strikeLeg1,"
    "bidPriceLeg1,expirationDateLeg2,askPriceLeg2,netDebit,volatilityLeg1,"
    "volatilityLeg2,ivSkew,impliedVolatilityRank1y,intradayVs30dHistoricIV,"
    "netDelta,netVega,expirationType,averageVolatility,daysToExpiration,"
    "expirationDate,baseNextEarningsDate,timeCode,dividendExDate,"
    "historicVolatility30d,baseTrendSpotterSignal,baseTrendSpotterStrength,"
    "symbolCode,symbolType&orderBy=ivSkew&orderDir=desc&eq(type,put)="
)

LONG_CALL_DIAGONAL_FIELDS = (
    "baseSymbol,baseSymbolType,underlyingLastPrice,expirationDateLeg1,strikeLeg1,"
    "askPriceLeg1,expirationDateLeg2,strikeLeg2,bidPriceLeg2,netDebit,volatilityLeg1,"
    "volatilityLeg2,ivSkewInverse,impliedVolatilityRank1y,intradayVs30dHistoricIV,netDelta,"
    "netVega,expirationType,averageVolatility,daysToExpiration,expirationDate,"
    "baseNextEarningsDate,timeCode,dividendExDate,historicVolatility30d,"
    "baseTrendSpotterSignal,baseTrendSpotterStrength,symbolCode,symbolType"
    "&orderBy=ivSkewInverse&orderDir=desc"
)

SHORT_CALL_DIAGONAL_FIELDS = (
    "baseSymbol,baseSymbolType,underlyingLastPrice,expirationDateLeg1,strikeLeg1,"
    "bidPriceLeg1,expirationDateLeg2,strikeLeg2,askPriceLeg2,netCredit,volatilityLeg1,"
    "volatilityLeg2,ivSkew,impliedVolatilityRank1y,intradayVs30dHistoricIV,netDelta,"
    "netVega,expirationType,averageVolatility,daysToExpiration,expirationDate,"
    "baseNextEarningsDate,timeCode,dividendExDate,historicVolatility30d,"
    "baseTrendSpotterSignal,baseTrendSpotterStrength,symbolCode,symbolType"
    "&orderBy=ivSkew&orderDir=desc"
)

LONG_PUT_DIAGONAL_FIELDS = (
    "baseSymbol,baseSymbolType,underlyingLastPrice,expirationDateLeg1,strikeLeg1,"
    "bidPriceLeg1,expirationDateLeg2,strikeLeg2,askPriceLeg2,netDebit,volatilityLeg1,"
    "volatilityLeg2,ivSkew,impliedVolatilityRank1y,intradayVs30dHistoricIV,netDelta,"
    "netVega,expirationType,averageVolatility,daysToExpiration,expirationDate,"
    "baseNextEarningsDate,timeCode,dividendExDate,historicVolatility30d,"
    "baseTrendSpotterSignal,baseTrendSpotterStrength,"
    "symbolCode,symbolType&orderBy=ivSkew&orderDir=desc"
)

SHORT_PUT_DIAGONAL_FIELDS = (
    "baseSymbol,baseSymbolType,underlyingLastPrice,expirationDateLeg1,strikeLeg1,"
    "askPriceLeg1,expirationDateLeg2,strikeLeg2,bidPriceLeg2,netDebit,volatilityLeg1,"
    "volatilityLeg2,ivSkewInverse,impliedVolatilityRank1y,intradayVs30dHistoricIV,"
    "netDelta,netVega,expirationType,averageVolatility,daysToExpiration,"
    "expirationDate,baseNextEarningsDate,timeCode,dividendExDate,"
    "baseTrendSpotterSignal,baseTrendSpotterStrength,"
    "symbolCode,symbolType&orderBy=ivSkewInverse&orderDir=desc"
)


class HorizontalSpreadsFields:
    def __init__(self):
        self.long_call_calendar_fields = LONG_CALL_CALENDAR_FIELDS
        self.long_put_calendar_fields = LONG_PUT_CALENDAR_FIELDS
        self.long_call_diagonal_fields = LONG_CALL_DIAGONAL_FIELDS
        self.short_call_diagonal_fields = SHORT_CALL_DIAGONAL_FIELDS
        self.long_put_diagonal_fields = LONG_PUT_DIAGONAL_FIELDS
        self.short_put_diagonal_fields = SHORT_PUT_DIAGONAL_FIELDS
        self.additional_infos = print(
            """
            Each strategy has its own endpoint and fields.
            
            Add symbol field via `baseSymbol`;
            meta: expirations,field.shortName,field.type,field.description;
            raw: 1
            expirationDate: default "nearest"
            expirationType: default weekly
            page: defaut 1
            limit : default 100
            """
        )
