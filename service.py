import bentoml
from bentoml.io import JSON
import pandas as pd

# Charger le modèle BentoML
model = bentoml.sklearn.get("energy_predictor:latest")

# Créer le service
svc = bentoml.Service("energy_predictor_service")

# Définir l'API
@svc.api(input=JSON(), output=JSON())
def predict(input_data):
    df = pd.DataFrame([input_data])
    predictions = model.predict(df)
    return {"prediction": predictions.tolist()}
