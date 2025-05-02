from models import Player, PlayerStats, Position, InjuryType

def test_prediction():
    test_player = Player(
        name="Test Player",
        position=Position.PG,
        height=75,
        weight=190,
        injury=InjuryType.ANKLE,
        current_stats=PlayerStats(
            points=20,
            rebounds=5,
            assists=7
        )
    )
    
    print("Player created successfully!")
    print(test_player.dict())

if __name__ == "__main__":
    test_prediction()