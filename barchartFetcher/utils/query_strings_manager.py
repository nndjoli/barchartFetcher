def build_query_string_dictionary(complete_dataframe):
    query_strings_dict = {}

    fields_dataframe = complete_dataframe
    categories = fields_dataframe["category"].unique()

    for category in categories:

        if category not in query_strings_dict:
            query_strings_dict[category] = {}

        category_fields_dataframe = fields_dataframe[fields_dataframe["category"] == category]
        subcategories = category_fields_dataframe["subcategory"].unique()

        for subcategory in subcategories:

            if subcategory not in query_strings_dict[category]:

                query_strings_dict[category][subcategory] = ""

            subcategory_fields_dataframe = category_fields_dataframe[category_fields_dataframe["subcategory"] == subcategory]
            subcategory_fields_list = subcategory_fields_dataframe["apiField"].tolist()
            subcategory_fields_string = ",".join(subcategory_fields_list)

            query_strings_dict[category][subcategory] = subcategory_fields_string

    for category, subcategories in query_strings_dict.items():
        if len(subcategories.keys()) == 1:
            query_strings_dict[category] = list(subcategories.values())[0]
    return query_strings_dict


class QueryStringsManager:
    def __init__(self, complete_dataframe):
        self.complete_dataframe = complete_dataframe
        """Complete DataFrame with all fields."""
        self.query_strings_dict = build_query_string_dictionary(complete_dataframe)
        """Dictionary with query strings for each category and subcategory."""
