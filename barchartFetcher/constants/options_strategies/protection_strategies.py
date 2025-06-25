MARRIED_PUTS_FIELDS = (
    "baseSymbol,baseSymbolType,symbol,underlyingLastPrice,expirationDate,"
    "daysToExpiration,strike,strikePrice,moneyness,askPrice,breakEvenAsk,"
    "breakEvenPercentAsk,maxRisk,downside,volume,openInterest,"
    "impliedVolatilityRank1y,overallDelta,breakEvenProbability,tradeTime,"
    "symbolCode,symbolType,expirationType,daysToExpiration,"
    "impliedVolatilityRank1y,baseNextEarningsDate,timeCode,dividendExDate,"
    "historicVolatility30d,baseTrendSpotterSignal,baseTrendSpotterStrength,"
    "averageVolatility&orderBy=strikePrice&orderDir=asc"
)

LONG_COLLAR_SPREAD_FIELDS = (
    "baseSymbol,baseSymbolType,underlyingLastPrice,expirationDate,"
    "daysToExpiration,strikeLeg1,bidPriceLeg1,strikeLeg2,askPriceLeg2,"
    "breakEven,netDebitCredit,percentOfCost,maxProfit,maxLoss,maxRisk,"
    "upside,downside,overallDelta,breakEvenProbability,symbolCode,"
    "symbolType,expirationType,legs,daysToExpiration,averageVolatility,"
    "baseNextEarningsDate,timeCode,dividendExDate,historicVolatility30d,"
    "impliedVolatilityRank1y,baseTrendSpotterSignal,baseTrendSpotterStrength"
    "&orderBy=strikeLeg1&orderDir=asc"
)


class ProtectionStrategiesFields:
    def __init__(self):
        self.married_puts_fields = MARRIED_PUTS_FIELDS
        self.long_collar_spread_fields = LONG_COLLAR_SPREAD_FIELDS
        self.additional_infos = print(
            """
            Each strategy has its own endpoint:
            - Married Puts: "married_puts"
            - Long Collar Spread: "long_collar_spread"
            
            Pass symbol via `baseSymbol`;
            Default `meta` = "expirations,field.shortName,field.type,field.description"
            Default `raw` = 1
            Optional: [expirationDate(default="nearest"), expirationType(default="weekly"), page(default=1), limit(default=100)] parameters
            
            """
        )
