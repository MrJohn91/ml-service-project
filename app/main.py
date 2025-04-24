from fastapi import FastAPI, HTTPException, Body, Query
from pydantic import BaseModel
from app import model, mongodb

app = FastAPI()

# model for Iris samples
class IrisSample(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float
    species: str = None

class PredictionRequest(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

# Initialize database with Iris dataset on startup
@app.on_event("startup")
def startup_event():
    mongodb.initialize_db_with_iris()

@app.post("/data")
def add_sample(sample: IrisSample):
    mongodb.insert_sample(sample.dict())
    return {"message": "Sample added"}

@app.get("/data")
def get_samples(species: str = Query(None, description="Filter by species")):
    return mongodb.get_samples(species)

@app.post("/train")
def train_model():
    samples = mongodb.get_samples()
    if not samples:
        raise HTTPException(status_code=400, detail="No data to train on")
    result = model.train(samples)
    return result

@app.post("/predict")
def predict(sample: PredictionRequest):
    prediction = model.predict(sample.dict())
    return {"species": prediction}

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.get("/metrics")
def get_metrics():
    metrics = model.get_metrics()
    if "error" in metrics:
        raise HTTPException(status_code=400, detail=metrics["error"])
    return metrics