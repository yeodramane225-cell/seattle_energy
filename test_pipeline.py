from api.model_loader import load_pipeline
import pandas as pd
import numpy as np


# Charger le pipeline
pipeline = load_pipeline()

# Créer un DataFrame avec toutes les colonnes que ton pipeline attend
# On met des valeurs fictives mais réalistes
df_test = pd.DataFrame([{
    "PropertyGFATotal": 48210,
    "Latitude": 48.85,
    "Longitude": 2.35,
    "YearBuilt": 1990,
    "DataYear": 2023,
    "LargestPropertyUseType": "Office",
    "ListOfAllPropertyUseTypes": "Office,Parking",
    "ThirdLargestPropertyUseTypeGFA": 0,
    "NumberofFloors": 5,
    "AgeBuilding": 33,
    "YearsENERGYSTARCertified": 0,
    "PropertyGFATotal_log1p": 10.78,
    "SecondLargestPropertyUseTypeGFA": 0,
    "BuildingType": "Existing",
    "SecondLargestPropertyUseType": None,
    "NumberofBuildings": 1,
    "ThirdLargestPropertyUseType": None,
    "PrimaryPropertyType": "Office",
    "State": "WA",
    "PropertyGFAParking": 2000,
    "City": "Seattle",
    "LargestPropertyUseTypeGFA": 48210,
    "PropertyGFABuilding(s)": 48210
}])

# Faire la prédiction
pred_log = pipeline.predict(df_test)
print("Prédiction log:", pred_log)


# Transformer la prédiction log en valeur réelle
pred_real = np.expm1(pred_log[0])
print("Prédiction réelle :", pred_real)
