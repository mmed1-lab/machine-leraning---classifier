# fast API entry point


from fastapi import FastAPI
from routes.product_routes import router as product_router
from service.predection_service import sentimentPrediction
from typing import Any
from models.Sentiment import Sentiment

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(product_router)


@app.get("/")
def home():
    return {"message": "Product Sentiment API is running"}


@app.post('/predict-sentiment')
def sentiment(sentiment: Sentiment) -> dict[str, Any]:
    return sentimentPrediction.predictSentiment(sentiment.text)
