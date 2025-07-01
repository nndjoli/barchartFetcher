from barchartFetcher.utils.query_async_dicts import make_async_dicts
from barchartFetcher.utils.query_manager import QueryManager
from barchartFetcher.utils.sync_query_functions.options import (
    options_expirations,
)


class Symbol:
    def __init__(self, symbol: str):
        self.symbol = symbol
        self.__qm__ = QueryManager()
        self.__oe__ = None
        self.__oe_str__ = None

        try:
            self.__oe__ = options_expirations(
                self.__qm__, symbols=symbol, raw=1
            )
            self.__oe_str__ = ",".join(
                [x["raw"]["expirationDate"] for x in self.__oe__["data"]]
            )

        except Exception:
            self.__oe__ = None
            self.__oe_str__ = ""

        self.__ad__ = make_async_dicts(self.symbol, self.__oe_str__)

    def financials(self):
        return self.__qm__.async_queries(self.__ad__["financials"])

    def analysts(self):
        return self.__qm__.async_queries(self.__ad__["analysts"])

    def company(self):
        return self.__qm__.async_queries(self.__ad__["company"])

    def technicals(self):
        return self.__qm__.async_queries(self.__ad__["technicals"])

    def quotes(self):
        return self.__qm__.async_queries(self.__ad__["quotes"])

    def options(self):
        return self.__qm__.async_queries(self.__ad__["options"])

    def options_strategies_long(self):
        return self.__qm__.async_queries(
            self.__ad__["options_strategies_long"]
        )

    def options_strategies_vertical_spreads(self):
        return self.__qm__.async_queries(
            self.__ad__["options_strategies_vertical_spreads"]
        )

    def options_strategies_protection(self):
        return self.__qm__.async_queries(
            self.__ad__["options_strategies_protection"]
        )

    def options_strategies_straddles_and_strangles(self):
        return self.__qm__.async_queries(
            self.__ad__["options_strategies_straddles_and_strangles"]
        )

    def options_strategies_horizontal_spreads(self):
        return self.__qm__.async_queries(
            self.__ad__["options_strategies_horizontal_spreads"]
        )

    def options_strategies_butterfly_spreads(self):
        return self.__qm__.async_queries(
            self.__ad__["options_strategies_butterfly_spreads"]
        )

    def options_strategies_condor(self):
        return self.__qm__.async_queries(
            self.__ad__["options_strategies_condor"]
        )

    def options_strategies_covered_calls_and_naked_puts(self):
        return self.__qm__.async_queries(
            self.__ad__["options_strategies_covered_calls_and_naked_puts"]
        )
