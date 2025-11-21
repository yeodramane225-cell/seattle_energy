import joblib
import os

MODEL_PATH = os.path.join(os.path.dirname(__file__), "..", "model", "pipeline.pkl")

def load_pipeline():
    """Charge le pipeline complet (préprocessing + modèle)."""
    pipeline = joblib.load(MODEL_PATH)
    return pipeline
