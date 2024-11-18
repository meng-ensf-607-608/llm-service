from pydantic import BaseModel, PositiveInt
from typing import List, Optional

class PatientInput(BaseModel):
    complaints: str
    age: PositiveInt
    gender: str
    occupation: str
    chronic_conditions: Optional[str] = None


class Cause(BaseModel):
    cause: str
    severity: PositiveInt
    symptoms: List[str]


class HealthRecommendation(BaseModel):
    likely_causes: List[Cause]
    lifestyle_changes: List[str]
    dietary_changes: List[str]
