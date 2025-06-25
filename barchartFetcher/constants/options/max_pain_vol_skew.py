# Max Pain/ Vol Skew Fields:
MAX_PAIN_VOL_SKEW_FIELDS = (
    "symbol,strikePrice,optionType,baseLastPrice,openInterest,volume,"
    "volatility,daysToExpiration,expirationDate,tradeTime.format(m/d/y)"
    "&expirations=OPTIONS_EXPIRATIONS_FIELDS&le(nearestToLast,40)="
)


class MaxPainVolSkewFields:
    def __init__(self):
        self.max_pain_vol_skew_fields = MAX_PAIN_VOL_SKEW_FIELDS
        self.max_pain_vol_skew_endpoint = "options"
        self.max_pain_vol_skew_requires = print(
            "Need to replace OPTIONS_EXPIRATIONS_FIELDS by the queried symbol options expirations dates.\n"
            "options_expirations_url = options_expirations_endpt + f'symbols=symbol&fields={options_expirations_fields}&raw=1\n"
            "options_expirations = QueryManager().sync_query(options_expirations_url)\n"
            "...turn options_expirations into a list of dates."
            "(','.join(options_expirations))"
        )
