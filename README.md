# ml-service-project

## Setup
## docker-compose up --build

## Service runs on http://localhost:8000

## Endpoints

## POST /data – Adds an Iris sample{ "sepal_length": 5.1, "sepal_width": 3.5, "petal_length": 1.4, "petal_width": 0.2, "species": "setosa" }
## GET /data?species=... – List Iris samples
## POST /train – Train the model
## POST /predict – Predict species from input{ "sepal_length": 5.1, "sepal_width": 3.5, "petal_length": 1.4, "petal_width": 0.2 }
## GET /health – Check service status
