# Options Prices Fields
OPTIONS_PRICES_FIELDS = (
    "symbol,baseSymbol,strikePrice,expirationDate,moneyness,bidPrice,midpoint,askPrice,"
    "lastPrice,priceChange,percentChange,volume,openInterest,openInterestChange,delta,"
    "volatility,optionType,daysToExpiration,tradeTime,averageVolatility,historicVolatility30d,"
    "baseNextEarningsDate,dividendExDate,baseTimeCode,impliedVolatilityRank1y,symbolCode,"
    "symbolType,theoretical,gamma,theta,vega,rho,volumeOpenInterestRatio,itmProbability"
    "expirationType,expiration,dte,bidXSize,askXSize,tradePrice,tradeSize,side,premium,"
    "tradeCondition,label,baseSymbolType"
)


class OptionsPricesFields:
    def __init__(self):
        self.options_prices_fields = OPTIONS_PRICES_FIELDS
