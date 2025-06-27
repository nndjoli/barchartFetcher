# Options Prices Fields
OPTIONS_PRICES_FIELDS = (
    "symbol,baseSymbol,strikePrice,expirationDate,moneyness,bidPrice,midpoint,"
    "askPrice,lastPrice,priceChange,percentChange,volume,openInterest,"
    "openInterestChange,delta,volatility,optionType,daysToExpiration,tradeTime,"
    "averageVolatility,historicVolatility30d,baseNextEarningsDate,dividendExDate,"
    "baseTimeCode,impliedVolatilityRank1y,symbolCode,symbolType,theoretical,gamma,"
    "theta,vega,rho,volumeOpenInterestRatio,itmProbabilityexpirationType,expiration,"
    "dte,bidXSize,askXSize,tradePrice,tradeSize,side,premium,tradeCondition,label,"
    "baseSymbolType"
)


class OptionsPricesFields:
    def __init__(self):
        self.options_prices_fields = {
            "endpoint": "options",
            "symbol_param": "baseSymbol",
            "fields": OPTIONS_PRICES_FIELDS,
            "groupBy": "optionType",
            "expirationDate": "nearest",
            "meta": "field.shortName,field.description,field.type",
            "orderBy": "strikePrice",
            "orderDir": "asc",
            "optionsOverview": "true",
            "raw": 1,
        }
