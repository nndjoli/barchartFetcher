# Covered Calls Fields:
COVERED_CALLS_FIELDS = (
    "symbol,baseSymbol,underlyingLastPrice,expirationDate,daysToExpiration,"
    "strike,moneyness,bidPrice,breakEvenBid,percentToBreakEvenBid,volume,"
    "openInterest,impliedVolatilityRank1y,delta,flat,flatAnnual,potentialReturn,"
    "breakEvenProbability,tradeTime,averageVolatility,baseNextEarningsDate,"
    "timeCode,dividendExDate,historicVolatility30d,impliedVolatilityRank1y,"
    "baseTrendSpotterSignal,baseTrendSpotterStrength,symbolCode,"
    "symbolType"
)


class CoveredCallsFields:
    def __init__(self):
        self.covered_calls_fields = {
            "endpoint": "covered_calls",
            "symbol_param": "baseSymbol",
            "fields": COVERED_CALLS_FIELDS,
            "orderBy": "strike",
            "orderDir": "desc",
            "expirationDate": "Example: 2025-06-27",
            "meta": "expirations,field.shortName,field.type,field.description",
            "ge(tradeTime,previousTradingDay)": "",
            "between(delta,0.1,0.6)": "",
            "expirationType": "weekly",
            "page": 1,
            "raw": 1,
        }
