import numpy as np
from sklearn.linear_model import LinearRegression
import pandas as pd

class Player:
    def __init__(self, position, height, weight, injury, current_stats):
        self.position = position
        self.height = height
        self.weight = weight
        self.injury = injury
        self.current_stats = current_stats

    def predict_stats(self):
        # Create a dataframe with the player's attributes
        df = pd.DataFrame({
            'position': [self.position],
            'height': [self.height],
            'weight': [self.weight],
            'injury': [self.injury],
            'current_points': [self.current_stats[0]],
            'current_rebounds': [self.current_stats[1]],
            'current_assists': [self.current_stats[2]]
        })

        # Convert categorical variables to numerical variables
        df['position'] = df['position'].map({
            'point guard': 0,
            'shooting guard': 1,
            'small forward': 2,
            'power forward': 3,
            'center': 4
        })

        df['injury'] = df['injury'].map({
            'ankle sprain': 0,
            'ACL tear': 1,
            'broken arm': 2
        })

        # Create a linear regression model
        model = LinearRegression()

        # Train the model on the player's attributes
        model.fit(df[['position', 'height', 'weight', 'injury', 'current_points', 'current_rebounds', 'current_assists']], df[['current_points', 'current_rebounds', 'current_assists']])

        # Predict the player's stats
        predicted_stats = model.predict(df[['position', 'height', 'weight', 'injury', 'current_points', 'current_rebounds', 'current_assists']])

        return predicted_stats[0]

# Create a player object
player = Player('point guard', 6.2, 180.5, 'ankle sprain', [20.5, 5.2, 7.8])

# Predict the player's stats
predicted_stats = player.predict_stats()

print('Predicted Stats:')
print('Points:', predicted_stats[0])
print('Rebounds:', predicted_stats[1])
print('Assists:', predicted_stats[2])
