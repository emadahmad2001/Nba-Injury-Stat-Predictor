# services/prediction.py
from sklearn.ensemble import GradientBoostingRegressor
import joblib
import pandas as pd

class InjuryPredictor:
    def __init__(self):
        self.model = GradientBoostingRegressor()
        # Load pre-trained model or train new one
        try:
            self.model = joblib.load('models/injury_model.pkl')
        except:
            self.train_model()
    
    def train_model(self, data_path='data/nba_players.csv'):
        df = pd.read_csv(data_path)
        # Feature engineering here
        X = df[['position', 'height', 'weight', 'injury', 'games_missed']]
        y = df[['points', 'rebounds', 'assists']]
        self.model.fit(X, y)
        joblib.dump(self.model, 'models/injury_model.pkl')
    
    def predict(self, player_data: dict) -> dict:
        df = pd.DataFrame([player_data])
        prediction = self.model.predict(df)
        return {
            'points': prediction[0][0],
            'rebounds': prediction[0][1],
            'assists': prediction[0][2]
        }