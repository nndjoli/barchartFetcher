# Module: overview
from urllib.parse import urlencode


def analyst_rating(symbols: str = "AAPL", raw: str = "1") -> str:
    """URL builder for analyst_rating"""
    base_url = "https://www.barchart.com/proxies/core-api/v1/quotes/get"
    params = {
        "symbols": symbols,
        "raw": raw,
        "fields": "averageRecommendation,totalRecommendations,estimatedEarnings,estimatedEarnings1qAgo,highTargetEstimate,meanTargetEstimate,lowTargetEstimate",
        "meta": "field.shortName,field.description,field.type",
    }
    query = urlencode(params)
    return base_url + "?" + query


def fundamentals(symbols: str = "AAPL", raw: str = "1") -> str:
    """URL builder for fundamentals"""
    base_url = "https://www.barchart.com/proxies/core-api/v1/quotes/get"
    params = {
        "symbols": symbols,
        "raw": raw,
        "fields": "marketCap,sharesOutstanding,annualSales,annualNetIncome,ebit,ebitda,beta,priceSales,priceCashFlow,priceBook,peRatioTrailing,epsAnnual,earnings,epsDate,nextEarningsDate,dividendRate,dividendYield,dividend,dividendDate,dividendExDate,industryGroup,sectors",
        "meta": "field.shortName,field.description,field.type",
    }
    query = urlencode(params)
    return base_url + "?" + query


def options_overview(symbols: str = "AAPL", raw: str = "1") -> str:
    """URL builder for options_overview"""
    base_url = "https://www.barchart.com/proxies/core-api/v1/quotes/get"
    params = {
        "symbols": symbols,
        "raw": raw,
        "fields": "optionsWeightedImpliedVolatility,optionsWeightedImpliedVolatilityChange,historicVolatility30d,optionsImpliedVolatilityPercentile1y,optionsImpliedVolatilityRank1y,optionsWeightedImpliedVolatilityHigh1y,optionsWeightedImpliedVolatilityHighDate1y,optionsWeightedImpliedVolatilityLow1y,optionsWeightedImpliedVolatilityLowDate1y,optionsPutCallVolumeRatio,optionsTotalVolume,optionsTotalVolume1m,optionsPutCallOpenInterestRatio,optionsTotalOpenInterest,optionsTotalOpenInterest1m",
        "meta": "field.shortName,field.description,field.type",
    }
    query = urlencode(params)
    return base_url + "?" + query


def price_performance(symbols: str = "AAPL", raw: str = "1") -> str:
    """URL builder for price_performance"""
    base_url = "https://www.barchart.com/proxies/core-api/v1/quotes/get"
    params = {
        "symbols": symbols,
        "raw": raw,
        "fields": "highPrice1m,highDate1m,lowPrice1m,lowDate1m,priceChange1m,percentChange1m,highPrice3m,highDate3m,lowPrice3m,lowDate3m,priceChange3m,percentChange3m,highPrice1y,highDate1y,lowPrice1y,lowDate1y,priceChange1y,percentChange1y",
        "meta": "field.shortName,field.description,field.type",
    }
    query = urlencode(params)
    return base_url + "?" + query


def quote(symbols: str = "AAPL", raw: str = "1") -> str:
    """URL builder for quote"""
    base_url = "https://www.barchart.com/proxies/core-api/v1/quotes/get"
    params = {
        "symbols": symbols,
        "raw": raw,
        "fields": "lowPrice,highPrice,openPrice,lastPrice,volume,averageVolume20d,stochasticK14d,weightedAlpha,priceChange5d,percentChange5d,rangePercent1y,highPrice1y,lowPrice1y",
        "meta": "field.shortName,field.description,field.type",
    }
    query = urlencode(params)
    return base_url + "?" + query


def technical_opinion(symbols: str = "AAPL", raw: str = "1") -> str:
    """URL builder for technical_opinion"""
    base_url = "https://www.barchart.com/proxies/core-api/v1/quotes/get"
    params = {
        "symbols": symbols,
        "raw": raw,
        "fields": "opinion,opinionSignal,opinionPercent,opinionStrength,opinionDirection,opinionChange",
        "meta": "field.shortName,field.description,field.type",
    }
    query = urlencode(params)
    return base_url + "?" + query
