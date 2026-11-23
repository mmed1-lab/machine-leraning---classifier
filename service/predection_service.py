import joblib
from typing import Any
from ml_model.cleaning import clean_text

class SentimentPredictionService:
    
    SENTIMENTS = {0: 'neutral', 1: 'negative', 2: 'positive'}

    def __init__(self):
        self.model = joblib.load('./ml_model/svc.joblib')
        self.encoder = joblib.load('./ml_model/encoder.joblib')
        
    
    def predictSentiment(self, text: str) -> dict[str, Any]:

        text = clean_text(text)
        vector = self.encoder.encode(text)

        result_id = self.model.predict([vector])[0]
        result = self.SENTIMENTS[int(result_id)].capitalize()

        proba = self.model.predict_proba([vector])[0]

        probs = {
            self.SENTIMENTS[int(c)]: float(p)
            for c, p in zip(self.model.classes_, proba)
        }

        return {
            'sentiment': result,
            'probabilities': probs
        }



sentimentPrediction = SentimentPredictionService()