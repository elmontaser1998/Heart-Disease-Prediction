import joblib
from fastapi import FastAPI
import numpy as np

# Charger le modèle
model = joblib.load("best_model.joblib")
classe_name = np.array(['no disease', 'disease'])

app = FastAPI()

@app.get('/')
def read_root():
    return {'message': 'Heart disease Prediction'}

@app.post("/predict")
def predict(data: dict):    
    # Vérifier si 'features' est bien dans les données reçues
    if 'features' not in data:
        return {"error": "The 'features' key is missing from the input data"}

    # Charger les caractéristiques et les transformer en tableau NumPy pour la prédiction
    features = np.array(data['features']).reshape(1, -1)
    
    # Effectuer la prédiction
    prediction = model.predict(features)  
    predicted_class = classe_name[prediction][0] 
    
    return {"prediction_class": predicted_class}
