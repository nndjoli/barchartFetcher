# Naked Puts Fields:
NAKED_PUTS_FIELDS = (
    "symbol,symbolType,symbolCode,baseSymbol,"
    "underlyingLastPrice,expirationDate,daysToExpiration,"
    "strike,moneyness,bidPrice,breakEvenBid,percentToBreakEvenBid,"
    "volume,openInterest,impliedVolatilityRank1y,delta,potentialReturn,"
    "potentialReturnAnnual,breakEvenProbability,tradeTime,averageVolatility,"
    "baseNextEarningsDate,timeCode,dividendExDate,historicVolatility30d,"
    "baseTrendSpotterSignal,baseTrendSpotterStrength&orderBy=strike"
    "&orderDir=asc&between(delta,-0.6,-0.1)="
)


class NakedPutsFields:
    def __init__(self):
        self.naked_puts_fields = NAKED_PUTS_FIELDS
        self.naked_puts_endpoint = "naked_puts"
        self.additional_infos = """
        Pass symbol using baseSymbol;
        Default meta = field.shortName,field.description,expirations,field.shortName,field.type;
        Optional: [expirationDate, expirationType, page] parameters; 
        Default raw = 1
        """
