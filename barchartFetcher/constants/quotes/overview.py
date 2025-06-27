# Quote Fields
QUOTE_FIELDS = (
    "lowPrice,highPrice,openPrice,lastPrice,volume,averageVolume20d,"
    "stochasticK14d,weightedAlpha,priceChange5d,percentChange5d,rangePercent1y,"
    "highPrice1y,lowPrice1y"
)

# Fundamentals Fields
FUNDAMENTALS_FIELDS = (
    "marketCap,sharesOutstanding,annualSales,annualNetIncome,ebit,ebitda,beta,"
    "priceSales,priceCashFlow,priceBook,peRatioTrailing,epsAnnual,earnings,"
    "epsDate,nextEarningsDate,dividendRate,dividendYield,dividend,dividendDate,"
    "dividendExDate,industryGroup,sectors"
)

# Options Overview Fields
OPTIONS_OVERVIEW_FIELDS = (
    "optionsWeightedImpliedVolatility,optionsWeightedImpliedVolatilityChange,"
    "historicVolatility30d,optionsImpliedVolatilityPercentile1y,"
    "optionsImpliedVolatilityRank1y,optionsWeightedImpliedVolatilityHigh1y,"
    "optionsWeightedImpliedVolatilityHighDate1y,"
    "optionsWeightedImpliedVolatilityLow1y,"
    "optionsWeightedImpliedVolatilityLowDate1y,optionsPutCallVolumeRatio,"
    "optionsTotalVolume,optionsTotalVolume1m,optionsPutCallOpenInterestRatio,"
    "optionsTotalOpenInterest,optionsTotalOpenInterest1m"
)

# Analyst Rating and Earnings Estimates Fields
ANALYST_RATING_FIELDS = (
    "averageRecommendation,totalRecommendations,estimatedEarnings,"
    "estimatedEarnings1qAgo,highTargetEstimate,meanTargetEstimate,"
    "lowTargetEstimate"
)

# Price Performance Fields
PRICE_PERFORMANCE_FIELDS = (
    "highPrice1m,highDate1m,lowPrice1m,lowDate1m,priceChange1m,percentChange1m,"
    "highPrice3m,highDate3m,lowPrice3m,lowDate3m,priceChange3m,percentChange3m,"
    "highPrice1y,highDate1y,lowPrice1y,lowDate1y,priceChange1y,percentChange1y"
)

# Barchart Technical Opinion Fields
TECHNICAL_OPINION_FIELDS = "opinion,opinionSignal,opinionPercent,opinionStrength,opinionDirection,opinionChange"


class OverviewFields:
    def __init__(self):
        self.quote_fields = {
            "endpoint": "quote",
            "symbol_param": "symbols",
            "fields": QUOTE_FIELDS,
            "meta": "fields.shortName,fields.description,fields.type",
            "raw": 1,
        }
        self.fundamentals_fields = {
            "endpoint": "quote",
            "symbol_param": "symbols",
            "fields": FUNDAMENTALS_FIELDS,
            "meta": "fields.shortName,fields.description,fields.type",
            "raw": 1,
        }
        self.options_overview_fields = {
            "endpoint": "quote",
            "symbol_param": "symbols",
            "fields": OPTIONS_OVERVIEW_FIELDS,
            "meta": "fields.shortName,fields.description,fields.type",
            "raw": 1,
        }
        self.analyst_rating_fields = {
            "endpoint": "quote",
            "symbol_param": "symbols",
            "fields": ANALYST_RATING_FIELDS,
            "meta": "fields.shortName,fields.description,fields.type",
            "raw": 1,
        }
        self.price_performance_fields = {
            "endpoint": "quote",
            "symbol_param": "symbols",
            "fields": PRICE_PERFORMANCE_FIELDS,
            "meta": "fields.shortName,fields.description,fields.type",
            "raw": 1,
        }
        self.technical_opinion_fields = {
            "endpoint": "quote",
            "symbol_param": "symbols",
            "fields": TECHNICAL_OPINION_FIELDS,
            "meta": "fields.shortName,fields.description,fields.type",
            "raw": 1,
        }
