from barchartFetcher.constants.analysts import *
from barchartFetcher.constants.company import *
from barchartFetcher.constants.financials import *
from barchartFetcher.constants.options import *
from barchartFetcher.constants.options_strategies import *
from barchartFetcher.constants.quotes import *
from barchartFetcher.constants.technicals import *

fields_classes_mapping = {
    "analyst_ratings": AnalystRatingsFields(),
    "butterfly_spreads": ButterflySpreadsFields(),
    "condor": CondorFields(),
    "covered_calls": CoveredCallsFields(),
    "earnings_estimates": EarningsEstimatesFields(),
    "expected_move": ExpectedMoveFields(),
    "expirations": ExpirationsFields(),
    "financial_summary": FinancialSummaryFields(),
    "gex": GEXFields(),
    "horizontal_spreads": HorizontalSpreadsFields(),
    "insider_trades": InsiderTradesFields(),
    "key_statistics": KeyStatisticsFields(),
    "long_call_put": LongCallPutFields(),
    "max_pain_vol_skew": MaxPainVolSkewFields(),
    "naked_puts": NakedPutsFields(),
    "opinion": OpinionFields(),
    "options_flow": OptionsFlowFields(),
    "options_prices": OptionsPricesFields(),
    "overview": OverviewFields(),
    "performance_report": PerformanceReportFields(),
    "protection_strategies": ProtectionStrategiesFields(),
    "put_call_ratios": PutCallRatioSFields(),
    "sec_filings": SECFilingsFields(),
    "sector_competitors": SectorCompetitorsFields(),
    "straddles_strangles": StraddlesStranglesFields(),
    "technical_analysis": TechnicalAnalysisFields(),
    "vertical_spreads": VerticalSpreadsFields(),
    "volatility_charts": VolatilityChartsFields(),
}
