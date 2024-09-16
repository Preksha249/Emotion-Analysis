# Emotion-Analysis

1. SentimentAnalyser.java → SentimentAnalyser.py
We can use nltk or vaderSentiment for sentiment analysis in Python.

2. SentimentClassification.java → SentimentClassification.py
This class can be represented as a simple container for sentiment results:

3. SentimentResult.java → SentimentResult.py
This class could store the results of sentiment analysis similarly to SentimentClassification, or it could store more detailed information

4. SentimentAnalysis.java → SentimentAnalysis.py
This file could serve as the main driver in Python to process input and output the sentiment classification

5. posit.java, negat.java, neut.java, vposit.java, vnegat.java → Positive, Negative, Neutral Classes
In Python, these could be handled with threshold definitions and custom categories:


GENERAL FLOW IN PYTHON:
- The text input is sent to the SentimentAnalyser class, which uses vaderSentiment to analyze the sentiment.
- Based on the sentiment scores, the text is classified as positive, negative, or neutral using the classify method.
- The results are stored in SentimentResult and can be further processed or printed.


STRUCTURE OF THE CODE: 
sentiment_analysis_project/
│
├── sentiment_analyser.py            # Main Sentiment Analysis logic
├── sentiment_classification.py      # Class for storing sentiment classification
├── sentiment_result.py              # Class for storing the result of sentiment analysis
├── sentiment_analysis.py            # Orchestrator/Driver code
├── sentiment_categories.py          # Handles sentiment thresholds and categorization
├── main.py                          # FastAPI application
├── test_sentiment_analysis.py       # Unit tests for your project
└── README.md                        # Project description and setup guide


DEPENDENCIES:
- install venderSentiment using: `pip install vaderSentiment`
- install FastAPI and Uvicorn: `pip install fastapi uvicorn`
- main.py contains the fastAPI API

EXPLANNATION OF API CODE:
- FastAPI instance: We create a FastAPI app using FastAPI().
- Pydantic Models: We use Pydantic models (SentimentRequest and SentimentResponse) to define the request and response data formats. The SentimentRequest model expects the user to send a string (text), and the SentimentResponse will return the analyzed text, its classification, and sentiment scores.
- API Endpoint: The /analyze endpoint accepts POST requests. The input text is processed by the analyser, and the result is returned in the response.


RUNNING THE PROGRAM (FastAPI application)
to run we need to use *uvicorn* to serve the application. 
command: `uvicorn main:app --reload`
  - app: refers to the FastAPI instance we created in the file.
  - --reload: enables hot-reloading so that the server restarts automatically when changes are made to the code. 


ACCESSING THE API

- url: - http://127.0.0.1:8000/analyze -
- method: POST
- Body (JSON format):
   {
    "text": " sentence..."
   }
  use postman or curl to test
or
   run on browser:
     - http://127.0.0.1:8000/docs - 
   testing with curl:
     -         curl -X 'POST' \  'http://127.0.0.1:8000/analyze' \ -H 'Content-Type: application/json' \-d '{"text": "I love FastAPI!"}'

Deployed in 'Railway'
 - create a Procfile in the root directory. and then paste `web: gunicorn -w 4 -k uvicorn.workers.UvicornWorker main:app`
     web: This tells Railway that this is the web process.
     gunicorn -w 4 -k uvicorn.workers.UvicornWorker main:app: This command tells Railway to use gunicorn with 4 worker threads (-w 4) and to serve the FastAPI app using Uvicorn (main:app). Here, main is the Python file main.py, and app is the FastAPI instance in that file.
 - then run the two commands:
        `pip install gunicorn`
        `pip freeze > requirements.txt`
       






