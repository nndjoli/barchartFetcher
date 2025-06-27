# Put Call Ratio Fields
PUT_CALL_RATIOS_FIELDS = (
    "expirationDate,expirationType,daysToExpiration,putVolume,callVolume,"
    "totalVolume,putCallVolumeRatio,putOpenInterest,callOpenInterest,"
    "totalOpenInterest,putCallOpenInterestRatio,averageVolatility,symbolCode,"
    "symbolType,lastPrice,dailyLastPrice"
)

# Put Call Ratio Historical Fields
PUT_CALL_RATIOS_HISTORICAL_FIELDS = (
    "putCallVolumeRatio,putCallOpenInterestRatio,date"
)


class PutCallRatioSFields:
    def __init__(self):
        self.put_call_ratio_fields = {
            "endpoint": "options_expirations",
            "symbol_param": "symbol",
            "fields": PUT_CALL_RATIOS_FIELDS,
            "meta": "field.shortName,field.description,field.type",
            "raw": 1,
            "page": 1,
            "limit": 100,
        }
        self.put_call_ratio_historical_fields = {
            "endpoint": "options_historical",
            "symbol_param": "symbol",
            "fields": PUT_CALL_RATIOS_HISTORICAL_FIELDS,
            "limit": 200,
            "orderBy": "date",
            "orderDir": "desc",
        }
