from fastapi import FastAPI
from backend.models import Player
from backend.services.predictions import InjuryPredictor

app = FastAPI()
predictor = InjuryPredictor()

@app.post("/predict")
async def predict_stats(player: Player):
    return predictor.predict(player.dict())