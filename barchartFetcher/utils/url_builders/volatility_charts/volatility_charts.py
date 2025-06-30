# Module: volatility_charts
from urllib.parse import urlencode


def dte_histo_iv(
    symbol: str = "AAPL",
    limit: int = 999,
    orderBy: str = "date",
    orderDir: str = "desc",
    groupBy: str = "date",
) -> str:
    """URL builder for dte_histo_iv"""
    base_url = "https://www.barchart.com/proxies/core-api/v1/options/delta/get"
    params = {
        "symbol": symbol,
        "limit": limit,
        "orderBy": orderBy,
        "orderDir": orderDir,
        "groupBy": groupBy,
        "fields": "symbol,date,delta05_30_puts,delta05_60_puts,delta05_90_puts,delta05_120_puts,delta05_150_puts,delta05_180_puts,delta05_360_puts,delta10_30_puts,delta10_60_puts,delta10_90_puts,delta10_120_puts,delta10_150_puts,delta10_180_puts,delta10_360_puts,delta15_30_puts,delta15_60_puts,delta15_90_puts,delta15_120_puts,delta15_150_puts,delta15_180_puts,delta15_360_puts,delta20_30_puts,delta20_60_puts,delta20_90_puts,delta20_120_puts,delta20_150_puts,delta20_180_puts,delta20_360_puts,delta25_30_puts,delta25_60_puts,delta25_90_puts,delta25_120_puts,delta25_150_puts,delta25_180_puts,delta25_360_puts,delta30_30_puts,delta30_60_puts,delta30_90_puts,delta30_120_puts,delta30_150_puts,delta30_180_puts,delta30_360_puts,delta35_30_puts,delta35_60_puts,delta35_90_puts,delta35_120_puts,delta35_150_puts,delta35_180_puts,delta35_360_puts,delta40_30_puts,delta40_60_puts,delta40_90_puts,delta40_120_puts,delta40_150_puts,delta40_180_puts,delta40_360_puts,delta45_30_puts,delta45_60_puts,delta45_90_puts,delta45_120_puts,delta45_150_puts,delta45_180_puts,delta45_360_puts,delta50_30_puts,delta50_60_puts,delta50_90_puts,delta50_120_puts,delta50_150_puts,delta50_180_puts,delta50_360_puts,delta55_30_puts,delta55_60_puts,delta55_90_puts,delta55_120_puts,delta55_150_puts,delta55_180_puts,delta55_360_puts,delta60_30_puts,delta60_60_puts,delta60_90_puts,delta60_120_puts,delta60_150_puts,delta60_180_puts,delta60_360_puts,delta65_30_puts,delta65_60_puts,delta65_90_puts,delta65_120_puts,delta65_150_puts,delta65_180_puts,delta65_360_puts,delta70_30_puts,delta70_60_puts,delta70_90_puts,delta70_120_puts,delta70_150_puts,delta70_180_puts,delta70_360_puts,delta75_30_puts,delta75_60_puts,delta75_90_puts,delta75_120_puts,delta75_150_puts,delta75_180_puts,delta75_360_puts,delta80_30_puts,delta80_60_puts,delta80_90_puts,delta80_120_puts,delta80_150_puts,delta80_180_puts,delta80_360_puts,delta85_30_puts,delta85_60_puts,delta85_90_puts,delta85_120_puts,delta85_150_puts,delta85_180_puts,delta85_360_puts,delta90_30_puts,delta90_60_puts,delta90_90_puts,delta90_120_puts,delta90_150_puts,delta90_180_puts,delta90_360_puts,delta95_30_puts,delta95_60_puts,delta95_90_puts,delta95_120_puts,delta95_150_puts,delta95_180_puts,delta95_360_puts,delta05_30_calls,delta05_60_calls,delta05_90_calls,delta05_120_calls,delta05_150_calls,delta05_180_calls,delta05_360_calls,delta10_30_calls,delta10_60_calls,delta10_90_calls,delta10_120_calls,delta10_150_calls,delta10_180_calls,delta10_360_calls,delta15_30_calls,delta15_60_calls,delta15_90_calls,delta15_120_calls,delta15_150_calls,delta15_180_calls,delta15_360_calls,delta20_30_calls,delta20_60_calls,delta20_90_calls,delta20_120_calls,delta20_150_calls,delta20_180_calls,delta20_360_calls,delta25_30_calls,delta25_60_calls,delta25_90_calls,delta25_120_calls,delta25_150_calls,delta25_180_calls,delta25_360_calls,delta30_30_calls,delta30_60_calls,delta30_90_calls,delta30_120_calls,delta30_150_calls,delta30_180_calls,delta30_360_calls,delta35_30_calls,delta35_60_calls,delta35_90_calls,delta35_120_calls,delta35_150_calls,delta35_180_calls,delta35_360_calls,delta40_30_calls,delta40_60_calls,delta40_90_calls,delta40_120_calls,delta40_150_calls,delta40_180_calls,delta40_360_calls,delta45_30_calls,delta45_60_calls,delta45_90_calls,delta45_120_calls,delta45_150_calls,delta45_180_calls,delta45_360_calls,delta50_30_calls,delta50_60_calls,delta50_90_calls,delta50_120_calls,delta50_150_calls,delta50_180_calls,delta50_360_calls,delta55_30_calls,delta55_60_calls,delta55_90_calls,delta55_120_calls,delta55_150_calls,delta55_180_calls,delta55_360_calls,delta60_30_calls,delta60_60_calls,delta60_90_calls,delta60_120_calls,delta60_150_calls,delta60_180_calls,delta60_360_calls,delta65_30_calls,delta65_60_calls,delta65_90_calls,delta65_120_calls,delta65_150_calls,delta65_180_calls,delta65_360_calls,delta70_30_calls,delta70_60_calls,delta70_90_calls,delta70_120_calls,delta70_150_calls,delta70_180_calls,delta70_360_calls,delta75_30_calls,delta75_60_calls,delta75_90_calls,delta75_120_calls,delta75_150_calls,delta75_180_calls,delta75_360_calls,delta80_30_calls,delta80_60_calls,delta80_90_calls,delta80_120_calls,delta80_150_calls,delta80_180_calls,delta80_360_calls,delta85_30_calls,delta85_60_calls,delta85_90_calls,delta85_120_calls,delta85_150_calls,delta85_180_calls,delta85_360_calls,delta90_30_calls,delta90_60_calls,delta90_90_calls,delta90_120_calls,delta90_150_calls,delta90_180_calls,delta90_360_calls,delta95_30_calls,delta95_60_calls,delta95_90_calls,delta95_120_calls,delta95_150_calls,delta95_180_calls,delta95_360_calls,delta05_30_both,delta05_60_both,delta05_90_both,delta05_120_both,delta05_150_both,delta05_180_both,delta05_360_both,delta10_30_both,delta10_60_both,delta10_90_both,delta10_120_both,delta10_150_both,delta10_180_both,delta10_360_both,delta15_30_both,delta15_60_both,delta15_90_both,delta15_120_both,delta15_150_both,delta15_180_both,delta15_360_both,delta20_30_both,delta20_60_both,delta20_90_both,delta20_120_both,delta20_150_both,delta20_180_both,delta20_360_both,delta25_30_both,delta25_60_both,delta25_90_both,delta25_120_both,delta25_150_both,delta25_180_both,delta25_360_both,delta30_30_both,delta30_60_both,delta30_90_both,delta30_120_both,delta30_150_both,delta30_180_both,delta30_360_both,delta35_30_both,delta35_60_both,delta35_90_both,delta35_120_both,delta35_150_both,delta35_180_both,delta35_360_both,delta40_30_both,delta40_60_both,delta40_90_both,delta40_120_both,delta40_150_both,delta40_180_both,delta40_360_both,delta45_30_both,delta45_60_both,delta45_90_both,delta45_120_both,delta45_150_both,delta45_180_both,delta45_360_both,delta50_30_both,delta50_60_both,delta50_90_both,delta50_120_both,delta50_150_both,delta50_180_both,delta50_360_both,delta55_30_both,delta55_60_both,delta55_90_both,delta55_120_both,delta55_150_both,delta55_180_both,delta55_360_both,delta60_30_both,delta60_60_both,delta60_90_both,delta60_120_both,delta60_150_both,delta60_180_both,delta60_360_both,delta65_30_both,delta65_60_both,delta65_90_both,delta65_120_both,delta65_150_both,delta65_180_both,delta65_360_both,delta70_30_both,delta70_60_both,delta70_90_both,delta70_120_both,delta70_150_both,delta70_180_both,delta70_360_both,delta75_30_both,delta75_60_both,delta75_90_both,delta75_120_both,delta75_150_both,delta75_180_both,delta75_360_both,delta80_30_both,delta80_60_both,delta80_90_both,delta80_120_both,delta80_150_both,delta80_180_both,delta80_360_both,delta85_30_both,delta85_60_both,delta85_90_both,delta85_120_both,delta85_150_both,delta85_180_both,delta85_360_both,delta90_30_both,delta90_60_both,delta90_90_both,delta90_120_both,delta90_150_both,delta90_180_both,delta90_360_both,delta95_30_both,delta95_60_both,delta95_90_both,delta95_120_both,delta95_150_both,delta95_180_both,delta95_360_both,",
    }
    query = urlencode(params)
    url = base_url + "?" + query
    return url


def ex_histo_iv(
    symbol: str = "AAPL",
    expirations=None,
    groupBy: str = "date",
) -> str:
    """URL builder for ex_histo_iv"""
    base_url = "https://www.barchart.com/proxies/core-api/v1/options/delta/get"
    params = {
        "symbol": symbol,
        "expirations": expirations,
        "eq(date,latest)": "",
        "groupBy": groupBy,
        "fields": "symbol,date,delta05_puts,delta10_puts,delta15_puts,delta20_puts,delta25_puts,delta30_puts,delta35_puts,delta40_puts,delta45_puts,delta50_puts,delta55_puts,delta60_puts,delta65_puts,delta70_puts,delta75_puts,delta80_puts,delta85_puts,delta90_puts,delta95_puts,delta05_calls,delta10_calls,delta15_calls,delta20_calls,delta25_calls,delta30_calls,delta35_calls,delta40_calls,delta45_calls,delta50_calls,delta55_calls,delta60_calls,delta65_calls,delta70_calls,delta75_calls,delta80_calls,delta85_calls,delta90_calls,delta95_calls,delta05_both,delta10_both,delta15_both,delta20_both,delta25_both,delta30_both,delta35_both,delta40_both,delta45_both,delta50_both,delta55_both,delta60_both,delta65_both,delta70_both,delta75_both,delta80_both,delta85_both,delta90_both,delta95_both",
    }
    query = urlencode(params)
    url = base_url + "?" + query
    return url


def historical_volatility(
    symbols: str = "AAPL",
    limit: int = 999,
    period: int = 30,
    orderBy: str = "tradeTime",
    orderDir: str = "desc",
    raw: int = 1,
) -> str:
    """URL builder for historical_volatility"""
    base_url = (
        "https://www.barchart.com/proxies/core-api/v1/historical-volatility"
    )
    params = {
        "symbols": symbols,
        "limit": limit,
        "period": period,
        "orderBy": orderBy,
        "orderDir": orderDir,
        "fields": "symbol,volatility,tradeTime",
        "raw": raw,
    }
    query = urlencode(params)
    url = base_url + "?" + query
    return url


def iv_rank_percentile(
    symbol: str = "AAPL",
    limit: int = 360,
    orderBy: str = "date",
    orderDir: str = "desc",
    raw: int = 1,
) -> str:
    """URL builder for iv_rank_percentile"""
    base_url = (
        "https://www.barchart.com/proxies/core-api/v1/options-historical/get"
    )
    params = {
        "symbol": symbol,
        "limit": limit,
        "orderBy": orderBy,
        "orderDir": orderDir,
        "raw": raw,
        "fields": "symbol,impliedVolatilityRank1y,impliedVolatilityPercentile1y,totalVolume,totalOpenInterest,historicalLastPrice,date",
    }
    query = urlencode(params)
    url = base_url + "?" + query
    return url
