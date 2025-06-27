# Earnings Estimates Fields
EARNINGS_ESTIMATES_FIELDS = (
    "estimatedEarnings,estimatedEarnings1qAgo,highTargetEstimate,"
    "meanTargetEstimate,lowTargetEstimate,estimatedEarnings2qAgo,"
    "estimatedEarnings3qAgo,estimatedEarnings4qAgo,reportedEarnings1qAgo,"
    "reportedEarnings2qAgo,reportedEarnings3qAgo,reportedEarnings4qAgo,"
    "earningsDifference1qAgo,earningsDifference2qAgo,earningsDifference3qAgo,"
    "earningsDifference4qAgo,earningsSurprise1qAgo,earningsSurprise2qAgo,"
    "earningsSurprise3qAgo,earningsSurprise4qAgo"
)


class EarningsEstimatesFields:
    def __init__(self):
        self.earnings_estimates_fields = {
            "endpoint": "quote",
            "symbol_param": "symbols",
            "fields": EARNINGS_ESTIMATES_FIELDS,
            "meta": "field.shortName,field.type,field.description",
            "raw": 1,
        }
