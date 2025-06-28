class QueryEndpoints:
    def __init__(self):
        # Quote Endpoint
        self.quote = "https://www.barchart.com/proxies/core-api/v1/quotes/get?"

        # Historical Endpoints
        self.historical = (
            "https://www.barchart.com/proxies/core-api/v1/historical/get?"
        )
        self.historical_volatility = "https://www.barchart.com/proxies/core-api/v1/historical-volatility?"

        # Options Endpoints
        self.options = (
            "https://www.barchart.com/proxies/core-api/v1/options/get?"
        )
        self.options_flow = (
            "https://www.barchart.com/proxies/core-api/v1/options/flow?"
        )
        self.options_historical = "https://www.barchart.com/proxies/core-api/v1/options-historical/get?"
        self.options_expirations = "https://www.barchart.com/proxies/core-api/v1/options-expirations/get?"
        self.options_delta = (
            "https://www.barchart.com/proxies/core-api/v1/options/delta/get?"
        )

        # Options Strategies Endpoints
        self.covered_calls = "https://www.barchart.com/proxies/core-api/v1/options/covered-calls?"
        self.naked_puts = (
            "https://www.barchart.com/proxies/core-api/v1/options/naked-puts?"
        )

        # Vertical Spreads Endpoints
        self.bear_call_spreads = "https://www.barchart.com/proxies/core-api/v1/options/bear-calls-spread?"
        self.bear_put_spreads = "https://www.barchart.com/proxies/core-api/v1/options/bear-puts-spread?"
        self.bull_call_spreads = "https://www.barchart.com/proxies/core-api/v1/options/bull-calls-spread?"
        self.bull_put_spreads = "https://www.barchart.com/proxies/core-api/v1/options/bull-puts-spread?"

        # Protection Strategies Endpoints
        self.married_puts = (
            "https://www.barchart.com/proxies/core-api/v1/options/married-put?"
        )
        self.long_collar_spread = "https://www.barchart.com/proxies/core-api/v1/options/long-collar-spread?"

        # Straddle and Strangle Strategies Endpoints
        self.long_straddle = "https://www.barchart.com/proxies/core-api/v1/options/long-straddle-spread?"
        self.long_strangle = "https://www.barchart.com/proxies/core-api/v1/options/long-strangle-spread?"
        self.short_straddle = "https://www.barchart.com/proxies/core-api/v1/options/short-straddle-spread?"
        self.short_strangle = "https://www.barchart.com/proxies/core-api/v1/options/short-strangle-spread?"

        # Horizontal Spreads Endpoints
        self.long_call_calendar = "https://www.barchart.com/proxies/core-api/v1/options/long-call-calendar-spread?"
        self.long_put_calendar = "https://www.barchart.com/proxies/core-api/v1/options/long-put-calendar-spread?"
        self.long_call_diagonal = "https://www.barchart.com/proxies/core-api/v1/options/bull-calls-diagonal-spread?"
        self.short_call_diagonal = "https://www.barchart.com/proxies/core-api/v1/options/bear-calls-diagonal-spread?"
        self.long_put_diagonal = "https://www.barchart.com/proxies/core-api/v1/options/bull-puts-diagonal-spread?"
        self.short_put_diagonal = "https://www.barchart.com/proxies/core-api/v1/options/bear-puts-diagonal-spread?"

        # Butterfly Strategies Endpoints
        self.long_call_butterfly = "https://www.barchart.com/proxies/core-api/v1/options/long-call-butterfly-spread?"
        self.short_call_butterfly = "https://www.barchart.com/proxies/core-api/v1/options/short-call-butterfly-spread?"
        self.long_put_butterfly = "https://www.barchart.com/proxies/core-api/v1/options/long-put-butterfly-spread?"
        self.short_put_butterfly = "https://www.barchart.com/proxies/core-api/v1/options/short-put-butterfly-spread?"
        self.long_iron_butterfly = "https://www.barchart.com/proxies/core-api/v1/options/long-iron-butterfly-spread?"
        self.short_iron_butterfly = "https://www.barchart.com/proxies/core-api/v1/options/short-iron-butterfly-spread?"

        # Condor Strategies Endpoints
        self.long_call_condor = "https://www.barchart.com/proxies/core-api/v1/options/long-call-condors?"
        self.short_call_condor = "https://www.barchart.com/proxies/core-api/v1/options/short-call-condors?"
        self.long_put_condor = "https://www.barchart.com/proxies/core-api/v1/options/long-put-condors?"
        self.short_put_condor = "https://www.barchart.com/proxies/core-api/v1/options/short-put-condors?"
        self.long_iron_condor = "https://www.barchart.com/proxies/core-api/v1/options/long-condors?"
        self.short_iron_condor = "https://www.barchart.com/proxies/core-api/v1/options/short-condors?"

        # Others
        self.earnings_dividends = "https://www.barchart.com/proxies/core-api/v1/earnings-dividends/get?"
        self.insider_trades = (
            "https://www.barchart.com/proxies/core-api/v1/insiderTrades/get?"
        )
        self.momentum = (
            "https://www.barchart.com/proxies/core-api/v1/momentum/get?"
        )
        self.sec_filings = (
            "https://www.barchart.com/proxies/core-api/v1/sec-filings/get?"
        )
