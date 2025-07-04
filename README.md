<h1>barchartFetcher</h1>

Client utilities for fetching quotes, options data and fundamental metrics from Barchart.

* **Documentation**: [barchartFetcher documentation](https://github.com/nndjoli/barchartFetcher/blob/main/docs/documentation.md)
<h2>Requirements & Installation:</h2>

* **Dependencies**: `httpx`, `nest_asyncio`, `pandas`, `beautifulsoup4`
* **To install**, run:

```bash
pip install barchartFetcher
```

<h2>Example:</h2>

The package exposes several classes—`Quotes`, `Options`, `Company`, `Financials`, `Analysts`, `Technicals`, `OptionsStrategies` and a convenience wrapper `Symbol` to access multiple endpoints at once.

```python
quotes = barchartFetcher.Quotes()
q = quotes.quote("AAPL")

print("Keys:\n")
print(q.keys())

print("\nMeta:\n")
pprint(q['meta'])

print("\nData:\n")
pprint(q['data'])
```

Output:

```
Keys:

dict_keys(['count', 'total', 'data', 'meta', 'errors'])

Meta:

{'field': {'description': {'averageVolume20d': 'The average number of shares '
                                               'or contracts traded over the '
                                               'last 20 days.',
                           'highPrice': 'The highest trade price for the day.',
                           'highPrice1y': 'The highest price over the last '
                                          '52-weeks.',
                           'lastPrice': 'The last trade price.',
                           'lowPrice': 'The lowest trade price for the day.',
                           'lowPrice1y': 'The lowest price over the last '
                                         '52-weeks.',
                           'openPrice': 'Opening price for the day.',
                           'percentChange5d': '5-Day Percent Change: The '
                                              'percent difference between the '
                                              'current price and the '
                                              'settlement price from 5 days '
                                              'ago.',
                           'priceChange5d': '5-Day Price Change: The '
                                            'difference between the current '
                                            'price, and the settlement price '
                                            'from 5 days ago.',
                           'rangePercent1y': 'The current price range over a '
                                             '52-week period, expressed as a '
                                             'percent. ((last price - 52W low) '
                                             '/ (52W high - 52W low)) * 100.0',
                           'stochasticK14d': 'Shows (within a range of '
                                             '0%-100%) where the price closed '
                                             'in relation to its price range '
                                             'over the last 14-Days with a '
                                             '3-period exponential moving '
                                             'average applied.',
                           'symbol': '',
                           'volume': 'The total number of shares or contracts '
                                     'traded for the day.',
                           'weightedAlpha': 'A measure of how much a stock has '
                                            'risen or fallen over a one-year '
                                            'period with a higher weighting '
                                            'for recent price activity.'},
           'shortName': {'averageVolume20d': '20D Avg Vol',
                         'highPrice': 'High',
                         'highPrice1y': '52W High',
                         'lastPrice': 'Last',
                         'lowPrice': 'Low',
                         'lowPrice1y': '52W Low',
                         'openPrice': 'Open',
                         'percentChange5d': '5D %Chg',
                         'priceChange5d': '5D Chg',
                         'rangePercent1y': '52W Range%',
                         'stochasticK14d': '14D Stoch %K',
                         'symbol': 'Symbol',
                         'volume': 'Volume',
                         'weightedAlpha': 'Wtd Alpha'},
           'type': {'averageVolume20d': 'integer',
                    'highPrice': 'price',
                    'highPrice1y': 'price',
                    'lastPrice': 'price',
                    'lowPrice': 'price',
                    'lowPrice1y': 'price',
                    'openPrice': 'price',
                    'percentChange5d': 'percentChange',
                    'priceChange5d': 'priceChange',
                    'rangePercent1y': 'percent',
                    'stochasticK14d': 'percent',
                    'symbol': 'string',
                    'volume': 'integer',
                    'weightedAlpha': 'change'}}}

Data:

[{'averageVolume20d': '58,270,727',
  'highPrice': '213.34',
  'highPrice1y': '260.10',
  'lastPrice': '212.44',
  'lowPrice': '208.14',
  'lowPrice1y': '169.21',
  'openPrice': '208.91',
  'percentChange5d': '+5.40%',
  'priceChange5d': '+10.88',
  'rangePercent1y': '47.56%',
  'raw': {'averageVolume20d': 58270727,
          'highPrice': 213.34,
          'highPrice1y': 260.1,
          'lastPrice': 212.44,
          'lowPrice': 208.14,
          'lowPrice1y': 169.21,
          'openPrice': 208.91,
          'percentChange5d': 0.054,
          'priceChange5d': 10.88,
          'rangePercent1y': 47.56,
          'stochasticK14d': 87.13,
          'symbol': 'AAPL',
          'volume': 67941805,
          'weightedAlpha': -7.38},
  'stochasticK14d': '87.13%',
  'symbol': 'AAPL',
  'volume': '67,941,805',
  'weightedAlpha': '-7.38'}]
```

The `Symbol` class aggregates calls to different endpoints:

```python
aapl = barchartFetcher.Symbol("AAPL")
quotes_data = aapl.quotes()

print("Keys:\n")
print(quotes_data.keys())
print("\nOptions Overview Keys:\n")
print(quotes_data['options_overview'].keys())
print("\nOptions Overview Data:\n")
pprint(quotes_data['options_overview']['data'])
```

Output:

```
Keys:

dict_keys(['performance_past5d', 'performance_past5m', 'performance_past5w', 'price_performance', 'technical_opinion', 'options_overview', 'analysts_rating', 'fundamentals', 'lows_highs', 'quote'])

Options Overview Keys:

dict_keys(['count', 'total', 'data', 'meta', 'errors'])

Options Overview Data:

[{'historicVolatility30d': '21.31%',
  'optionsImpliedVolatilityPercentile1y': '75%',
  'optionsImpliedVolatilityRank1y': '26.00%',
  'optionsPutCallOpenInterestRatio': '0.72',
  'optionsPutCallVolumeRatio': '0.41',
  'optionsTotalOpenInterest': '5,330,140',
  'optionsTotalOpenInterest1m': '5,366,503',
  'optionsTotalVolume': '1,827,658',
  'optionsTotalVolume1m': '1,106,224',
  'optionsWeightedImpliedVolatility': '28.77%',
  'optionsWeightedImpliedVolatilityChange': '-0.31%',
  'optionsWeightedImpliedVolatilityHigh1y': '65.20%',
  'optionsWeightedImpliedVolatilityHighDate1y': '04/08/25',
  'optionsWeightedImpliedVolatilityLow1y': '15.97%',
  'optionsWeightedImpliedVolatilityLowDate1y': '12/04/24',
  'raw': {'historicVolatility30d': 21.31,
          'optionsImpliedVolatilityPercentile1y': 0.752,
          'optionsImpliedVolatilityRank1y': 25.999041095916,
          'optionsPutCallOpenInterestRatio': 0.71798737102943,
          'optionsPutCallVolumeRatio': 0.40845524119686,
          'optionsTotalOpenInterest': 5330140,
          'optionsTotalOpenInterest1m': 5366503,
          'optionsTotalVolume': 1827658,
          'optionsTotalVolume1m': 1106224,
          'optionsWeightedImpliedVolatility': 0.2876826080111,
          'optionsWeightedImpliedVolatilityChange': -0.0030605360889064,
          'optionsWeightedImpliedVolatilityHigh1y': 0.65202232651026,
          'optionsWeightedImpliedVolatilityHighDate1y': '2025-04-08T00:00:00Z',
          'optionsWeightedImpliedVolatilityLow1y': 0.15967773544705,
          'optionsWeightedImpliedVolatilityLowDate1y': '2024-12-04T00:00:00Z',
          'symbol': 'AAPL'},
  'symbol': 'AAPL'}]
  ```

Working directly with options data:

```python
options = barchartFetcher.Options()
exp = options.options_expirations("AAPL")
pprint(exp)
```

Output (truncated):

```
{'count': 21,
 'data': [{'callOpenInterest': '254,300',
           'callVolume': '675,585',
           'expirationDate': '07/03/25',
           'expirationType': 'weekly',
           'putCallOpenInterestRatio': '0.47',
           'putCallVolumeRatio': '0.45',
           'putOpenInterest': '120,098',
           'putVolume': '302,301',
           'raw': {'callOpenInterest': 254300,
                   'callVolume': 675585,
                   'expirationDate': '2025-07-03',
                   'expirationType': 'weekly',
                   'putCallOpenInterestRatio': 0.4723,
                   'putCallVolumeRatio': 0.4475,
                   'putOpenInterest': 120098,
                   'putVolume': 302301,
                   'symbol': 'AAPL|20250703|212.50C'},
            
            ... # Truncated
           
           'symbol': 'AAPL|20270617|210.00C'},
          {'callOpenInterest': '44,751',
           'callVolume': '2,369',
           'expirationDate': '12/17/27',
           'expirationType': 'monthly',
           'putCallOpenInterestRatio': '0.46',
           'putCallVolumeRatio': '0.22',
           'putOpenInterest': '20,692',
           'putVolume': '527',
           'raw': {'callOpenInterest': 44751,
                   'callVolume': 2369,
                   'expirationDate': '2027-12-17',
                   'expirationType': 'monthly',
                   'putCallOpenInterestRatio': 0.4624,
                   'putCallVolumeRatio': 0.2225,
                   'putOpenInterest': 20692,
                   'putVolume': 527,
                   'symbol': 'AAPL|20271217|210.00C'},
           'symbol': 'AAPL|20271217|210.00C'}],
 'meta': {'field': {'description': {'callOpenInterest': 'The call open '
                                                        'interest for the '
                                                        'current trading '
                                                        'session.',
                                    'callVolume': 'The total call volume for '
                                                  'the current trading session '
                                                  'for the underlying asset.',
                                    'expirationDate': 'The option expiration '
                                                      'date.',
                                    'expirationType': 'The type of option '
                                                      'expiration: monthly or '
                                                      'weekly.',
                                    'putCallOpenInterestRatio': 'The put/call '
                                                                'open interest '
                                                                'ratio based '
                                                                'on 1-day '
                                                                'average open '
                                                                'interest for '
                                                                'the '
                                                                'underlying '
                                                                'asset.',
                                    'putCallVolumeRatio': 'The underlying '
                                                          "asset's total "
                                                          'Put/Call volume '
                                                          'ratio for the '
                                                          'current trading '
                                                          'session.',
                                    'putOpenInterest': 'The put open interest '
                                                       'for the current '
                                                       'trading session.',
                                    'putVolume': 'The total put volume for the '
                                                 'current trading session for '
                                                 'the underlying asset.',
                                    'symbol': ''},
                    'shortName': {'callOpenInterest': 'Call OI',
                                  'callVolume': 'Call Volume',
                                  'expirationDate': 'Exp Date',
                                  'expirationType': 'Exp Type',
                                  'putCallOpenInterestRatio': 'P/C OI',
                                  'putCallVolumeRatio': 'P/C Vol',
                                  'putOpenInterest': 'Put OI',
                                  'putVolume': 'Put Volume',
                                  'symbol': 'Symbol'},
                    'type': {'callOpenInterest': 'integer',
                             'callVolume': 'integer',
                             'expirationDate': 'date',
                             'expirationType': 'string',
                             'putCallOpenInterestRatio': 'float',
                             'putCallVolumeRatio': 'float',
                             'putOpenInterest': 'integer',
                             'putVolume': 'integer',
                             'symbol': 'string'}}},
 'total': 21}
 ```

Additional examples:

```python
company = barchartFetcher.Company().company_informations("AAPL")
print(list(company["meta"]["field"]["shortName"].items())[:5])
print(list(company["data"][0].items())[:3])

analysts = barchartFetcher.Analysts().earnings_estimates("AAPL")
print(list(analysts["data"][0].items())[:3])

financials = barchartFetcher.Financials().financial_summary_quarterly("AAPL")
print(list(financials["data"][0].items())[:3])

technicals = barchartFetcher.Technicals().moving_averages("AAPL")
print(list(technicals["data"][0].keys())[:3])

strategies = barchartFetcher.OptionsStrategies().covered_calls(baseSymbol="AAPL")
print(len(strategies["data"]))
```

Outputs (truncated):

```
[('symbol', 'Symbol'), ('symbolShortName', 'Name'), ('address', 'Address'), ('country', 'Country'), ('website', 'Website')]
[('symbol', 'AAPL'), ('symbolShortName', 'Apple Inc'), ('address', ['ONE APPLE PARK WAY', 'CUPERTINO CA 95014 USA'])]
[('symbol', 'AAPL'), ('estimatedEarnings', '$1.42'), ('estimatedEarnings1qAgo', '$1.61')]
[('symbol', 'AAPL'), ('revenueLastQuarter', '95,359,000'), ('revenue1qAgo', '124,300,000')]
['symbol', 'movingAverage5d', 'priceChange5d']
0
```

Available helper classes and their main use-cases are summarized below.

| Class               | Description                                                 | Customizable query parameters |
| ------------------- | ----------------------------------------------------------- | ----------------------------- |
| `Quotes`            | Retrieve quotes, fundamentals and performance statistics    | True                          |
| `Options`           | Access options chains, expirations and volatility metrics   | True                          |
| `OptionsStrategies` | Screener utilities for common options strategies            | True                          |
| `Financials`        | Income statement, balance sheet and cash flow statements    | True                          |
| `Analysts`          | Analyst ratings and earnings estimates                      | True                          |
| `Company`           | Company profile, ratios and insider transactions            | True                          |
| `Technicals`        | Moving averages, stochastics and other indicators           | True                          |
| `Symbol`            | Convenience wrapper combining the above for a single symbol | False (uses Barchart default parameters; recommended)                          |

Results are typically returned as parsed JSON objects or DataFrames (for tables scraped from HTML). The package uses `httpx` with an internal cookie/session manager to query Barchart endpoints.

<h2>Usage Disclaimer</h2>

This library is intended for personal and educational use only. It is not affiliated with or endorsed by Barchart. The maintainers do not encourage or condone scraping or any activity that violates Barchart’s Terms of Service. Refer to the MIT License in this repository for warranty and liability information.