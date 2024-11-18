import pytest
from pydantic import ValidationError
from src.data_models import PatientInput, Cause, HealthRecommendation

# Test for PatientInput model
def test_patient_input_valid():
    patient_data = {
        "complaints": "Headache and fever",
        "age": 30,
        "gender": "Male",
        "occupation": "Engineer",
        "chronic_conditions": "Hypertension"
    }
    patient = PatientInput(**patient_data)
    assert patient.complaints == "Headache and fever"
    assert patient.age == 30
    assert patient.gender == "Male"
    assert patient.occupation == "Engineer"
    assert patient.chronic_conditions == "Hypertension"

def test_patient_input_optional_field():
    patient_data = {
        "complaints": "Headache and fever",
        "age": 30,
        "gender": "Male",
        "occupation": "Engineer"
    }
    patient = PatientInput(**patient_data)
    assert patient.chronic_conditions is None

def test_patient_input_invalid_age():
    with pytest.raises(ValidationError):
        PatientInput(
            complaints="Headache and fever",
            age=-5,  # Invalid negative age
            gender="Male",
            occupation="Engineer"
        )

def test_patient_input_missing_required_field():
    with pytest.raises(ValidationError):
        PatientInput(
            age=30,
            gender="Male",
            occupation="Engineer"
        )  # Missing 'complaints'

# Test for Cause model
def test_cause_valid():
    cause_data = {
        "cause": "Viral Infection",
        "severity": 2,
        "symptoms": ["Fever", "Cough"]
    }
    cause = Cause(**cause_data)
    assert cause.cause == "Viral Infection"
    assert cause.severity == 2
    assert cause.symptoms == ["Fever", "Cough"]

def test_cause_invalid_severity():
    with pytest.raises(ValidationError):
        Cause(
            cause="Viral Infection",
            severity=-1,  # Invalid negative severity
            symptoms=["Fever", "Cough"]
        )

def test_cause_missing_required_field():
    with pytest.raises(ValidationError):
        Cause(
            severity=2,
            symptoms=["Fever", "Cough"]
        )  # Missing 'cause'

# Test for HealthRecommendations model
def test_health_recommendations_valid():
    recommendations_data = {
        "likely_causes": [
            {"cause": "Viral Infection", "severity": 2, "symptoms": ["Fever", "Cough"]}
        ],
        "lifestyle_changes": ["Exercise regularly", "Reduce stress"],
        "dietary_changes": ["Increase water intake", "Eat more fruits"]
    }
    recommendations = HealthRecommendation(**recommendations_data)
    
    assert len(recommendations.likely_causes) == 1
    assert recommendations.likely_causes[0].cause == "Viral Infection"
    assert recommendations.lifestyle_changes == ["Exercise regularly", "Reduce stress"]
    assert recommendations.dietary_changes == ["Increase water intake", "Eat more fruits"]

def test_health_recommendations_missing_field():
    with pytest.raises(ValidationError):
        HealthRecommendation(
            likely_causes=[
                {"cause": "Viral Infection", "severity": 2, "symptoms": ["Fever", "Cough"]}
            ],
            lifestyle_changes=["Exercise regularly"]
            # Missing 'dietary_changes'
        )
