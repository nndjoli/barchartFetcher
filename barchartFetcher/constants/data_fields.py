from barchartFetcher.utils.query_manager import QueryManager

DATA_FIELDS = QueryManager().sync_query(
    url="https://www.barchart.com/education/data-fields/load-fields",
    output_format="json",
    method="POST",
)
