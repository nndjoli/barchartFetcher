ANALYST_RATINGS_FIELDS = (
    "exchange,symbolName,previousPrice,previousHighPrice,"
    "previousLowPrice,weeklyPreviousPrice,weeklyPreviousHighPrice,"
    "weeklyPreviousLowPrice,monthlyPreviousPrice,monthlyPreviousHighPrice,"
    "monthlyPreviousLowPrice,lastPrice,percentChange,priceChange,openPrice,lowPrice,"
    "highPrice,lowPrice1y,highPrice1y,highPrice1y,lowPrice1y,weightedAlpha,"
    "meanTargetEstimate,highTargetEstimate,lowTargetEstimate,averageRecommendation,"
    "totalRecommendations"
)


class AnalystRatingsFields:
    def __init__(self):
        self.analyst_ratings_fields = {
            "endpoint": "quotes",
            "symbol_param": "symbol",
            "fields": ANALYST_RATINGS_FIELDS,
            "meta": "field.shortName,field.type,field.description",
            "raw": 1,
        }
