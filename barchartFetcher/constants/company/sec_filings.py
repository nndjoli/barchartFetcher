SEC_FILINGS_FIELDS = (
    "date,formName,description,htmlUrl,wordUrl,pdfUrl,excelUrl"
)


class SECFilingsFields:
    def __init__(self):
        self.sec_filings_fields = {
            "endpoint": "sec_filings",
            "symbol_param": "symbol",
            "fields": SEC_FILINGS_FIELDS,
            "transactions": "1",
            "limit": "20",
        }
