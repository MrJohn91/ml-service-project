import pickle
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, f1_score, confusion_matrix
from sklearn.model_selection import train_test_split

MODEL_PATH = "model.pkl"
scaler = StandardScaler()
model = RandomForestClassifier(n_estimators=100, random_state=42)

# Global variable to store metrics
metrics = {}

def train(samples):
    global metrics
    # Extract features and labels from samples
    features = np.array([[s["sepal_length"], s["sepal_width"], 
                         s["petal_length"], s["petal_width"]] for s in samples])
    species = [s["species"] for s in samples]
    
    # Split data into training and validation sets (80-20 split)
    X_train, X_val, y_train, y_val = train_test_split(features, species, test_size=0.2, random_state=42)
    
    # Scale features and train model
    X_train_scaled = scaler.fit_transform(X_train)
    model.fit(X_train_scaled, y_train)
    
    # Scale validation set and make predictions
    X_val_scaled = scaler.transform(X_val)
    y_pred = model.predict(X_val_scaled)
    
    # Compute metrics
    accuracy = accuracy_score(y_val, y_pred)
    f1 = f1_score(y_val, y_pred, average="weighted")
    conf_matrix = confusion_matrix(y_val, y_pred, labels=["setosa", "versicolor", "virginica"]).tolist()
    
    # Store metrics
    metrics = {
        "accuracy": accuracy,
        "f1_score": f1,
        "confusion_matrix": conf_matrix
    }
    
    # Save model and scaler
    with open(MODEL_PATH, "wb") as f:
        pickle.dump((scaler, model), f)
    
    return {"message": "Model trained successfully"}

def predict(sample):
    # Load model 
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

def get_metrics():
    return metrics if metrics else {"error": "Model not trained yet"}
