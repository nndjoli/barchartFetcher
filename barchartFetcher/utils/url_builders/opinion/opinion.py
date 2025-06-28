# Module: opinion
from urllib.parse import urlencode
import re

def composite_indicator(symbols: str = 'AAPL', raw: str = '1') -> str:
    """URL builder for composite_indicator"""
    base_url = 'https://www.barchart.com/proxies/core-api/v1/quotes/get'
    params = {
        'symbols': symbols,
        'raw': raw,
        'fields': 'trendSpotterSignal,trendSpotterStrength,trendSpotterDirection',
        'meta': 'field.shortName,fields.description,field.type',
    }
    query = urlencode(params)
    return base_url + '?' + query

def long_term_indicators(symbols: str = 'AAPL', raw: str = '1') -> str:
    """URL builder for long_term_indicators"""
    base_url = 'https://www.barchart.com/proxies/core-api/v1/quotes/get'
    params = {
        'symbols': symbols,
        'raw': raw,
        'fields': 'movingAverage100dSignal,movingAverage100dStrength,movingAverage100dDirection,movingAverage150dSignal,movingAverage150dStrength,movingAverage150dDirection,movingAverage200dSignal,movingAverage200dStrength,movingAverage200dDirection,macd100to200dSignal,macd100to200dStrength,macd100to200dDirection',
        'meta': 'field.shortName,field.description,field.type',
    }
    query = urlencode(params)
    return base_url + '?' + query

def medium_term_indicators(symbols: str = 'AAPL', raw: str = '1') -> str:
    """URL builder for medium_term_indicators"""
    base_url = 'https://www.barchart.com/proxies/core-api/v1/quotes/get'
    params = {
        'symbols': symbols,
        'raw': raw,
        'fields': 'movingAverage50dSignal,movingAverage50dStrength,movingAverage50dDirection,macd50to100dSignal,macd50to100dStrength,macd50to100dDirection,macd50to150dSignal,macd50to150dStrength,macd50to150dDirection,macd50to200dSignal,macd50to200dStrength,macd50to200dDirection',
        'meta': 'field.shortName,field.description,field.type',
    }
    query = urlencode(params)
    return base_url + '?' + query

def opinion(symbols: str = 'AAPL', raw: str = '1') -> str:
    """URL builder for opinion"""
    base_url = 'https://www.barchart.com/proxies/core-api/v1/quotes/get'
    params = {
        'symbols': symbols,
        'raw': raw,
        'fields': 'opinion,opinionSignal,opinionPercent,opinionStrength,opinionDirection,opinionChange,opinionPrevious,opinionPreviousSignal,opinionPreviousPercent,opinionLastWeek,opinionLastWeekSignal,opinionLastWeekPercent,opinionLastMonth,opinionLastMonthSignal,opinionLastMonthPercent,opinionShortTerm,opinionShortTermSignal,opinionShortTermPercent,opinionMediumTerm,opinionMediumTermSignal,opinionMediumTermPercent,opinionLongTerm,opinionLongTermSignal,opinionLongTermPercent',
        'meta': 'field.shortName,field.description,field.type',
    }
    query = urlencode(params)
    return base_url + '?' + query

def short_term_indicators(symbols: str = 'AAPL', raw: str = '1') -> str:
    """URL builder for short_term_indicators"""
    base_url = 'https://www.barchart.com/proxies/core-api/v1/quotes/get'
    params = {
        'symbols': symbols,
        'raw': raw,
        'fields': 'movingAverage20dSignal,movingAverage20dStrength,movingAverage20dDirection,macd20to50dSignal,macd20to50dStrength,macd20to50dDirection,macd20to100dSignal,macd20to100dStrength,macd20to100dDirection,macd20to200dSignal,macd20to200dStrength,macd20to200dDirection',
        'meta': 'field.shortName,field.description,field.type',
    }
    query = urlencode(params)
    return base_url + '?' + query
