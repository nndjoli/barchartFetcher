# Long Call Fields
LONG_CALL_FIELDS = (
    "underlyingLastPrice,expirationDate,daysToExpiration,"
    "strike,moneyness,symbol,baseSymbol,askPrice,"
    "timePremiumAskPercent,breakEvenAsk,percentToBreakEvenAsk,"
    "netDebit,daysToExpiration,volume,openInterest,impliedVolatilityRank1y,"
    "delta,breakEvenProbability,tradeTime,otmProbability,averageVolatility,"
    "baseNextEarningsDate,timeCode,dividendExDate,historicVolatility30d,"
    "baseTrendSpotterSignal,baseTrendSpotterStrength,symbolCode,symbolType,"
    "hasOptions&orderBy=strikePrice&orderDir=desc&eq(symbolType,call)="
    "&ge(tradeTime,previousTradingDay)=&between(delta,0.2,0.9)="
)

# Long Put Fields:
LONG_PUT_FIELDS = (
    "underlyingLastPrice,expirationDate,daysToExpiration,"
    "strike,moneyness,symbol,baseSymbol,askPrice,"
    "timePremiumAskPercent,breakEvenAsk,percentToBreakEvenAsk,"
    "netDebit,daysToExpiration,volume,openInterest,impliedVolatilityRank1y,"
    "delta,breakEvenProbability,tradeTime,otmProbability,averageVolatility,"
    "baseNextEarningsDate,timeCode,dividendExDate,historicVolatility30d,"
    "baseTrendSpotterSignal,baseTrendSpotterStrength,symbolCode,symbolType,"
    "hasOptions&orderBy=strikePrice&orderDir=desc&eq(symbolType,put)="
    "&ge(tradeTime,previousTradingDay)=&between(delta,-0.9,-0.2)="
)


class LongCallPutFields:
    def __init__(self):
        self.long_call_fields = LONG_CALL_FIELDS
        self.long_put_fields = LONG_PUT_FIELDS
        self.additional_infos = print(
            """
            Endpoint: "options"
            Add symbol field via `baseSymbol`;
            meta: expirations,field.shortName,field.type,field.description;
            raw: 1
            """
        )
