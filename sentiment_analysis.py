from sentiment_analyser import SentimentAnalyser
from sentiment_result import SentimentResult

class SentimentAnalysis:
    def __init__(self):
        self.analyser = SentimentAnalyser()

    def analyze_text(self, text):
        scores = self.analyser.analyze(text)
        classification = self.analyser.classify(scores)
        result = SentimentResult(text, classification, scores)
        return result

# Main code to accept user input
if __name__ == "__main__":
    sentiment_analysis = SentimentAnalysis()

    # Ask the user for input
    user_input = input("Please enter a statement to analyze its sentiment: ")

    # Analyze the user's input
    result = sentiment_analysis.analyze_text(user_input)

    # Print the result
    print(result)
