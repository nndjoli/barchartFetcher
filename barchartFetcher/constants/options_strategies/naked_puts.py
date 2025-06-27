# Naked Puts Fields:
NAKED_PUTS_FIELDS = (
    "symbol,symbolType,symbolCode,baseSymbol,underlyingLastPrice,expirationDate,"
    "daysToExpiration,strike,moneyness,bidPrice,breakEvenBid,"
    "percentToBreakEvenBid,volume,openInterest,impliedVolatilityRank1y,delta,"
    "potentialReturn,potentialReturnAnnual,breakEvenProbability,tradeTime,"
    "averageVolatility,baseNextEarningsDate,timeCode,dividendExDate,"
    "historicVolatility30d,baseTrendSpotterSignal,"
    "baseTrendSpotterStrength"
)


class NakedPutsFields:
    def __init__(self):
        self.naked_puts_fields = {
            "endpoint": "options/naked-puts",
            "symbol_param": "baseSymbol",
            "fields": NAKED_PUTS_FIELDS,
            "orderBy": "strike",
            "orderDir": "asc",
            "expirationDate": "Example: 2025-06-27",
            "meta": "expirations,field.shortName,field.type,field.description",
            "between(delta,-0.6,-0.1)": "",
            "expirationType": "weekly",
            "page": 1,
            "raw": 1,
        }
