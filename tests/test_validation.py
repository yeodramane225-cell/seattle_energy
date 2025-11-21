import pytest
from api.validation import EnergyInput
from pydantic import ValidationError

def test_energy_input_valid():
    data = {
        "PropertyGFATotal": 48210,
        "Latitude": 48.85,
        "Longitude": 2.35,
        "YearBuilt": 1990
    }
    e = EnergyInput(**data)
    assert e.PropertyGFATotal == 48210

def test_energy_input_invalid():
    data = {
        "PropertyGFATotal": 500,  # trop petit
        "Latitude": 48.85,
        "Longitude": 2.35,
        "YearBuilt": 1990
    }
    with pytest.raises(ValidationError):
        EnergyInput(**data)
