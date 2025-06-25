SEC_FILINGS_FIELDS = "date,formName,description,htmlUrl,wordUrl,pdfUrl,excelUrl&transactions=1"


class SECFilingsFields:
    def __init__(self):
        self.sec_filings_fields = SEC_FILINGS_FIELDS
        self.additional_infos = print(
            """
            Add symbol field via `symbol`;
            limit: 20 (default_value);
            """
        )
