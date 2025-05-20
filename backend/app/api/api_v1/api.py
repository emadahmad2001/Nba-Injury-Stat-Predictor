from fastapi import APIRouter
from app.api.api_v1.endpoints import players, injuries, predictions, teams, auth

api_router = APIRouter()

api_router.include_router(auth.router, prefix="/auth", tags=["authentication"])
api_router.include_router(players.router, prefix="/players", tags=["players"])
api_router.include_router(injuries.router, prefix="/injuries", tags=["injuries"])
api_router.include_router(predictions.router, prefix="/predictions", tags=["predictions"])
api_router.include_router(teams.router, prefix="/teams", tags=["teams"]) 