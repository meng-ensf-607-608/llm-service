from pydantic import BaseModel
from typing import List, Optional

class PatientInput(BaseModel):
    complaints: str
    age: int
    gender: str
    occupation: str
    chronic_conditions: Optional[str] = None


class Cause(BaseModel):
    cause: str
    severity: int
    symptoms: str


class HealthRecommendations(BaseModel):
    likely_causes: List[Cause]
    lifestyle_changes: List[str]
    dietary_changes: List[str]
