from bentoml import Service, Runnable
from bentoml.io import JSON

# 1. Créez un Runnable pour exécuter la prédiction
class PredictRunnable(Runnable):
    SUPPORTED_RESOURCES = ("cpu",)
    SUPPORTS_CPU_MULTI_THREADING = True

    def run(self, input_data):
        # Remplacez ceci par votre logique réelle
        return {"result": input_data}

# 2. Créez le Service
svc = Service(name="seattle_energy_service")

# 3. Créez le runner et ajoutez-le au Service
predict_runner = PredictRunnable()
svc.add_runnable(predict_runner)

# 4. Ajoutez l'API manuellement
svc.add_api(
    predict_runner,
    name="predict",      # nom de l'API
    input=JSON(),
    output=JSON(),
)
