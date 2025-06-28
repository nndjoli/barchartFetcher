# Module: key_statistics
from urllib.parse import urlencode


def company_informations(symbols: str = "AAPL", raw: str = "1") -> str:
    """URL builder for company_informations"""
    base_url = "https://www.barchart.com/proxies/core-api/v1/quotes/get"
    params = {
        "symbols": symbols,
        "raw": raw,
        "fields": "symbolShortName,address,country,website,numberOfEmployees,phoneNumber,symbolDescription,exchange,industryGroup,industry,sicSymbol,sicDescription,sectors,tradeTime,hasOptions,hasWeeklyOptions,openPrice,highPrice,lowPrice,lastPrice,priceChange,percentChange",
        "meta": "field.shortName,field.type,field.description",
    }
    query = urlencode(params)
    return base_url + "?" + query


def growth(symbols: str = "AAPL", raw: str = "1") -> str:
    """URL builder for growth"""
    base_url = "https://www.barchart.com/proxies/core-api/v1/quotes/get"
    params = {
        "symbols": symbols,
        "raw": raw,
        "fields": "percentChange1y, percentChange3y, percentChange5y,revenueGrowth5y,earningsGrowth5y,dividendGrowth5y",
        "meta": "field.shortName,field.type,field.description",
    }
    query = urlencode(params)
    return base_url + "?" + query


def overview(symbols: str = "AAPL", raw: str = "1") -> str:
    """URL builder for overview"""
    base_url = "https://www.barchart.com/proxies/core-api/v1/quotes/get"
    params = {
        "symbols": symbols,
        "raw": raw,
        "fields": "marketCap,enterpriseValue,sharesOutstanding,annualSales,annualNetIncome,lastQuarterSales,lastQuarterIncome,ebit,ebitda,beta,percentInsider,percentInstitutional,float,floatPercentage,shortVolumeRatio",
        "meta": "field.shortName,field.type,field.description",
    }
    query = urlencode(params)
    return base_url + "?" + query


def per_share_information(symbols: str = "AAPL", raw: str = "1") -> str:
    """URL builder for per_share_information"""
    base_url = "https://www.barchart.com/proxies/core-api/v1/quotes/get"
    params = {
        "symbols": symbols,
        "raw": raw,
        "fields": "earnings,epsDate,nextEarningsDate,epsAnnual,epsGrowthQuarter,epsGrowthYear,dividendRate,dividendYield,dividend,dividendDate,dividendExDate,paymentDate,dividendPayout,split,splitDate",
        "meta": "field.shortName,field.type,field.description",
    }
    query = urlencode(params)
    return base_url + "?" + query


def ratios(symbols: str = "AAPL", raw: str = "1") -> str:
    """URL builder for ratios"""
    base_url = "https://www.barchart.com/proxies/core-api/v1/quotes/get"
    params = {
        "symbols": symbols,
        "raw": raw,
        "fields": "peRatioTrailing,peRatioForward,pegRatio,returnOnEquity,returnOnAssets,profitMargin,debtEquity,priceSales,priceCashFlow,priceBook,bookValue,interestCoverage",
        "meta": "field.shortName,field.type,field.description",
    }
    query = urlencode(params)
    return base_url + "?" + query
