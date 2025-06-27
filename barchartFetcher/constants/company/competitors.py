# Sector Competitors Fields
SECTOR_COMPETITORS_FIELDS = (
    "weightedAlpha,lastPrice,priceChange,percentChange,highPrice1y,"
    "lowPrice1y,percentChange1y,tradeTime,symbolCode,symbolType,"
    "hasOptions"
)


class SectorCompetitorsFields:
    def __init__(self):
        self.sector_competitors_fields = {
            "endpoint": "quote",
            "symbol_param": "symbol",
            "lists": "stocks.inSector.all(<sector_symbol_from_key_statistics>)",
            "fields": SECTOR_COMPETITORS_FIELDS,
            "orderBy": "weightedAlpha",
            "orderDir": "desc",
            "meta": "field.shortName,field.type,field.description,lists.lastUpdate",
            "hasOptions": "true",
            "page": 1,
            "limit": 100,
            "raw": 1,
        }
