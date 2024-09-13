from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

class SentimentAnalyser:
    def __init__(self):
        self.analyzer = SentimentIntensityAnalyzer()

    def analyze(self, text):
        sentiment_scores = self.analyzer.polarity_scores(text)
        return sentiment_scores

    def classify(self, sentiment_scores):
        compound = sentiment_scores['compound']
        if compound >= 0.05:
            return 'Positive'
        elif compound <= -0.05:
            return 'Negative'
        else:
            return 'Neutral'
