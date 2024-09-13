class SentimentClassification:
    def __init__(self, classification, scores):
        self.classification = classification
        self.scores = scores

    def __str__(self):
        return f"Classification: {self.classification}, Scores: {self.scores}"
