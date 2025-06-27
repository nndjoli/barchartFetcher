# Insider trades fields
INSIDER_TRADES_FIELDS = (
    "fullName,shortJobTitle,transactionType,transactionDate,"
    "amount,reportedPrice,usdValue,eodHolding,eodHoldingPercentage,symbolCode,"
    "hasOptions,symbolType,lastPrice,dailyLastPrice"
)


class InsiderTradesFields:
    def __init__(self):
        self.insider_trades_fields = {
            "endpoint": "insider_trades",
            "symbol_param": "eq(symbol|<symbol>)",
            "eq(symbol|<symbol>)": "",
            "orderBy": "transactionDate",
            "orderDir": "desc",
            "meta": "field.shortName,field.type,field.description",
            "page": 1,
            "limit": 100,
            "raw": 1,
        }
