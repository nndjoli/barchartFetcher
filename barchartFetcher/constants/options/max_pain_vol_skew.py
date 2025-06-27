# Max Pain/ Vol Skew Fields:
MAX_PAIN_VOL_SKEW_FIELDS = (
    "symbol,strikePrice,optionType,baseLastPrice,openInterest,volume,volatility,"
    "daysToExpiration,expirationDate,tradeTime.format(m/d/y)"
)


class MaxPainVolSkewFields:
    def __init__(self):
        self.max_pain_vol_skew_fields = {
            "endpoint": "options",
            "symbol_param": "symbols",
            "raw": 1,
            "fields": MAX_PAIN_VOL_SKEW_FIELDS,
            "expirations": "Example: 2025-06-27,2025-07-03,2025-07-11",
            "groupBy": "expirationDate",
            "le(nearestToLast,40)": "",
        }
