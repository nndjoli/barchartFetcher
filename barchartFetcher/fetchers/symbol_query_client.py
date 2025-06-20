from barchartFetcher.utils.query_manager import (
    QueryManager,
)
from barchartFetcher.utils.query_category_builder import (
    QueryCategoryBuilder,
)
from barchartFetcher.utils.query_strings_manager import (
    QueryStringsManager,
)
from barchartFetcher.constants.data_fields_manager import (
    DataFieldsManager,
)

from dataclasses import dataclass
from typing import Dict, Any
import pandas as pd


class SymbolQueryClient:

    def __init__(self, symbols):

        self.symbols = symbols
        self.query_manager = QueryManager()
        self.data_fields_manager = DataFieldsManager(self.query_manager)
        self.query_strings_manager = QueryStringsManager(
            self.query_manager, self.data_fields_manager.complete_dataframe
        )
        self.query_category_builder = QueryCategoryBuilder(
            self.query_manager, self.query_strings_manager.query_strings_dict
        )

    @dataclass
    class __informations:

        symbolName: Any = None
        symbolShortName: Any = None
        exchange: Any = None
        industry: Any = None
        industryGroup: Any = None
        sicSymbol: Any = None
        sicDescription: Any = None
        numberOfEmployees: Any = None
        openInterest: Any = None
        tradeTime: Any = None
        hasOptions: Any = None
        hasWeeklyOptions: Any = None

        parent: Any = None
        symbols: str = None
        data: Dict[str, Any] = None

        def __init__(self, parent):
            self._parent = parent
            self.symbols = parent.symbols
            self.symbols = parent.symbols
            self.data = parent.query_category_builder.get(
                "informations", self.symbols
            )
            tempdf = pd.DataFrame(self.data["informations"]["data"])
            self.symbolName = tempdf["symbolName"].to_list()
            self.symbolShortName = tempdf["symbolShortName"].to_list()
            self.exchange = tempdf["exchange"].to_list()
            self.industry = tempdf["industry"].to_list()
            self.industryGroup = tempdf["industryGroup"].to_list()
            self.sicSymbol = tempdf["sicSymbol"].to_list()
            self.sicDescription = tempdf["sicDescription"].to_list()
            self.numberOfEmployees = tempdf["numberOfEmployees"].to_list()
            self.openInterest = tempdf["openInterest"].to_list()
            self.tradeTime = tempdf["tradeTime"].to_list()
            self.hasOptions = tempdf["hasOptions"].to_list()
            self.hasWeeklyOptions = tempdf["hasWeeklyOptions"].to_list()

    def Informations(self):
        return self.__informations(self)

    @dataclass
    class __quotes:

        general_symbol_information: Any = None
        current_day_prices: Any = None
        prior_day_prices: Any = None
        pre_market_prices: Any = None
        post_market_prices: Any = None
        volume: Any = None
        percent_change: Any = None
        price_change: Any = None
        percent_from_average: Any = None
        average_volume: Any = None
        performance_vs_market: Any = None

        parent: Any = None
        symbols: str = None
        data: Dict[str, Any] = None

        def __init__(self, parent):
            self._parent = parent
            self.symbols = parent.symbols
            self.symbols = parent.symbols
            self.data = parent.query_category_builder.get(
                "quotes", self.symbols
            )

            for key, value in self.data.items():
                setattr(self, key, value)

    def Quotes(self):
        return self.__quotes(self)

    @dataclass
    class __technicals:

        gaps_and_range_changes: Any = None
        support_and_resistance: Any = None
        moving_average: Any = None
        raw_stochastic: Any = None
        stochastic_percent_k: Any = None
        stochastic_percent_d: Any = None
        average_true_range: Any = None
        average_directional_index: Any = None
        positive_directional_index: Any = None
        negative_directional_index: Any = None
        relative_strength: Any = None
        percent_r: Any = None
        historic_volatility: Any = None
        macd_oscillator: Any = None
        standard_deviation: Any = None
        other_technicals: Any = None

        parent: Any = None
        symbols: str = None
        data: Dict[str, Any] = None

        def __init__(self, parent):
            self._parent = parent
            self.symbols = parent.symbols
            self.symbols = parent.symbols
            self.data = parent.query_category_builder.get(
                "technicals", self.symbols
            )

            for key, value in self.data.items():
                setattr(self, key, value)

    def Technicals(self):
        return self.__technicals(self)

    @dataclass
    class __sentiment:

        overall_opinion: Any = None
        trend_seeker: Any = None
        short_term_indicators: Any = None
        medium_term_indicators: Any = None
        long_term_indicators: Any = None
        legacy_indicators: Any = None

        parent: Any = None
        symbols: str = None
        data: Dict[str, Any] = None

        def __init__(self, parent):
            self._parent = parent
            self.symbols = parent.symbols
            self.symbols = parent.symbols
            self.data = parent.query_category_builder.get(
                "sentiment", self.symbols
            )

            for key, value in self.data.items():
                setattr(self, key, value)

    def Sentiment(self):
        return self.__sentiment(self)

    @dataclass
    class __highs_and_lows:

        highs_lows_5d: Any = None
        highs_lows_1mo: Any = None
        highs_lows_3mo: Any = None
        highs_lows_6mo: Any = None
        highs_lows_ytd: Any = None
        highs_lows_52w: Any = None
        highs_lows_2yr: Any = None
        highs_lows_3yr: Any = None
        highs_lows_5yr: Any = None
        highs_lows_10yr: Any = None
        highs_lows_20yr: Any = None
        all_time_highs_lows: Any = None

        parent: Any = None
        symbols: str = None
        data: Dict[str, Any] = None

        def __init__(self, parent):
            self._parent = parent
            self.symbols = parent.symbols
            self.symbols = parent.symbols
            self.data = parent.query_category_builder.get(
                "highs_and_lows", self.symbols
            )

            self.highs_lows_5d = self.data.get("5d_highs_lows", None)
            self.highs_lows_1mo = self.data.get("1mo_highs_lows", None)
            self.highs_lows_3mo = self.data.get("3mo_highs_lows", None)
            self.highs_lows_6mo = self.data.get("6mo_highs_lows", None)
            self.highs_lows_ytd = self.data.get("ytd_highs_lows", None)
            self.highs_lows_52w = self.data.get("52w_highs_lows", None)
            self.highs_lows_2yr = self.data.get("2yr_highs_lows", None)
            self.highs_lows_3yr = self.data.get("3yr_highs_lows", None)
            self.highs_lows_5yr = self.data.get("5yr_highs_lows", None)
            self.highs_lows_10yr = self.data.get("10yr_highs_lows", None)
            self.highs_lows_20yr = self.data.get("20yr_highs_lows", None)
            self.all_time_highs_lows = self.data.get(
                "all_time_highs_lows", None
            )

    def Highs_and_lows(self):
        return self.__highs_and_lows(self)

    @dataclass
    class __fundamentals:

        key_statistics: Any = None
        earnings: Any = None
        dividends_and_splits: Any = None
        financial_ratios: Any = None
        analysts_and_estimates: Any = None
        income_statement_yearly_data: Any = None
        income_statement_quarterly_data: Any = None
        balance_sheet_yearly_data: Any = None
        balance_sheet_quarterly_data: Any = None
        cash_flow_yearly_data: Any = None
        cash_flow_quarterly_data: Any = None

        parent: Any = None
        symbols: str = None
        data: Dict[str, Any] = None

        def __init__(self, parent):
            self._parent = parent
            self.symbols = parent.symbols
            self.symbols = parent.symbols
            self.data = parent.query_category_builder.get(
                "fundamentals", self.symbols
            )

            for key, value in self.data.items():
                setattr(self, key, value)

    def Fundamentals(self):
        return self.__fundamentals(self)

    @dataclass
    class __options:

        options_overview_implied_volatility: Any = None
        options_overview_iv_rank: Any = None
        options_overview_iv_change: Any = None
        options_overview_iv_percentile: Any = None
        options_overview_implied_volatility_highs: Any = None
        options_overview_implied_volatility_lows: Any = None
        options_overview_total_options_volume: Any = None
        options_overview_total_options_volume_percent_change: Any = None
        options_overview_put_total_volume: Any = None
        options_overview_call_total_volume: Any = None
        options_overview_put_call_total_volume_ratio: Any = None
        options_overview_total_options_open_interest: Any = None
        options_overview_total_options_open_interest_percent_change: Any = None
        options_overview_total_put_open_interest: Any = None
        options_overview_total_call_open_interest: Any = None
        options_overview_total_put_call_open_interest_ratio: Any = None
        options_strikes_option_info: Any = None
        options_strikes_covered_call: Any = None
        options_strikes_options_analysis: Any = None
        options_strikes_strike_volatility: Any = None
        options_strikes_break_even: Any = None
        options_strikes_greeks: Any = None
        options_strikes_greek_ratios: Any = None
        options_strikes_probability: Any = None
        options_strikes_percent_of_stock: Any = None
        options_strikes_time_premium: Any = None
        options_strikes_yield_to_strike: Any = None
        options_strikes_potential_return: Any = None
        options_strikes_strike_to_standard_deviation: Any = None
        options_strikes_options_flow: Any = None

        parent: Any = None
        symbols: str = None
        data: Dict[str, Any] = None

        def __init__(self, parent):
            self._parent = parent
            self.symbols = parent.symbols
            self.symbols = parent.symbols
            self.data = parent.query_category_builder.get(
                "options", self.symbols
            )

            for key, value in self.data.items():
                setattr(self, key, value)

    def Options(self):
        return self.__options(self)

    @dataclass
    class __etfs:

        etfName: Any = None
        fundFamily: Any = None
        assetClass: Any = None
        leverage: Any = None
        managedAssets: Any = None
        netAssetValue: Any = None
        managementFee: Any = None
        alpha: Any = None

        parent: Any = None
        symbols: str = None
        data: Dict[str, Any] = None

        def __init__(self, parent):
            self._parent = parent
            self.symbols = parent.symbols
            self.symbols = parent.symbols
            self.data = parent.query_category_builder.get("etfs", self.symbols)

            tempdf = pd.DataFrame(self.data["etfs"]["data"])
            self.etfName = tempdf["etfName"].to_list()
            self.fundFamily = tempdf["fundFamily"].to_list()
            self.assetClass = tempdf["assetClass"].to_list()
            self.leverage = tempdf["leverage"].to_list()
            self.managedAssets = tempdf["managedAssets"].to_list()
            self.netAssetValue = tempdf["netAssetValue"].to_list()
            self.managementFee = tempdf["managementFee"].to_list()
            self.alpha = tempdf["alpha"].to_list()

    def Etfs(self):
        return self.__etfs(self)

    @dataclass
    class __futures:

        contractName: Any = None
        contractExpirationDate: Any = None
        daysToContractExpiration: Any = None
        contractFirstNoticeDate: Any = None
        daysToFirstNotice: Any = None
        pointValue: Any = None
        margin: Any = None
        openInterest: Any = None

        parent: Any = None
        symbols: str = None
        data: Dict[str, Any] = None

        def __init__(self, parent):
            self._parent = parent
            self.symbols = parent.symbols
            self.symbols = parent.symbols
            self.data = parent.query_category_builder.get(
                "futures", self.symbols
            )

            tempdf = pd.DataFrame(self.data["futures"]["data"])
            self.contractName = tempdf["contractName"].to_list()
            self.contractExpirationDate = tempdf[
                "contractExpirationDate"
            ].to_list()
            self.daysToContractExpiration = tempdf[
                "daysToContractExpiration"
            ].to_list()
            self.contractFirstNoticeDate = tempdf[
                "contractFirstNoticeDate"
            ].to_list()
            self.daysToFirstNotice = tempdf["daysToFirstNotice"].to_list()
            self.pointValue = tempdf["pointValue"].to_list()
            self.margin = tempdf["margin"].to_list()
            self.openInterest = tempdf["openInterest"].to_list()

    def Futures(self):
        return self.__futures(self)

    @dataclass
    class __portfolio:

        quantity: Any = None
        action: Any = None
        entry_date: Any = None
        entry_price: Any = None
        exit_date: Any = None
        exit_price: Any = None
        commission: Any = None
        stock_value: Any = None
        daily_return: Any = None
        ret: Any = None
        total_price_change: Any = None
        total_percent_change: Any = None

        parent: Any = None
        symbols: str = None
        data: Dict[str, Any] = None

        def __init__(self, parent):
            self._parent = parent
            self.symbols = parent.symbols
            self.symbols = parent.symbols
            self.data = parent.query_category_builder.get(
                "portfolio", self.symbols
            )

            tempdf = pd.DataFrame(self.data["portfolio"]["data"])
            self.quantity = tempdf["quantity"].to_list()
            self.action = tempdf["action"].to_list()
            self.entry_date = tempdf["entryDate"].to_list()
            self.entry_price = tempdf["entryPrice"].to_list()
            self.exit_date = tempdf["exitDate"].to_list()
            self.exit_price = tempdf["exitPrice"].to_list()
            self.commission = tempdf["commission"].to_list()
            self.stock_value = tempdf["stockValue"].to_list()
            self.daily_return = tempdf["dailyReturn"].to_list()
            self.ret = tempdf["return"].to_list()
            self.total_price_change = tempdf["totalPriceChange"].to_list()
            self.total_percent_change = tempdf["totalPercentChange"].to_list()

    def Portfolio(self):
        return self.__portfolio(self)
