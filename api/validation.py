from pydantic import BaseModel, Field
from typing import Optional

class EnergyInput(BaseModel):
    DataYear: int = Field(..., ge=2000, le=2025)
    BuildingType: str
    PrimaryPropertyType: str
    YearBuilt: int = Field(..., ge=1900, le=2025)
    NumberofBuildings: int = Field(..., gt=0)
    NumberofFloors: int = Field(..., gt=0)
    PropertyGFATotal: float = Field(..., gt=1000)
    PropertyGFABuilding_s: float = Field(..., gt=0)  # remplace les parenthèses par "_s"
    PropertyGFAParking: float = Field(..., ge=0)
    ListOfAllPropertyUseTypes: str
    LargestPropertyUseType: str
    LargestPropertyUseTypeGFA: float = Field(..., ge=0)
    SecondLargestPropertyUseType: Optional[str] = Field(default=None)
    SecondLargestPropertyUseTypeGFA: Optional[float] = Field(default=0.0, ge=0)
    ThirdLargestPropertyUseType: Optional[str] = Field(default=None)
    ThirdLargestPropertyUseTypeGFA: Optional[float] = Field(default=0.0, ge=0)
    Latitude: float = Field(..., ge=-90, le=90)
    Longitude: float = Field(..., ge=-180, le=180)
    City: str
    State: str
    YearsENERGYSTARCertified: int = Field(..., ge=0)
