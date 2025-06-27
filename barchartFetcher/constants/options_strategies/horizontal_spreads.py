LONG_CALL_CALENDAR_FIELDS = (
    "baseSymbol,baseSymbolType,underlyingLastPrice,expirationDateLeg1,"
    "strikeLeg1,bidPriceLeg1,expirationDateLeg2,askPriceLeg2,netDebit,"
    "volatilityLeg1,volatilityLeg2,ivSkew,impliedVolatilityRank1y,"
    "intradayVs30dHistoricIV,netDelta,netVega,expirationType,averageVolatility,"
    "daysToExpiration,expirationDate,baseNextEarningsDate,timeCode,"
    "dividendExDate,historicVolatility30d,baseTrendSpotterSignal,"
    "baseTrendSpotterStrength,symbolCode,symbolType"
)

LONG_PUT_CALENDAR_FIELDS = (
    "baseSymbol,baseSymbolType,underlyingLastPrice,expirationDateLeg1,"
    "strikeLeg1,bidPriceLeg1,expirationDateLeg2,askPriceLeg2,netDebit,"
    "volatilityLeg1,volatilityLeg2,ivSkew,impliedVolatilityRank1y,"
    "intradayVs30dHistoricIV,netDelta,netVega,expirationType,averageVolatility,"
    "daysToExpiration,expirationDate,baseNextEarningsDate,timeCode,"
    "dividendExDate,historicVolatility30d,baseTrendSpotterSignal,"
    "baseTrendSpotterStrength,symbolCode,symbolType"
)

LONG_CALL_DIAGONAL_FIELDS = (
    "baseSymbol,baseSymbolType,underlyingLastPrice,expirationDateLeg1,"
    "strikeLeg1,askPriceLeg1,expirationDateLeg2,strikeLeg2,bidPriceLeg2,"
    "netDebit,volatilityLeg1,volatilityLeg2,ivSkewInverse,"
    "impliedVolatilityRank1y,intradayVs30dHistoricIV,netDelta,netVega,"
    "expirationType,averageVolatility,daysToExpiration,expirationDate,"
    "baseNextEarningsDate,timeCode,dividendExDate,historicVolatility30d,"
    "baseTrendSpotterSignal,baseTrendSpotterStrength,symbolCode,"
    "symbolType"
)

SHORT_CALL_DIAGONAL_FIELDS = (
    "baseSymbol,baseSymbolType,underlyingLastPrice,expirationDateLeg1,"
    "strikeLeg1,bidPriceLeg1,expirationDateLeg2,strikeLeg2,askPriceLeg2,"
    "netCredit,volatilityLeg1,volatilityLeg2,ivSkew,impliedVolatilityRank1y,"
    "intradayVs30dHistoricIV,netDelta,netVega,expirationType,averageVolatility,"
    "daysToExpiration,expirationDate,baseNextEarningsDate,timeCode,"
    "dividendExDate,historicVolatility30d,baseTrendSpotterSignal,"
    "baseTrendSpotterStrength,symbolCode,symbolType"
)

LONG_PUT_DIAGONAL_FIELDS = (
    "baseSymbol,baseSymbolType,underlyingLastPrice,expirationDateLeg1,"
    "strikeLeg1,bidPriceLeg1,expirationDateLeg2,strikeLeg2,askPriceLeg2,"
    "netDebit,volatilityLeg1,volatilityLeg2,ivSkew,impliedVolatilityRank1y,"
    "intradayVs30dHistoricIV,netDelta,netVega,expirationType,averageVolatility,"
    "daysToExpiration,expirationDate,baseNextEarningsDate,timeCode,"
    "dividendExDate,historicVolatility30d,baseTrendSpotterSignal,"
    "baseTrendSpotterStrength,symbolCode,symbolType"
)

SHORT_PUT_DIAGONAL_FIELDS = (
    "baseSymbol,baseSymbolType,underlyingLastPrice,expirationDateLeg1,"
    "strikeLeg1,askPriceLeg1,expirationDateLeg2,strikeLeg2,bidPriceLeg2,"
    "netDebit,volatilityLeg1,volatilityLeg2,ivSkewInverse,"
    "impliedVolatilityRank1y,intradayVs30dHistoricIV,netDelta,netVega,"
    "expirationType,averageVolatility,daysToExpiration,expirationDate,"
    "baseNextEarningsDate,timeCode,dividendExDate,baseTrendSpotterSignal,"
    "baseTrendSpotterStrength,symbolCode,symbolType"
)


class HorizontalSpreadsFields:
    def __init__(self):
        self.long_call_calendar_fields = {
            "endpoint": "options/long-call-calendar-spread",
            "symbol_param": "baseSymbol",
            "fields": LONG_CALL_CALENDAR_FIELDS,
            "orderBy": "ivSkew",
            "orderDir": "desc",
            "expirationDate": "Example: 2025-06-27",
            "expirationType": "weekly",
            "eq(type,call)": "",
            "meta": "expirations,field.shortName,field.type,field.description",
            "page": 1,
            "limit": 100,
            "raw": 1,
        }

        self.long_put_calendar_fields = {
            "endpoint": "options/long-put-calendar-spread",
            "symbol_param": "baseSymbol",
            "fields": LONG_PUT_CALENDAR_FIELDS,
            "orderBy": "ivSkew",
            "orderDir": "desc",
            "expirationDate": "Example: 2025-06-27",
            "expirationType": "weekly",
            "eq(type,put)": "",
            "meta": "expirations,field.shortName,field.type,field.description",
            "page": 1,
            "limit": 100,
            "raw": 1,
        }

        self.long_call_diagonal_fields = {
            "endpoint": "options/bull-calls-diagonal-spread",
            "symbol_param": "baseSymbol",
            "fields": LONG_CALL_DIAGONAL_FIELDS,
            "orderBy": "ivSkewInverse",
            "orderDir": "desc",
            "expirationDate": "Example: 2025-06-27",
            "expirationType": "weekly",
            "page": 1,
            "limit": 100,
            "raw": 1,
            "meta": "expirations,field.shortName,field.type,field.description",
        }

        self.short_call_diagonal_fields = {
            "endpoint": "options/bear-calls-diagonal-spread",
            "symbol_param": "baseSymbol",
            "fields": SHORT_CALL_DIAGONAL_FIELDS,
            "orderBy": "ivSkew",
            "orderDir": "desc",
            "expirationDate": "Example: 2025-06-27",
            "expirationType": "weekly",
            "page": 1,
            "limit": 100,
            "raw": 1,
            "meta": "expirations,field.shortName,field.type,field.description",
        }

        self.long_put_diagonal_fields = {
            "endpoint": "options/bull-puts-diagonal-spread",
            "symbol_param": "baseSymbol",
            "fields": LONG_PUT_DIAGONAL_FIELDS,
            "orderBy": "ivSkew",
            "orderDir": "desc",
            "expirationDate": "Example: 2025-06-27",
            "expirationType": "weekly",
            "page": 1,
            "limit": 100,
            "raw": 1,
            "meta": "expirations,field.shortName,field.type,field.description",
        }

        self.short_put_diagonal_fields = {
            "endpoint": "options/bear-puts-diagonal-spread",
            "symbol_param": "baseSymbol",
            "fields": SHORT_PUT_DIAGONAL_FIELDS,
            "orderBy": "ivSkewInverse",
            "orderDir": "desc",
            "expirationDate": "Example: 2025-06-27",
            "expirationType": "weekly",
            "page": 1,
            "limit": 100,
            "raw": 1,
            "meta": "expirations,field.shortName,field.type,field.description",
        }
