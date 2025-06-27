BULL_CALL_SPREADS_FIELDS = (
    "breakEven,breakEvenPercent,maxProfit,maxLoss,maxProfitPercent,"
    "riskRewardRatio,impliedVolatilityRank1y,breakEvenProbability,time,"
    "averageVolatility,baseNextEarningsDate,timeCode,dividendExDate,"
    "historicVolatility30d,impliedVolatilityRank1y,baseTrendSpotterSignal,"
    "baseTrendSpotterStrength,symbolCode,"
    "symbolType"
)

BEAR_CALL_SPREADS_FIELDS = (
    "underlyingLastPrice,expirationDate,daysToExpiration,strikeLeg1,"
    "bidPriceLeg1,strikeLeg2,askPriceLeg2,breakEven,breakEvenPercent,maxProfit,"
    "maxLoss,maxProfitPercent,riskRewardRatio,impliedVolatilityRank1y,"
    "lossProbability,time,averageVolatility,baseNextEarningsDate,timeCode,"
    "dividendExDate,historicVolatility30d,impliedVolatilityRank1y,"
    "baseTrendSpotterSignal,baseTrendSpotterStrength,symbolCode,"
    "symbolType"
)

BEAR_PUT_SPREADS_FIELDS = (
    "underlyingLastPrice,expirationDate,daysToExpiration,strikeLeg1,"
    "askPriceLeg1,strikeLeg2,bidPriceLeg2,breakEven,breakEvenPercent,maxProfit,"
    "maxLoss,maxProfitPercent,riskRewardRatio,impliedVolatilityRank1y,"
    "breakEvenProbability,time,averageVolatility,baseNextEarningsDate,timeCode,"
    "dividendExDate,historicVolatility30d,impliedVolatilityRank1y,"
    "baseTrendSpotterSignal,baseTrendSpotterStrength,symbolCode,"
    "symbolType"
)

BULL_PUT_SPREADS_FIELDS = (
    "underlyingLastPrice,expirationDate,daysToExpiration,strikeLeg1,"
    "bidPriceLeg1,strikeLeg2,askPriceLeg2,breakEven,breakEvenPercent,maxProfit,"
    "maxLoss,maxProfitPercent,riskRewardRatio,impliedVolatilityRank1y,"
    "lossProbability,time,averageVolatility,baseNextEarningsDate,timeCode,"
    "dividendExDate,historicVolatility30d,impliedVolatilityRank1y,"
    "baseTrendSpotterSignal,baseTrendSpotterStrength,symbolCode,"
    "symbolType"
)


class VerticalSpreadsFields:
    def __init__(self):
        self.bull_call_spreads_fields = {
            "endpoint": "options/bull-calls-spread",
            "symbol_param": "baseSymbol",
            "fields": BULL_CALL_SPREADS_FIELDS,
            "orderBy": "strikeLeg1",
            "orderDir": "asc",
            "expirationDate": "Example: 2025-06-27",
            "expirationType": "weekly",
            "between(abs(deltaLeg1),0.3,)": "",
            "between(abs(deltaLeg2),0.1,)": "",
            "between(riskRewardRatio,0.33,1.5)": "",
            "meta": "expirations,field.shortName,field.type,field.description",
            "raw": 1,
        }
        self.bear_call_spreads_fields = {
            "endpoint": "options/bear-calls-spread",
            "symbol_param": "baseSymbol",
            "fields": BEAR_CALL_SPREADS_FIELDS,
            "orderBy": "strikeLeg1",
            "orderDir": "desc",
            "expirationDate": "Example: 2025-06-27",
            "expirationType": "weekly",
            "between(abs(deltaLeg1),0,0.6)": "",
            "between(abs(deltaLeg2),,0.3)": "",
            "between(riskRewardRatio,2,5)": "",
            "meta": "expirations,field.shortName,field.type,field.description",
            "raw": 1,
        }
        self.bear_put_spreads_fields = {
            "endpoint": "options/bear-puts-spread",
            "symbol_param": "baseSymbol",
            "fields": BEAR_PUT_SPREADS_FIELDS,
            "orderBy": "strikeLeg1",
            "orderDir": "desc",
            "expirationDate": "Example: 2025-06-27",
            "expirationType": "weekly",
            "between(abs(deltaLeg1),0.3,)": "",
            "between(abs(deltaLeg2),0.1,)": "",
            "between(riskRewardRatio,0.33,1.5)": "",
            "meta": "expirations,field.shortName,field.type,field.description",
            "raw": 1,
        }

        self.bull_put_spreads_fields = {
            "endpoint": "options/bull-puts-spread",
            "symbol_param": "baseSymbol",
            "fields": BULL_PUT_SPREADS_FIELDS,
            "orderBy": "strikeLeg1",
            "orderDir": "asc",
            "expirationDate": "Example: 2025-06-27",
            "expirationType": "weekly",
            "between(abs(deltaLeg1),,0.6)": "",
            "between(abs(deltaLeg2),0,0.3)": "",
            "between(riskRewardRatio,2,5)": "",
            "meta": "expirations,field.shortName,field.type,field.description",
            "raw": 1,
        }
