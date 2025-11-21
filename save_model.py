import bentoml
import joblib
from pathlib import Path

# Chemin vers ton pipeline
pipeline_path = Path("model/pipeline.pkl")

# Charger le pipeline
pipeline = joblib.load(pipeline_path)

# Enregistrer le modèle dans BentoML
bentoml.sklearn.save_model(
    "energy_predictor",  # nom du modèle dans BentoML
    pipeline,
    signatures={"predict": {"batchable": True}},  # optionnel
)

print("Modèle enregistré avec succès dans BentoML !")
