class SentimentResult:
    def __init__(self, text, classification, scores):
        self.text = text
        self.classification = classification
        self.scores = scores

    def __str__(self):
        return f"Text: {self.text}, Classification: {self.classification}, Scores: {self.scores}"
