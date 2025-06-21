# test_simulateur.py
from simulateur import generate
import pytest

def test_generate_structure():
    data = generate()
    assert isinstance(data, dict)
    assert set(data.keys()) == {
        "timestamp", "patient_id", "heart_rate", "blood_pressure", "glucose_level"
    }

def test_heart_rate_range():
    for _ in range(10):
        data = generate()
        assert 60 <= data["heart_rate"] <= 130

def test_patient_id_known():
    patients = [
        "c5d5de7c-5cb3-4741-8ac7-7bf81eaeec50",
        "6951fc9b-715e-4e3d-8fb7-ebd561b8d97c",
        "86f061d7-6560-4916-84bb-4f8c8749f1ef"
    ]
    for _ in range(10):
        data = generate()
        assert data["patient_id"] in patients

