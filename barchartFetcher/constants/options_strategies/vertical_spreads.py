BULL_CALL_SPREADS_FIELDS = (
    "breakEven,breakEvenPercent,maxProfit,maxLoss,maxProfitPercent,"
    "riskRewardRatio,impliedVolatilityRank1y,breakEvenProbability,time,"
    "averageVolatility,baseNextEarningsDate,timeCode,dividendExDate,"
    "historicVolatility30d,impliedVolatilityRank1y,baseTrendSpotterSignal,"
    "baseTrendSpotterStrength,symbolCode,symbolType&orderBy=strikeLeg1"
    "&orderDir=asc&between(abs(deltaLeg1),0.3,)=&between(abs(deltaLeg2),0.1,)="
    "&between(riskRewardRatio,0.33,1.5)="
)

BEAR_CALL_SPREADS_FIELDS = (
    "underlyingLastPrice,expirationDate,daysToExpiration,strikeLeg1,bidPriceLeg1,"
    "strikeLeg2,askPriceLeg2,breakEven,breakEvenPercent,maxProfit,maxLoss,"
    "maxProfitPercent,riskRewardRatio,impliedVolatilityRank1y,lossProbability,"
    "time,averageVolatility,baseNextEarningsDate,timeCode,dividendExDate,"
    "historicVolatility30d,impliedVolatilityRank1y,baseTrendSpotterSignal,"
    "baseTrendSpotterStrength,symbolCode,symbolType&orderBy=strikeLeg1"
    "&orderDir=desc&between(abs(deltaLeg1),0,0.6)=&between(abs(deltaLeg2),,0.3)="
    "&between(riskRewardRatio,2,5)="
)

BEAR_PUT_SPREADS_FIELDS = (
    "underlyingLastPrice,expirationDate,daysToExpiration,strikeLeg1,askPriceLeg1,"
    "strikeLeg2,bidPriceLeg2,breakEven,breakEvenPercent,maxProfit,maxLoss,"
    "maxProfitPercent,riskRewardRatio,impliedVolatilityRank1y,breakEvenProbability,"
    "time,averageVolatility,baseNextEarningsDate,timeCode,dividendExDate,"
    "historicVolatility30d,impliedVolatilityRank1y,baseTrendSpotterSignal,"
    "baseTrendSpotterStrength,symbolCode,symbolType&orderBy=strikeLeg1"
    "&orderDir=desc&between(abs(deltaLeg1),0.3,)=&between(abs(deltaLeg2),0.1,)"
    "&between(riskRewardRatio,0.33,1.5)="
)

BULL_PUT_SPREADS_FIELDS = (
    "underlyingLastPrice,expirationDate,daysToExpiration,strikeLeg1,bidPriceLeg1,"
    "strikeLeg2,askPriceLeg2,breakEven,breakEvenPercent,maxProfit,maxLoss,"
    "maxProfitPercent,riskRewardRatio,impliedVolatilityRank1y,lossProbability,"
    "time,averageVolatility,baseNextEarningsDate,timeCode,dividendExDate,"
    "historicVolatility30d,impliedVolatilityRank1y,baseTrendSpotterSignal,"
    "baseTrendSpotterStrength,symbolCode,symbolType&orderBy=strikeLeg1"
    "&orderDir=asc&between(abs(deltaLeg1),,0.6)=&between(abs(deltaLeg2),0,0.3)="
    "&between(riskRewardRatio,2,5)="
)


class VerticalSpreadsFields:
    def __init__(self):
        self.bull_call_spreads_fields = BULL_CALL_SPREADS_FIELDS
        self.bear_call_spreads_fields = BEAR_CALL_SPREADS_FIELDS
        self.bear_put_spreads_fields = BEAR_PUT_SPREADS_FIELDS
        self.bull_put_spreads_fields = BULL_PUT_SPREADS_FIELDS
        self.additional_infos = """
            Each spread type has its own endpoint:
            - Bull Call Spreads: `bull-calls-spread`
            - Bear Call Spreads: `bear-calls-spread`
            - Bear Put Spreads: `bear-puts-spread`
            - Bull Put Spreads: `bull-puts-spread`

            Pass symbol using baseSymbol;
            Default meta = field.shortName,field.description,expirations,field.shortName,field.type;
            Optional: [expirationDate, expirationType] parameters;
            Default raw = 1
        """
