# barchartFetcher Classes Overview

This document lists the classes imported in `__init__.py` and the queries they perform. It describes what each method returns and the main parameters you can adjust.

Most methods return a dictionary containing at least the keys `data`, `meta`, `count`, and `total`. Some functions from `Financials` also produce `DataFrame` objects when parsing financial tables.

## Available classes

- `Analysts` – earnings estimates and analyst recommendations
- `Company` – company profiles, ratios and insider transactions
- `Financials` – financial statements
- `Options` – options data and volatility metrics
- `OptionsStrategies` – screeners for more than thirty option strategies
- `Quotes` – quotes and performance statistics
- `Technicals` – technical indicators
- `Symbol` – wrapper that combines the previous classes for a single symbol

---

## Analysts

| Method | Description | Parameters |
|-------|-------------|----------------|
| `earnings_estimates` | EPS forecasts and expected earnings release dates | `symbols`, `raw` |
| `analyst_ratings` | Analyst ratings and revisions for a symbol | `symbol`, `raw` |

## Company

| Method | Description | Parameters |
|-------|-------------|----------------|
| `sector_competitors` | Competitors within a given sector for a symbol | `symbol`, `sector_symbol`, `orderBy`, `orderDir`, `hasOptions`, `page`, `limit`, `raw` |
| `company_informations` | Company profile including address and sector | `symbols`, `raw` |
| `growth` | Growth metrics such as revenue or earnings | `symbols`, `raw` |
| `quote_overview` | Quick quote overview | `symbols`, `raw` |
| `per_share_information` | Per-share metrics like EPS and dividends | `symbols`, `raw` |
| `ratios` | Key financial ratios | `symbols`, `raw` |
| `sec_filings` | Latest SEC filings | `symbol`, `transactions`, `limit` |
| `insider_trades` | Recent insider trades | `symbol`, `transactions`, `limit` |

## Financials

| Method | Description | Parameters |
|-------|-------------|----------------|
| `financial_summary_quarterly` | Quarterly financial summary | `symbols`, `raw` |
| `financial_summary_yearly` | Yearly financial summary | `symbols`, `raw` |
| `income_statement` | Income statement table | `symbol`, `frequency`, `page` |
| `balance_sheet` | Balance sheet table | `symbol`, `frequency`, `page` |
| `cash_flow` | Cash flow statement table | `symbol`, `frequency`, `page` |

## Options

| Method | Description | Parameters |
|-------|-------------|----------------|
| `historical_earnings` | Historical earnings or events data | `symbol`, `type`, `events` |
| `expected_move` | Expected move and volatility | `symbol`, `orderBy`, `orderDir`, `raw`, `page`, `limit` |
| `options_expirations` | Available option expirations | `symbols`, `raw` |
| `bullish_bearish_sentiment` | Bullish/bearish sentiment for a symbol | `symbol`, `raw` |
| `options_flow` | Notable options flow | `symbol`, `orderBy`, `orderDir`, `limit`, `min_trade_size`, `raw` |
| `gamma_exposure` | Gamma exposure by strike | `symbols`, `expirations`, `groupBy`, `max_strike_spot_distance` |
| `max_pain_vol_skew` | Max pain and volatility skew metrics | `symbols`, `raw`, `expirations`, `groupBy`, `max_strike_spot_distance` |
| `options_prices` | Filtered option chain | `baseSymbol`, `groupBy`, `expirationDate`, `orderBy`, `orderDir`, `optionsOverview`, `raw` |
| `put_call_ratio` | Current put/call ratio | `symbol`, `raw`, `page`, `limit` |
| `historical_put_call_ratios` | Historical put/call ratio | `symbol`, `limit`, `orderBy`, `orderDir` |
| `historical_iv_by_days_to_exp` | Implied volatility by days to expiration | `symbol`, `limit`, `orderBy`, `orderDir`, `groupBy` |
| `historical_iv_by_exp_dates` | Implied volatility by expiration date | `symbol`, `expirations`, `groupBy` |
| `historical_volatility` | Historical volatility | `symbols`, `limit`, `period`, `orderBy`, `orderDir`, `raw` |
| `historical_iv_rank_percentile` | Implied volatility rank percentile | `symbol`, `limit`, `orderBy`, `orderDir`, `raw` |

## OptionsStrategies

Each method in this class returns opportunities for a specific options strategy. Common parameters include `baseSymbol`, `orderBy`, `orderDir`, `expirationDate`, `expirationType`, `page`, `limit`, and `raw`. Results provide a table of strategies with information such as probability of profit, cost, and potential yield.

## Quotes

| Method | Description | Parameters |
|-------|-------------|----------------|
| `analyst_rating` | Overview of analyst recommendations | `symbols`, `raw` |
| `fundamentals` | Fundamental data such as market cap and dividends | `symbols`, `raw` |
| `options_overview` | Summary of the options chain | `symbols`, `raw` |
| `price_performance` | Price performance metrics | `symbols`, `raw` |
| `quote` | Last traded price and volume | `symbols`, `raw` |
| `technical_opinion` | Aggregated technical opinion | `symbols`, `raw` |
| `lows_highs` | 52-week lows and highs | `symbols`, `raw` |
| `performance_past_5d` | Performance over the last five days | `symbols`, `raw` |
| `performance_past_5m` | Performance over the last five months | `symbols`, `raw` |
| `performance_past_5w` | Performance over the last five weeks | `symbols`, `raw` |
| `price_per` | Price performance ratios | `symbols`, `raw` |

## Technicals

| Method | Description | Parameters |
|-------|-------------|----------------|
| `moving_averages` | Moving averages | `symbols`, `raw` |
| `stochastics` | Stochastic oscillator | `symbols`, `raw` |
| `strength` | Relative strength index | `symbols`, `raw` |
| `composite_indicator` | Composite trend indicator | `symbols`, `raw` |
| `long_term_indicators` | Long-term trend indicators | `symbols`, `raw` |
| `medium_term_indicators` | Medium-term trend indicators | `symbols`, `raw` |
| `barchart_opinion` | General Barchart opinion | `symbols`, `raw` |
| `short_term_indicators` | Short-term trend indicators | `symbols`, `raw` |

## Symbol

This class chains several asynchronous requests for a given symbol. After retrieving the available options expirations it exposes methods (`financials`, `analysts`, `company`, `technicals`, `quotes`, `options` and various strategy groups) that return the same structures as the methods listed above. It uses Barchart’s default query parameters, which are also the defaults in the previously presented classes methods.
 