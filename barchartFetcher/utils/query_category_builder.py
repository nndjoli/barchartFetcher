from barchartFetcher.constants.query_endpoints import QueryEndpoints


def query_category(
    QueryManager, category: str, symbols: str, query_strings_dict: dict
):
    """
    Function to query a specific category with the given symbols.
    """
    if category not in query_strings_dict:
        raise ValueError(
            f"Category '{category}' not found in query strings dictionary. Must be one of {list(query_strings_dict.keys())}."
        )

    qe = QueryEndpoints()

    tasks_dict = {}

    category_content = query_strings_dict[category]
    category_content_type = type(category_content)

    if category_content_type is str:
        tasks_dict[category] = {
            "url": qe.quote
            + f"symbols={symbols}&fields=symbol,"
            + category_content
            + "&raw=1&meta=field.name,field.type,field.description",
            "output_format": "json",
        }

    elif category_content_type is dict:
        for subcategory, fields in category_content.items():
            tasks_dict[subcategory] = {
                "url": qe.quote
                + f"symbols={symbols}&fields=symbol,"
                + fields
                + "&raw=1&meta=field.name,field.type,field.description",
                "output_format": "json",
            }

    res = QueryManager.async_queries(tasks_dict)

    return res


class QueryCategoryBuilder:
    """
    Class to build queries for a specific category.
    """

    def __init__(self, QueryManager, query_strings_dict: dict):

        self.qm = QueryManager
        self.query_strings_dict = query_strings_dict
        self.categories = list(query_strings_dict.keys())

    def get(self, category: str, symbols: str):
        if category not in self.categories:
            raise ValueError(
                f"Category '{category}' not found. Must be one of {self.categories}."
            )
        return query_category(
            self.qm, category, symbols, self.query_strings_dict
        )
