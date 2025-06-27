# Options Expirations Fields
EXPIRATIONS_FIELDS = (
    "callVolume,putVolume,putCallVolumeRatio,callOpenInterest,putOpenInterest,"
    "putCallOpenInterestRatio,expirationDate,expirationType"
)


class ExpirationsFields:
    def __init__(self):
        self.expirations_fields = {
            "endpoint": "options_expirations",
            "symbol_param": "symbols",
            "fields": EXPIRATIONS_FIELDS,
            "meta": "field.shortName,field.description,field.type",
            "raw": 1,
        }
