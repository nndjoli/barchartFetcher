from dataclasses import dataclass
from typing import Any
from urllib.parse import quote

from barchartFetcher import constants

query_endpoints = constants.QueryEndpoints()
query_fields_classes = constants.fields_classes_mapping


def build_tasks_dict(symbol, fields_class):
    attributes = {}

    for x in dir(query_fields_classes[fields_class]):
        if x.endswith("fields"):
            attribute = x
            attributes[attribute.replace("_fields", "")] = getattr(
                query_fields_classes[fields_class], x
            )

    tasks = {}

    for attribute, fields in attributes.items():
        attribute_url = ""

        endpoint = getattr(query_endpoints, fields["endpoint"])
        attribute_url += endpoint

        symbol_param = fields["symbol_param"]

        if symbol_param != "eq(symbol,<symbol>)":
            attribute_url += f"{symbol_param}={symbol}"
        else:
            fields.pop("eq(symbol,<symbol>)", None)
            attribute_url += f"eq(symbol,{symbol})="

        for field in fields:
            if field not in [
                "endpoint",
                "symbol_param",
            ]:
                attribute_url += f"&{field}={fields[field]}"

        tasks[attribute] = {
            "url": quote(attribute_url, safe=":/?&="),
            "output_format": "json",
        }

    return tasks


def build_all_tasks_dicts(symbol):
    all_tasks_dicts = {}
    for key, value in query_fields_classes.items():
        tasks = build_tasks_dict(symbol, key)
        all_tasks_dicts[key] = tasks
    return all_tasks_dicts


@dataclass
class QueryTasksDicts:
    analyst_ratings: Any = None
    butterfly_spreads: Any = None
    condor: Any = None
    covered_calls: Any = None
    earnings_estimates: Any = None
    expected_move: Any = None
    expirations: Any = None
    financial_summary: Any = None
    gex: Any = None
    horizontal_spreads: Any = None
    insider_trades: Any = None
    key_statistics: Any = None
    long_call_put: Any = None
    max_pain_vol_skew: Any = None
    naked_puts: Any = None
    opinion: Any = None
    options_flow: Any = None
    options_prices: Any = None
    overview: Any = None
    performance_report: Any = None
    protection_strategies: Any = None
    put_call_ratios: Any = None
    sec_filings: Any = None
    sector_competitors: Any = None
    straddles_strangles: Any = None
    technical_analysis: Any = None
    vertical_spreads: Any = None
    volatility_charts: Any = None

    def __init__(self, symbol):
        self.symbol = symbol

        tasks_dicts = build_all_tasks_dicts(symbol)

        for key, value in tasks_dicts.items():
            setattr(self, key, value)
