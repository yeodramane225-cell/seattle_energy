FROM python:3.11-slim

# Installer BentoML et dépendances
RUN pip install --no-cache-dir bentoml==1.4.29 pandas scikit-learn numpy pydantic

WORKDIR /app

# Copier le code et le modèle
COPY service.py .
COPY model ./model

EXPOSE 3000

# Lancer le service
CMD ["python", "-m", "bentoml", "serve", "service:svc", "--reload"]
