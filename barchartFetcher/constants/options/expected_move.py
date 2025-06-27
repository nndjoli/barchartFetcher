# Expected Move Fields
EXPECTED_MOVE_FIELDS = (
    "expirationDate,expirationType,daysToExpiration,baseLastPrice,impliedMove,"
    "impliedMovePercent,baseUpperPrice,baseLowerPrice,averageVolatility,"
    "baseNextEarningsDate,baseTimeCode,symbolCode,symbolType"
)

# Earnings Fields
EARNINGS_FIELDS = "tradeTime.format(Y-m-d),value,event"


class ExpectedMoveFields:
    def __init__(self):
        self.expected_move_fields = {
            "endpoint": "options-expirations",
            "symbol_param": "symbol",
            "fields": EXPECTED_MOVE_FIELDS,
            "orderBy": "expirationDate",
            "orderDir": "asc",
            "meta": "field.shortName,field.description,field.type",
            "raw": 1,
            "page": 1,
            "limit": 100,
        }
        self.earnings_fields = {
            "endpoint": "historical",
            "symbol_param": "symbol",
            "fields": EARNINGS_FIELDS,
            "type": "events",
            "events": "earnings",
        }
