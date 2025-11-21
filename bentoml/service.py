import bentoml
from bentoml.io import JSON
import pandas as pd

# Récupérer le modèle scikit-learn enregistré
model = bentoml.sklearn.get("energy_predictor:latest")

# Créer le service
svc = bentoml.Service("energy_predictor_service")

# Définir un endpoint
@svc.api(input=JSON(), output=JSON())
def predict(json_data):
    df = pd.DataFrame([json_data])
    predictions = model.predict(df)
    return {"prediction": predictions.tolist()}
