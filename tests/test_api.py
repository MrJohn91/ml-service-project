import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

# Test the POST /data endpoint (adding a new sample)
def test_add_sample():
    sample = {
        "sepal_length": 5.1,
        "sepal_width": 3.5,
        "petal_length": 1.4,
        "petal_width": 0.2,
        "species": "setosa"
    }
    response = client.post("/data", json=sample)
    assert response.status_code == 200
    assert response.json() == {"message": "Sample added"}

# Test the GET /data endpoint (retrieving samples)
def test_get_samples():
    response = client.get("/data")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0  

# Test the POST /train endpoint (training the model)
def test_train_model():
    response = client.post("/train")
    assert response.status_code == 200
    assert response.json() == {"message": "Model trained successfully"}

# Test the POST /predict endpoint (predicting species)
def test_predict():
    sample = {
        "sepal_length": 5.1,
        "sepal_width": 3.5,
        "petal_length": 1.4,
        "petal_width": 0.2
    }
    response = client.post("/predict", json=sample)
    assert response.status_code == 200
    assert response.json() == {"species": "setosa"}

# Test the GET /health endpoint
def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}
