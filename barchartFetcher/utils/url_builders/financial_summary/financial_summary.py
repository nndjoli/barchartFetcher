# Module: financial_summary
from urllib.parse import urlencode


def financial_summary_q(symbols: str = "AAPL", raw: int = 1) -> str:
    """URL builder for financial_summary_q"""
    base_url = "https://www.barchart.com/proxies/core-api/v1/quotes/get"
    params = {
        "symbols": symbols,
        "raw": raw,
        "fields": "symbol,revenueLastQuarter,revenue1qAgo,revenue2qAgo,revenue3qAgo,revenue4qAgo,revenueGrowthLastQuarter,revenueGrowth1qAgo,revenueGrowth2qAgo,revenueGrowth3qAgo,revenueGrowth4qAgo,netIncomeLastQuarter,netIncome1qAgo,netIncome2qAgo,netIncome3qAgo,netIncome4qAgo,netIncomeGrowthLastQuarter,netIncomeGrowth1qAgo,netIncomeGrowth2qAgo,netIncomeGrowth3qAgo,netIncomeGrowth4qAgo,assetLastQuarter,asset1qAgo,asset2qAgo,asset3qAgo,asset4qAgo,assetGrowthLastQuarter,assetGrowth1qAgo,assetGrowth2qAgo,assetGrowth3qAgo,assetGrowth4qAgo,liabilityLastQuarter,liability1qAgo,liability2qAgo,liability3qAgo,liability4qAgo,liabilityGrowthLastQuarter,liabilityGrowth1qAgo,liabilityGrowth2qAgo,liabilityGrowth3qAgo,liabilityGrowth4qAgo,cashFlowLastQuarter,cashFlow1qAgo,cashFlow2qAgo,cashFlow3qAgo,cashFlow4qAgo,cashFlowGrowthLastQuarter,cashFlowGrowth1qAgo,cashFlowGrowth2qAgo,cashFlowGrowth3qAgo,cashFlowGrowth4qAgo,changeCashLastQuarter,changeCash1qAgo,changeCash2qAgo,changeCash3qAgo,changeCash4qAgo,changeCashGrowthLastQuarter,changeCashGrowth1qAgo,changeCashGrowth2qAgo,changeCashGrowth3qAgo,changeCashGrowth4qAgo",
        "meta": "field.shortName,field.type,field.description",
    }
    query = urlencode(params)
    return base_url + "?" + query


def financial_summary_y(symbols: str = "AAPL", raw: int = 1) -> str:
    """URL builder for financial_summary_y"""
    base_url = "https://www.barchart.com/proxies/core-api/v1/quotes/get"
    params = {
        "symbols": symbols,
        "raw": raw,
        "fields": "symbol,revenueLastYear,revenue1yAgo,revenue2yAgo,revenue3yAgo,revenue4yAgo,revenueGrowthLastYearrevenueGrowth1yAgo,revenueGrowth2yAgo,revenueGrowth3yAgo,revenueGrowth4yAgo,netIncomeLastYear,netIncome1yAgo,netIncome2yAgo,netIncome3yAgo,netIncome4yAgo,netIncomeGrowthLastYear,netIncomeGrowth1yAgo,netIncomeGrowth2yAgo,netIncomeGrowth3yAgo,netIncomeGrowth4yAgo,assetLastYear,asset1yAgo,asset2yAgo,asset3yAgo,asset4yAgo,assetGrowthLastYear,assetGrowth1yAgo,assetGrowth2yAgo,assetGrowth3yAgo,assetGrowth4yAgo,liabilityLastYear,liability1yAgo,liability2yAgo,liability3yAgo,liability4yAgo,liabilityGrowthLastYear,liabilityGrowth1yAgo,liabilityGrowth2yAgo,liabilityGrowth3yAgo,liabilityGrowth4yAgo,cashFlowLastYear,cashFlow1yAgo,cashFlow2yAgo,cashFlow3yAgo,cashFlow4yAgo,cashFlowGrowthLastYear,cashFlowGrowth1yAgo,cashFlowGrowth2yAgo,cashFlowGrowth3yAgo,cashFlowGrowth4yAgo,changeCashLastYear,changeCash1yAgo,changeCash2yAgo,changeCash3yAgo,changeCash4yAgo,changeCashGrowthLastYear,changeCashGrowth1yAgo,changeCashGrowth2yAgo,changeCashGrowth3yAgo,changeCashGrowth4yAgo",
        "meta": "field.shortName,field.type,field.description",
    }
    query = urlencode(params)
    return base_url + "?" + query
