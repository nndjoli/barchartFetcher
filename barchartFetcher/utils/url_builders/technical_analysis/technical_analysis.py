# Module: technical_analysis
from urllib.parse import urlencode


def moving_averages(symbols: str = "AAPL", raw: int = 1) -> str:
    """URL builder for moving_averages"""
    base_url = "https://www.barchart.com/proxies/core-api/v1/quotes/get"
    params = {
        "symbols": symbols,
        "raw": raw,
        "fields": "movingAverage5d,priceChange5d,percentChange5d,averageVolume5d,movingAverage20d,priceChange20d,percentChange20d,averageVolume20d,movingAverage50d,priceChange50d,percentChange50d,averageVolume50d,movingAverage100d,priceChange100d,percentChange100d,averageVolume100d,movingAverage200d,priceChange200d,percentChange200d,averageVolume200d,movingAverageYtd,priceChangeYtd,percentChangeYtd,averageVolumeYtd",
        "meta": "field.shortName,field.description,field.type",
    }
    query = urlencode(params)
    return base_url + "?" + query


def stochastics(symbols: str = "AAPL", raw: int = 1) -> str:
    """URL builder for stochastics"""
    base_url = "https://www.barchart.com/proxies/core-api/v1/quotes/get"
    params = {
        "symbols": symbols,
        "raw": raw,
        "fields": "rawStochastic9d,rawStochastic14d,rawStochastic20d,rawStochastic50d,rawStochastic100d,stochasticK9d,stochasticK14d,stochasticK20d,stochasticK50d,stochasticK100d,stochasticD9d,stochasticD14d,stochasticD20d,stochasticD50d,stochasticD100d,averageTrueRange9d,averageTrueRange14d,averageTrueRange20d,averageTrueRange50d,averageTrueRange100d",
        "meta": "field.shortName,field.description,field.type",
    }
    query = urlencode(params)
    return base_url + "?" + query


def strength(symbols: str = "AAPL", raw: int = 1) -> str:
    """URL builder for strength"""
    base_url = "https://www.barchart.com/proxies/core-api/v1/quotes/get"
    params = {
        "symbols": symbols,
        "raw": raw,
        "fields": "relativeStrength5d,relativeStrength9d,relativeStrength14d,relativeStrength20d,relativeStrength50d,relativeStrength100d,percentR9d,percentR14d,percentR20d,percentR50d,percentR100d,historicVolatility9d,historicVolatility14d,historicVolatility20d,historicVolatility30d,historicVolatility50d,historicVolatility90d,historicVolatility100d,macdOscillator9d,macdOscillator14d,macdOscillator20d,macdOscillator50d,macdOscillator100d",
        "meta": "field.shortName,field.description,field.type",
    }
    query = urlencode(params)
    return base_url + "?" + query
