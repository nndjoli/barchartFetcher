# Options Expirations Fields
EXPIRATIONS_FIELDS = (
    "callVolume,putVolume,putCallVolumeRatio,callOpenInterest,"
    "putOpenInterest,putCallOpenInterestRatio,expirationDate,"
    "expirationType"
)


class ExpirationsFields:

    def __init__(self):
        self.expirations_fields = EXPIRATIONS_FIELDS
