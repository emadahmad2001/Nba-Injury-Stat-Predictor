# models.py
from pydantic import BaseModel
from enum import Enum

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
    # Add more injury types

class PlayerStats(BaseModel):
    points: float
    rebounds: float
    assists: float
    # Additional stats

class Player(BaseModel):
    name: str
    position: Position
    height: float  # in inches
    weight: float  # in lbs
    injury: Optional[InjuryType]
    current_stats: PlayerStats