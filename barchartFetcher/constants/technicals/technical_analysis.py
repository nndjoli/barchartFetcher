# Moving Average fields
MA_FIELDS = (
    "movingAverage5d,priceChange5d,percentChange5d,averageVolume5d,movingAverage20d,"
    "priceChange20d,percentChange20d,averageVolume20d,movingAverage50d,"
    "priceChange50d,percentChange50d,averageVolume50d,movingAverage100d,"
    "priceChange100d,percentChange100d,averageVolume100d,movingAverage200d,"
    "priceChange200d,percentChange200d,averageVolume200d,movingAverageYtd,"
    "priceChangeYtd,percentChangeYtd,averageVolumeYtd"
)

# Stochastic and ATR fields
STOCHASTICS_FIELDS = (
    "rawStochastic9d,rawStochastic14d,rawStochastic20d,rawStochastic50d,"
    "rawStochastic100d,stochasticK9d,stochasticK14d,stochasticK20d,stochasticK50d,"
    "stochasticK100d,stochasticD9d,stochasticD14d,stochasticD20d,stochasticD50d,"
    "stochasticD100d,averageTrueRange9d,averageTrueRange14d,averageTrueRange20d,"
    "averageTrueRange50d,averageTrueRange100d"
)

# Relative Strength and Volatility fields
STRENGTH_FIELDS = (
    "relativeStrength5d,relativeStrength9d,relativeStrength14d,relativeStrength20d,"
    "relativeStrength50d,relativeStrength100d,percentR9d,percentR14d,percentR20d,"
    "percentR50d,percentR100d,historicVolatility9d,historicVolatility14d,"
    "historicVolatility20d,historicVolatility30d,historicVolatility50d,"
    "historicVolatility90d,historicVolatility100d,macdOscillator9d,"
    "macdOscillator14d,macdOscillator20d,macdOscillator50d,macdOscillator100d"
)


class TechnicalAnalysisFields:
    def __init__(self):
        self.ma_fields = MA_FIELDS
        self.stochastics_fields = STOCHASTICS_FIELDS
        self.strength_fields = STRENGTH_FIELDS
