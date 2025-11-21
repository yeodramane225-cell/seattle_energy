import pandas as pd
import numpy as np

def preprocess_input(data: dict) -> pd.DataFrame:
    """
    Prépare les données pour le modèle : renomme les colonnes,
    calcule les features dérivées et produit une DataFrame propre.
    """

    # Convertir en DataFrame
    df = pd.DataFrame([data])

    # Renommer PropertyGFABuilding_s -> PropertyGFABuilding(s)
    if "PropertyGFABuilding_s" in df.columns:
        df = df.rename(columns={"PropertyGFABuilding_s": "PropertyGFABuilding(s)"})

    # --- Calculs automatiques obligatoires ---

    # AgeBuilding = DataYear - YearBuilt
    df["AgeBuilding"] = df["DataYear"] - df["YearBuilt"]

    # PropertyGFATotal_log1p = log1p(PropertyGFATotal)
    df["PropertyGFATotal_log1p"] = np.log1p(df["PropertyGFATotal"])

    return df
