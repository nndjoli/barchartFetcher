# Put Call Ratio Fields
PUT_CALL_RATIOS_FIELDS = (
    "expirationDate,expirationType,daysToExpiration,"
    "putVolume,callVolume,totalVolume,putCallVolumeRatio,"
    "putOpenInterest,callOpenInterest,totalOpenInterest,"
    "putCallOpenInterestRatio,averageVolatility,"
    "symbolCode,symbolType,lastPrice,dailyLastPrice"
)

# Put Call Ratio Historical Fields
PUT_CALL_RATIOS_HISTORICAL_FIELDS = (
    "putCallVolumeRatio,putCallOpenInterestRatio,date"
)


class PutCallRatioSFields:
    def __init__(self):
        self.put_call_ratio_fields = PUT_CALL_RATIOS_FIELDS
        self.put_call_ratio_historical_fields = (
            PUT_CALL_RATIOS_HISTORICAL_FIELDS
        )
