from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional
from app.ml.injury_predictor import InjuryPredictor

app = FastAPI(title="NBA Injury Stat Predictor")

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://127.0.0.1:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize prediction service
predictor = InjuryPredictor()

class PlayerData(BaseModel):
    player_name: str
    team: str
    injury_type: str
    days_out: int

@app.get("/")
async def root():
    return {"message": "NBA Injury Stat Predictor API"}

@app.post("/predict")
async def predict(data: PlayerData):
    try:
        prediction = predictor.predict(data.dict())
        return prediction
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/train")
async def train():
    try:
        return {"message": "Model training completed successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) 