# Expected Move Fields
EXPECTED_MOVE_FIELDS = (
    "expirationDate,expirationType,daysToExpiration,"
    "baseLastPrice,impliedMove,impliedMovePercent,"
    "baseUpperPrice,baseLowerPrice,averageVolatility,"
    "baseNextEarningsDate,baseTimeCode,symbolCode,"
    "symbolType"
)

# Earnings Fields
EARNINGS_FIELDS = "tradeTime.format(Y-m-d),value,event"


class ExpectedMoveFields:
    def __init__(self):
        self.expected_move_fields = EXPECTED_MOVE_FIELDS
        self.earnings_fields = EARNINGS_FIELDS
