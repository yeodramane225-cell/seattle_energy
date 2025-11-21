import bentoml
from service_manual import svc

# Crée et enregistre le Bento
bento = bentoml.Bento.create(
    svc,
    version="v1",  # numéro de version du Bento
    description="Seattle Energy Service"
)

bento.save()
print(f"Bento créé avec succès : {bento.path}")
