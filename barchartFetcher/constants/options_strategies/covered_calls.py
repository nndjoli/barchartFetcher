# Covered Calls Fields:
COVERED_CALLS_FIELDS = (
    "symbol,baseSymbol,underlyingLastPrice,expirationDate,daysToExpiration,strike,"
    "moneyness,bidPrice,breakEvenBid,percentToBreakEvenBid,volume,openInterest,"
    "impliedVolatilityRank1y,delta,flat,flatAnnual,potentialReturn,breakEvenProbability,"
    "tradeTime,averageVolatility,baseNextEarningsDate,timeCode,dividendExDate,"
    "historicVolatility30d,impliedVolatilityRank1y,baseTrendSpotterSignal,"
    "baseTrendSpotterStrength,symbolCode,symbolType"
    "&orderBy=strike&orderDir=desc&between(delta,0.1,0.6)="
)


class CoveredCallsFields:
    def __init__(self):
        self.covered_calls_fields = COVERED_CALLS_FIELDS
        self.covered_calls_endpoint = "covered_calls"
        self.additional_infos = print(
            """
            Pass symbol via `baseSymbol`;
            Default `meta` = "expirations,field.shortName,field.type,field.description"
            Default `raw` = 1
            Optional: [expirationDate, expirationType, page] parameters
            """
        )
