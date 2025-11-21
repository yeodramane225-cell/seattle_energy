from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
import pandas as pd
import numpy as np
import joblib
import os

# Charger le modèle
model_path = os.path.join(os.path.dirname(__file__), "..", "model", "pipeline.pkl")
model = joblib.load(model_path)

# Initialiser FastAPI
app = FastAPI(title="Energy Prediction API", version="0.1.0")

# Schéma d'entrée (sans features dérivées)
class EnergyInput(BaseModel):
    DataYear: int
    LargestPropertyUseType: str
    ListOfAllPropertyUseTypes: str
    ThirdLargestPropertyUseTypeGFA: float
    NumberofFloors: int
    YearsENERGYSTARCertified: int
    SecondLargestPropertyUseTypeGFA: float
    BuildingType: str
    SecondLargestPropertyUseType: str
    NumberofBuildings: int
    ThirdLargestPropertyUseType: str
    PrimaryPropertyType: str
    State: str
    PropertyGFAParking: float
    City: str
    LargestPropertyUseTypeGFA: float
    PropertyGFATotal: float
    Latitude: float
    Longitude: float
    YearBuilt: int

    # Le modèle attend cette colonne EXACTE : "PropertyGFABuilding(s)"
    PropertyGFABuilding_s: float = Field(..., alias="PropertyGFABuilding(s)")


# Endpoint de prédiction
@app.post("/predict")
def predict(data: EnergyInput):
    try:
        # On reconstruit le JSON avec l'alias pour correspondre au pipeline
        df = pd.DataFrame([data.dict(by_alias=True)])

        # Calcul des features dérivées
        df['AgeBuilding'] = df['DataYear'] - df['YearBuilt']
        df['PropertyGFATotal_log1p'] = np.log1p(df['PropertyGFATotal'])

        # Prédiction
        pred_log = model.predict(df)
        pred_real = float(np.expm1(pred_log[0]))

        return {"prediction": pred_real}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
