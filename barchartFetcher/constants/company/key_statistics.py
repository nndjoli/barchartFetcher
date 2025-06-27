# Company Infos Fields
COMPANY_INFORMATIONS_FIELDS = (
    "symbolShortName,address,country,website,"
    "numberOfEmployees,phoneNumber,symbolDescription,exchange,industryGroup,"
    "industry,sicSymbol,sicDescription,sectors,tradeTime,hasOptions,"
    "hasWeeklyOptions,openPrice,highPrice,lowPrice,lastPrice,priceChange,"
    "percentChange"
)

# Company Overview Fields
OVERVIEW_FIELDS = (
    "marketCap,enterpriseValue,sharesOutstanding,annualSales,annualNetIncome,"
    "lastQuarterSales,lastQuarterIncome,ebit,ebitda,beta,percentInsider,"
    "percentInstitutional,float,floatPercentage,shortVolumeRatio"
)

# Company Growth Fields
GROWTH_FIELDS = (
    "percentChange1y, percentChange3y, percentChange5y,revenueGrowth5y,"
    "earningsGrowth5y,dividendGrowth5y"
)
# Per Share Information Fields
PER_SHARE_INFORMATION_FIELDS = (
    "earnings,epsDate,nextEarningsDate,epsAnnual,epsGrowthQuarter,epsGrowthYear,"
    "dividendRate,dividendYield,dividend,dividendDate,dividendExDate,"
    "paymentDate,dividendPayout,split,splitDate"
)

# Ratios FIelds
RATIOS_FIELDS = (
    "peRatioTrailing,peRatioForward,pegRatio,returnOnEquity,returnOnAssets,"
    "profitMargin,debtEquity,priceSales,priceCashFlow,priceBook,bookValue,"
    "interestCoverage"
)


class KeyStatisticsFields:
    def __init__(self):
        self.company_informations_fields = {
            "endpoint": "quote",
            "symbol_param": "symbols",
            "fields": COMPANY_INFORMATIONS_FIELDS,
            "meta": "field.shortName,field.type,field.description",
            "raw": 1,
        }
        self.overview_fields = {
            "endpoint": "quote",
            "symbol_param": "symbols",
            "fields": OVERVIEW_FIELDS,
            "meta": "field.shortName,field.type,field.description",
            "raw": 1,
        }
        self.growth_fields = {
            "endpoint": "quote",
            "symbol_param": "symbols",
            "fields": GROWTH_FIELDS,
            "meta": "field.shortName,field.type,field.description",
            "raw": 1,
        }

        self.per_share_information_fields = {
            "endpoint": "quote",
            "symbol_param": "symbols",
            "fields": PER_SHARE_INFORMATION_FIELDS,
            "meta": "field.shortName,field.type,field.description",
            "raw": 1,
        }
        self.ratios_fields = {
            "endpoint": "quote",
            "symbol_param": "symbols",
            "fields": RATIOS_FIELDS,
            "meta": "field.shortName,field.type,field.description",
            "raw": 1,
        }
