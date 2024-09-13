import unittest
from sentiment_analyser import SentimentAnalyser

class TestSentimentAnalyser(unittest.TestCase):
    def setUp(self):
        self.analyser = SentimentAnalyser()

    def test_positive_sentiment(self):
        scores = self.analyser.analyze("I love this!")
        self.assertEqual(self.analyser.classify(scores), 'Positive')

    def test_negative_sentiment(self):
        scores = self.analyser.analyze("I hate this!")
        self.assertEqual(self.analyser.classify(scores), 'Negative')

    def test_neutral_sentiment(self):
        scores = self.analyser.analyze("This is okay.")
        self.assertEqual(self.analyser.classify(scores), 'Neutral')

if __name__ == "__main__":
    unittest.main()
