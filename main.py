from fastapi import FastAPI
from pydantic import BaseModel
from sentiment_analyser import SentimentAnalyser
from sentiment_result import SentimentResult
from fastapi.middleware.cors import CORSMiddleware

# Initialize FastAPI app
app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize the sentiment analyzer
analyser = SentimentAnalyser()

# Request model for user input
class SentimentRequest(BaseModel):
    text: str

# Response model for sentiment analysis result
class SentimentResponse(BaseModel):
    text: str
    classification: str
    scores: dict

# Endpoint for sentiment analysis
@app.post("/analyze", response_model=SentimentResponse)
def analyze_sentiment(request: SentimentRequest):
    print(request.text)
    # Analyze the input text
    sentiment_scores = analyser.analyze(request.text)
    classification = analyser.classify(sentiment_scores)
    result = SentimentResult(request.text, classification, sentiment_scores)

    # Return the result as a response
    return SentimentResponse(
        text=result.text,
        classification=result.classification,
        scores=result.scores
    )
