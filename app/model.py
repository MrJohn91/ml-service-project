import pickle
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler

MODEL_PATH = "model.pkl"
scaler = StandardScaler()
model = RandomForestClassifier(n_estimators=100, random_state=42)

def train(samples):
    # Extract features and labels from samples
    features = np.array([[s["sepal_length"], s["sepal_width"], 
                         s["petal_length"], s["petal_width"]] for s in samples])
    species = [s["species"] for s in samples]
    
    # Scale features and train model
    X = scaler.fit_transform(features)
    model.fit(X, species)
    
    # Save model and scaler
    with open(MODEL_PATH, "wb") as f:
        pickle.dump((scaler, model), f)
    
    return {"message": "Model trained successfully"}

def predict(sample):
    # Load model if not already in memory
    try:
        with open(MODEL_PATH, "rb") as f:
            loaded_scaler, loaded_model = pickle.load(f)
    except:
        return "Model not trained yet"
    
    # Process input and make prediction
    features = np.array([[
        float(sample["sepal_length"]),
        float(sample["sepal_width"]),
        float(sample["petal_length"]),
        float(sample["petal_width"])
    ]])
    
    X = loaded_scaler.transform(features)
    species = loaded_model.predict(X)[0]
    
    return species