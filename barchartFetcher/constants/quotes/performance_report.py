# Past 5d Performance Fields:
PAST_5D_FIELDS = (
    "date1dAgo,open1dAgo,high1dAgo,low1dAgo,lastPrice1dAgo,priceChange1dAgo,"
    "percentChange1dAgo,volume1dAgo,date2dAgo,open2dAgo,high2dAgo,low2dAgo,"
    "lastPrice2dAgo,priceChange2dAgo,percentChange2dAgo,volume2dAgo,date3dAgo,"
    "open3dAgo,high3dAgo,low3dAgo,lastPrice3dAgo,priceChange3dAgo,"
    "percentChange3dAgo,volume3dAgo,date4dAgo,open4dAgo,high4dAgo,low4dAgo,"
    "lastPrice4dAgo,priceChange4dAgo,percentChange4dAgo,volume4dAgo,date5dAgo,"
    "open5dAgo,high5dAgo,low5dAgo,lastPrice5dAgo,priceChange5dAgo,"
    "percentChange5dAgo,volume5dAgo"
)

# Past 5w Performance Fields:
PAST_5W_FIELDS = (
    "weeklyDate1wAgo,weeklyOpen1wAgo,weeklyHigh1wAgo,weeklyLow1wAgo,"
    "weeklyLastPrice1wAgo,weeklyPriceChange1wAgo,weeklyPercentChange1wAgo,"
    "weeklyVolume1wAgo,weeklyDate2wAgo,weeklyOpen2wAgo,weeklyHigh2wAgo,"
    "weeklyLow2wAgo,weeklyLastPrice2wAgo,weeklyPriceChange2wAgo,"
    "weeklyPercentChange2wAgo,weeklyVolume2wAgo,weeklyDate3wAgo,weeklyOpen3wAgo,"
    "weeklyHigh3wAgo,weeklyLow3wAgo,weeklyLastPrice3wAgo,weeklyPriceChange3wAgo,"
    "weeklyPercentChange3wAgo,weeklyVolume3wAgo,weeklyDate4wAgo,weeklyOpen4wAgo,"
    "weeklyHigh4wAgo,weeklyLow4wAgo,weeklyLastPrice4wAgo,weeklyPriceChange4wAgo,"
    "weeklyPercentChange4wAgo,weeklyVolume4wAgo,weeklyDate5wAgo,weeklyOpen5wAgo,"
    "weeklyHigh5wAgo,weeklyLow5wAgo,weeklyLastPrice5wAgo,weeklyPriceChange5wAgo,"
    "weeklyPercentChange5wAgo,weeklyVolume5wAgo"
)

# Past 5m Performance Fields:
PAST_5M_FIELDS = (
    "monthlyDate1mAgo,monthlyOpen1mAgo,monthlyHigh1mAgo,monthlyLow1mAgo,"
    "monthlyLastPrice1mAgo,monthlyPriceChange1mAgo,monthlyPercentChange1mAgo,"
    "monthlyVolume1mAgo,monthlyDate2mAgo,monthlyOpen2mAgo,monthlyHigh2mAgo,"
    "monthlyLow2mAgo,monthlyLastPrice2mAgo,monthlyPriceChange2mAgo,"
    "monthlyPercentChange2mAgo,monthlyVolume2mAgo,monthlyDate3mAgo,"
    "monthlyOpen3mAgo,monthlyHigh3mAgo,monthlyLow3mAgo,monthlyLastPrice3mAgo,"
    "monthlyPriceChange3mAgo,monthlyPercentChange3mAgo,monthlyVolume3mAgo,"
    "monthlyDate4mAgo,monthlyOpen4mAgo,monthlyHigh4mAgo,monthlyLow4mAgo,"
    "monthlyLastPrice4mAgo,monthlyPriceChange4mAgo,monthlyPercentChange4mAgo,"
    "monthlyVolume4mAgo,monthlyDate5mAgo,monthlyOpen5mAgo,monthlyHigh5mAgo,"
    "monthlyLow5mAgo,monthlyLastPrice5mAgo,monthlyPriceChange5mAgo,"
    "monthlyPercentChange5mAgo,monthlyVolume5mAgo"
)

# Price Performance Fields:
PRICE_PERFORMANCE_FIELDS = (
    "lastPrice,percentChange5d,lowPrice5d,highPrice5d,lastPrice,percentChange1m,"
    "lowPrice1m,highPrice1m,lastPrice,percentChange3m,lowPrice3m,highPrice3m,"
    "lastPrice,percentChange6m,lowPrice6m,highPrice6m,lastPrice,"
    "percentChangeYtd,lowPriceYtd,highPriceYtd,lastPrice,percentChange1y,"
    "lowPrice1y,highPrice1y,lastPrice,percentChange3y,lowPrice3y,highPrice3y,"
    "lastPrice,percentChange5y,lowPrice5y,highPrice5y,lastPrice,"
    "percentChange10y,lowPrice10y,highPrice10y"
)

# Performance Lows and Highs Fields:
HIGHS_AND_LOWS_FIELDS = (
    "highHits1m,highPercent1m,lowHits1m,lowPercent1m,highHits3m,highPercent3m,"
    "lowHits3m,lowPercent3m,highHits6m,highPercent6m,lowHits6m,lowPercent6m,"
    "highHitsYtd,highPercentYtd,lowHitsYtd,lowPercentYtd,highHits1y,"
    "highPercent1y,lowHits1y,lowPercent1y,highHits3y,highPercent3y,lowHits3y,"
    "lowPercent3y,highHits5y,highPercent5y,lowHits5y,lowPercent5y,highHits10y,"
    "highPercent10y,lowHits10y,lowPercent10y"
)


class PerformanceReportFields:
    def __init__(self):
        self.past_5d_fields = {
            "endpoint": "quote",
            "symbol_param": "symbols",
            "fields": PAST_5D_FIELDS,
            "meta": "field.shortName,field.description,field.type",
            "raw": 1,
        }
        self.past_5w_fields = {
            "endpoint": "quote",
            "symbol_param": "symbols",
            "fields": PAST_5W_FIELDS,
            "meta": "field.shortName,field.description,field.type",
            "raw": 1,
        }
        self.past_5m_fields = {
            "endpoint": "quote",
            "symbol_param": "symbols",
            "fields": PAST_5M_FIELDS,
            "meta": "field.shortName,field.description,field.type",
            "raw": 1,
        }
        self.price_perf_fields = {
            "endpoint": "quote",
            "symbol_param": "symbols",
            "fields": PRICE_PERFORMANCE_FIELDS,
            "meta": "field.shortName,field.description,field.type",
            "raw": 1,
        }
        self.lows_highs_fields = {
            "endpoint": "quote",
            "symbol_param": "symbols",
            "fields": HIGHS_AND_LOWS_FIELDS,
            "meta": "field.shortName,field.description,field.type",
            "raw": 1,
        }
