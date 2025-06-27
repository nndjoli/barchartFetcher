# GEX Fields:
GAMMA_EXPOSURE_FIELDS = (
    "symbol,strikePrice,optionType,baseDailyLastPrice,baseLastPrice,dailyGamma,"
    "gamma,delta,dailyDelta,dailyOpenInterest,openInterest,dailyVolume,volume,"
    "daysToExpiration,expirationDate,averageVolatility"
)


class GEXFields:
    def __init__(self):
        self.gamma_exposure_fields = {
            "endpoint": "options",
            "symbol_param": "symbols",
            "fields": GAMMA_EXPOSURE_FIELDS,
            "expirations": "Example: 2025-06-27,2025-07-03",
            "groupBy": "strikePrice",
            "le(nearestToLast,100)": "",
        }
