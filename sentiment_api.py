from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Define input model
class TextInput(BaseModel):
    text: str
    
# Define output model
class SentimentOutput(BaseModel):
    sentiment: str
    score: float
    
# Fake AI function
def sentiment_analysis(text: str) -> SentimentOutput:
    if 'love' in text.lower():
        return SentimentOutput(sentiment='positive', score=0.95)
    elif 'hate' in text.lower():
        return SentimentOutput(sentiment='negative', score=0.05)
    else:
        return SentimentOutput(sentiment='neural', score=0.5)
    
# API endpoint that use the model
@app.post("/analyze/", response_model=SentimentOutput)
def analyze_text(input: TextInput):
    return sentiment_analysis(input.text)