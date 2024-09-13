class SentimentCategory:
    @staticmethod
    def categorize(score):
        if score >= 0.75:
            return 'Very Positive'
        elif score >= 0.05:
            return 'Positive'
        elif score <= -0.75:
            return 'Very Negative'
        elif score <= -0.05:
            return 'Negative'
        else:
            return 'Neutral'
