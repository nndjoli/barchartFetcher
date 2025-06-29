import os

import pandas as pd

from barchartFetcher.utils.query_manager import QueryManager

FIELDS_GROUPS = {
    "informations": ["general_symbol_information"],
    "quotes": [
        "general_symbol_information",
        "current_day_prices",
        "prior_day_prices",
        "pre_market_prices",
        "post_market_prices",
        "volume",
        "percent_change",
        "price_change",
        "percent_from_average",
        "average_volume",
        "performance_vs_market",
    ],
    "technicals": [
        "gaps_and_range_changes",
        "support_and_resistance",
        "moving_average",
        "raw_stochastic",
        "stochastic_percent_k",
        "stochastic_percent_d",
        "average_true_range",
        "average_directional_index",
        "positive_directional_index",
        "negative_directional_index",
        "relative_strength",
        "percent_r",
        "historic_volatility",
        "macd_oscillator",
        "standard_deviation",
        "other_technicals",
    ],
    "sentiment": [
        "overall_opinion",
        "trend_seeker",
        "short_term_indicators",
        "medium_term_indicators",
        "long_term_indicators",
        "legacy_indicators",
    ],
    "highs_and_lows": [
        "5d_highs_lows",
        "1mo_highs_lows",
        "3mo_highs_lows",
        "6mo_highs_lows",
        "ytd_highs_lows",
        "52w_highs_lows",
        "2yr_highs_lows",
        "3yr_highs_lows",
        "5yr_highs_lows",
        "10yr_highs_lows",
        "20yr_highs_lows",
        "all_time_highs_lows",
    ],
    "fundamentals": [
        "key_statistics",
        "earnings",
        "dividends_and_splits",
        "financial_ratios",
        "analysts_and_estimates",
        "income_statement_yearly_data",
        "income_statement_quarterly_data",
        "balance_sheet_yearly_data",
        "balance_sheet_quarterly_data",
        "cash_flow_yearly_data",
        "cash_flow_quarterly_data",
    ],
    "options": [
        # Overview
        "options_overview_implied_volatility",
        "options_overview_iv_rank",
        "options_overview_iv_change",
        "options_overview_iv_percentile",
        "options_overview_implied_volatility_highs",
        "options_overview_implied_volatility_lows",
        "options_overview_total_options_volume",
        "options_overview_total_options_volume_percent_change",
        "options_overview_put_total_volume",
        "options_overview_call_total_volume",
        "options_overview_put_call_total_volume_ratio",
        "options_overview_total_options_open_interest",
        "options_overview_total_options_open_interest_percent_change",
        "options_overview_total_put_open_interest",
        "options_overview_total_call_open_interest",
        "options_overview_total_put_call_open_interest_ratio",
        "options_overview_total_volume_open_interest_ratio",
        # Strikes
        "options_strikes_option_info",
        "options_strikes_covered_call",
        "options_strikes_options_analysis",
        "options_strikes_strike_volatility",
        "options_strikes_break_even",
        "options_strikes_greeks",
        "options_strikes_greek_ratios",
        "options_strikes_probability",
        "options_strikes_percent_of_stock",
        "options_strikes_time_premium",
        "options_strikes_yield_to_strike",
        "options_strikes_potential_return",
        "options_strikes_strike_to_standard_deviation",
        "options_strikes_options_flow",
    ],
    "etfs": ["etfs"],
    "futures": ["futures"],
    "portfolio": ["portfolio"],
    "investor_portfolio": ["investor_portfolio"],
    "others": [],
}

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_PATH = f"{CURRENT_DIR}/data_fields_static.json"


def fetch_data_fields(query_manager: QueryManager):
    # Data fields Query Parameters:
    method = "POST"
    output_format = "json"
    raw_data_fields_url = (
        "https://www.barchart.com/education/data-fields/load-fields"
    )

    # Fetching data fields
    data_fields = query_manager.sync_query(
        url=raw_data_fields_url, output_format=output_format, method=method
    )

    return data_fields


def build_mapping(response):
    data_fields = response.get("data", {})
    data_fields_names = list(data_fields.keys())

    names_mapping = {}

    for name in data_fields_names:
        original_name = name
        names_mapping[original_name] = ""

        if name.startswith("-"):
            name = name.replace("-", "Negative ")

        elif name.startswith("+"):
            name = name.replace("+", "Positive ")

        to_replace_by_underscore = [" → ", "-", " ", "/"]
        for char in to_replace_by_underscore:
            name = name.replace(char, "_")

        name = name.replace("%", "percent_")
        name = name.replace("(", "").replace(")", "")
        name = name.replace("&", "and")
        name = name.replace("Equities_and_ETFs_", "")

        if "Day" in name:
            for i in range(1, 10):
                name = name.replace(f"{i}_Day", f"{i}d")

        name = name.replace("_Week", "w")
        name = name.replace("_Month", "mo").replace("_Year_", "yr_")
        name = name.replace("_Data_Fields", "")
        name = name.lower()

        processed_name = name

        names_mapping[original_name] = processed_name

    return names_mapping


def apply_mapping(mapping, response):
    data_fields_renamed = {}
    for original_name, processed_name in mapping.items():
        data_fields_renamed[processed_name] = response["data"][original_name]
    return data_fields_renamed


def organize_fields(processed_response, FIELDS_GROUPS):
    categorized_response = {
        name for names in FIELDS_GROUPS.values() if names for name in names
    }

    all_fields = set(processed_response)

    organized_response = {
        category: {
            name: processed_response[name]
            for name in names
            if name in processed_response
        }
        for category, names in FIELDS_GROUPS.items()
        if category != "others"
    }

    unknown = all_fields - categorized_response
    organized_response["others"] = {
        name: processed_response[name] for name in unknown
    }

    return organized_response


def organize_fields_dfs(organized_response):
    def sub_to_df(sub):
        converted = {}
        for name, vals in sub.items():
            if not vals:
                continue
            try:
                df = (
                    pd.DataFrame(vals)
                    if len(vals) > 1
                    else pd.DataFrame([vals])
                )
                converted[name] = df
            except Exception as e:
                print(f"Error converting '{name}': {e}")
                converted[name] = vals
        return converted

    organized_fields = {
        category: sub_to_df(subs)
        for category, subs in organized_response.items()
        if sub_to_df(subs)
    }

    return organized_fields


def build_api_fields_df(organized_fields_dfs):
    frames = []
    for category, subs in organized_fields_dfs.items():
        for indicator, df in subs.items():
            if not isinstance(df, pd.DataFrame):
                try:
                    df = pd.DataFrame([df])
                except:
                    continue

            df = df.assign(category=category, subcategory=indicator)
            frames.append(df)

    all_fields_df = pd.concat(frames, ignore_index=True)
    all_fields_df = all_fields_df.dropna(subset=["apiField"])
    all_fields_df = all_fields_df.drop_duplicates(
        subset=["apiField", "category", "subcategory"]
    )

    return all_fields_df


def main(query_manager: QueryManager):
    response = fetch_data_fields(query_manager)
    mapping = build_mapping(response)
    processed_response = apply_mapping(mapping, response)
    organized_response = organize_fields(processed_response, FIELDS_GROUPS)
    organized_fields_dfs = organize_fields_dfs(organized_response)
    api_fields_df = build_api_fields_df(organized_fields_dfs)

    return {
        "dictionary": organized_response,
        "dataframes": organized_fields_dfs,
        "complete_dataframe": api_fields_df,
    }


class DataFieldsManager:
    def __init__(self, QueryManager: QueryManager):
        self.query_manager = QueryManager

        try:
            data = main(self.query_manager)

            self.dictionary = data["dictionary"]
            """Dictionary of data fields organized by categories and subcategories as dict."""
            self.dataframes = data["dataframes"]
            """Dictionary of data fields organized by categories and subcategories as DataFrames."""
            self.complete_dataframe = data["complete_dataframe"]
            """DataFrame of all data fields with their categories and subcategories."""

            # Save the complete dataframe to a static JSON file
            # Will overwrite itself every time the class is initialized
            # So that the static data is always as up to date as possible
            # You can uncomment the lines below to enable this functionality

            # if not os.path.exists(STATIC_PATH):
            #    os.makedirs(os.path.dirname(STATIC_PATH), exist_ok=True)

            # with open(STATIC_PATH, "w") as f:
            #    json.dump(data["complete_dataframe"].to_dict('records'), f, indent=4)

        except Exception as e:
            print("Error initializing DataFieldsManager:", e)
            print(
                f"Using static data fields (loaded from {STATIC_PATH}) instead."
            )

            # If the initialization fails, load the static data fields
            # If static update is not enabled, this will load the default static data
            # corresponding to today's date (2025-06-19)
            self.complete_dataframe = pd.read_json(
                STATIC_PATH, orient="records"
            )
            """DataFrame of all data fields with their categories and subcategories."""
