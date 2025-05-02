from typing import Optional  # Add this import at the top
from enum import Enum
from pydantic import BaseModel

class Position(str, Enum):
    PG = "Point Guard"
    SG = "Shooting Guard"
    SF = "Small Forward"
    PF = "Power Forward"
    C = "Center"

class InjuryType(str, Enum):
    ANKLE = "Ankle Sprain"
    ACL = "ACL Tear"
    HAMSTRING = "Hamstring Strain"

class PlayerStats(BaseModel):
    points: float
    rebounds: float
    assists: float

class Player(BaseModel):
    name: str = "Player Name"  # Added default value
    position: Position
    height: float  # in inches
    weight: float  # in lbs
    injury: Optional[InjuryType] = None  # Made optional with default None
    current_stats: PlayerStats

    # Add this method for compatibility
    def dict(self):
        return super().dict()