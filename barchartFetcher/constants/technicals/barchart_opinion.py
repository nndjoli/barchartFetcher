# Opinion Fields
OPINION_FIELDS = (
    "opinion,opinionSignal,opinionPercent,opinionStrength,opinionDirection,"
    "opinionChange,opinionPrevious,opinionPreviousSignal,opinionPreviousPercent,"
    "opinionLastWeek,opinionLastWeekSignal,opinionLastWeekPercent,opinionLastMonth,"
    "opinionLastMonthSignal,opinionLastMonthPercent,opinionShortTerm,"
    "opinionShortTermSignal,opinionShortTermPercent,opinionMediumTerm,"
    "opinionMediumTermSignal,opinionMediumTermPercent,opinionLongTerm,"
    "opinionLongTermSignal,opinionLongTermPercent"
)

# Composite Indicator Fields
COMPOSITE_INDICATOR_FIELDS = (
    "trendSpotterSignal,trendSpotterStrength,trendSpotterDirection"
)

# Short Term Indicators Fields
SHORT_TERM_INDICATORS_FIELDS = (
    "movingAverage20dSignal,movingAverage20dStrength,movingAverage20dDirection,"
    "macd20to50dSignal,macd20to50dStrength,macd20to50dDirection,macd20to100dSignal,"
    "macd20to100dStrength,macd20to100dDirection,macd20to200dSignal,"
    "macd20to200dStrength,macd20to200dDirection"
)

# Medium Term Indicators Fields
MEDIUM_TERM_INDICATORS_FIELDS = (
    "movingAverage50dSignal,movingAverage50dStrength,movingAverage50dDirection,"
    "macd50to100dSignal,macd50to100dStrength,macd50to100dDirection,"
    "macd50to150dSignal,macd50to150dStrength,macd50to150dDirection,"
    "macd50to200dSignal,macd50to200dStrength,macd50to200dDirection"
)

# Long Term Indicators Fields
LONG_TERM_INDICATORS_FIELDS = (
    "movingAverage100dSignal,movingAverage100dStrength,movingAverage100dDirection,"
    "movingAverage150dSignal,movingAverage150dStrength,movingAverage150dDirection,"
    "movingAverage200dSignal,movingAverage200dStrength,movingAverage200dDirection,"
    "macd100to200dSignal,macd100to200dStrength,macd100to200dDirection"
)


class OpinionFields:

    def __init__(self):
        self.fields = OPINION_FIELDS
        self.composite_indicator_fields = COMPOSITE_INDICATOR_FIELDS
        self.short_term_indicators_fields = SHORT_TERM_INDICATORS_FIELDS
        self.medium_term_indicators_fields = MEDIUM_TERM_INDICATORS_FIELDS
        self.long_term_indicators_fields = LONG_TERM_INDICATORS_FIELDS
