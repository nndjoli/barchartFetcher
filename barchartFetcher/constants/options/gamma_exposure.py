# GEX Fields:
GAMMA_EXPOSURE_FIELDS = (
    "fields=symbol,strikePrice,"
    "optionType,baseDailyLastPrice,baseLastPrice,dailyGamma,"
    "gamma,delta,dailyDelta,dailyOpenInterest,openInterest,dailyVolume,"
    "volume,daysToExpiration,expirationDate,averageVolatility,"
    "&expirations=OPTIONS_EXPIRATIONS_FIELDS&le(nearestToLast,100)="
)


class GEXFields:
    def __init__(self):

        self.gamma_exposure_fields = GAMMA_EXPOSURE_FIELDS
        self.gamma_exposure_endpoint = "options"
        self.gamma_exposure_requires = print(
            "Need to replace OPTIONS_EXPIRATIONS_FIELDS by the queried symbol options expiraitons.\n"
            "options_expirations_url = options_expirations_endpt + f'symbols=symbol&fields={options_expirations_fields}&raw=1\n"
            "options_expirations = QueryManager().sync_query(options_expirations_url)\n"
            "...turn options_expirations into a list of dates."
            "(','.join(options_expirations))"
        )
