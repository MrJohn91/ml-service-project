# ML Service Project

> ```markdown
> ![Architecture Diagram](./arc.png)
> ```

---

##  Project Overview

This project is a **Machine Learning (ML) service** providing a simple ML pipeline that:

- Ingests data
- Trains a model
- Serves predictions via REST API

It is built with **FastAPI**, containerized using **Docker**, and deployed to **AWS ECS** with CI/CD automation. The service also includes **monitoring via AWS CloudWatch** and **scheduled re-training via AWS Lambda & EventBridge**.

A sample dataset (Iris) is used (`data/iris.csv`), with data stored in **MongoDB** and models trained using **scikit-learn**.

---

## 🎯 Objective

The project demonstrates a production-ready ML system with the following key features:

- `POST /data`: Ingest data into MongoDB  
- `POST /train`: Train a scikit-learn model  
- `POST /predict`: Predict from input features  
- `GET /health`: Health check endpoint  
- **Dockerized** for easy local and cloud deployment  
- **CI/CD** via **GitLab**  
- **Monitoring** via **AWS CloudWatch**  
- **Scheduled re-training** using **AWS Lambda + EventBridge**

---

## 🛠️ Tech Stack

| Technology     | Purpose                                |
|----------------|----------------------------------------|
| **FastAPI**    | REST API Framework                     |
| **Scikit-learn** | ML Model Training and Prediction    |
| **MongoDB**    | Data Storage                           |
| **Docker**     | Containerization                       |
| **AWS ECS**    | App + MongoDB Deployment               |
| **AWS ECR**    | Docker Image Storage                   |
| **AWS CloudWatch** | Monitoring + Logs                  |
| **AWS Lambda + EventBridge** | Scheduled Re-training   |
| **GitLab CI/CD** | Automation Pipeline                  |
| **Pytest**     | Unit Testing                           |
| **Python 3.12**| Programming Language                   |

---

## 🚀 Setup

### 1. Clone the Repository
```bash
git clone https://github.com/MrJohn91/ml-service-project.git
cd ml-service-project
```

### 2. Run with Docker
Ensure Docker is installed and running.

Start the app and MongoDB with:
```bash
docker-compose up --build
```

### 3. Access the Service
- API base: `http://localhost:8000`
- Interactive docs: `http://localhost:8000/docs`

---

## 💻 Developer Setup (Devcontainer)

This project includes a preconfigured **devcontainer** for consistent local development using **VS Code**.

> To use:
1. Open the project in **VS Code**.
2. When prompted, click **"Reopen in Container"**.
3. VS Code will auto-setup Python, dependencies, and MongoDB.

---

## 📡 API Endpoints

### Ingest Data
```http
POST /data
```
**Example Payload:**
```json
{
  "sepal_length": 5.1,
  "sepal_width": 3.5,
  "petal_length": 1.4,
  "petal_width": 0.2,
  "species": "setosa"
}
```

### Retrieve Data
```http
GET /data?species=setosa
```

### Train Model
```http
POST /train
```

### Predict
```http
POST /predict
```
**Example Payload:**
```json
{
  "sepal_length": 5.1,
  "sepal_width": 3.5,
  "petal_length": 1.4,
  "petal_width": 0.2
}
```

### Health Check
```http
GET /health
```

---

## Run Tests

Use Docker to execute unit tests:
```bash
docker-compose exec app pytest -v tests/
```

---

## 🌐 Deployment

### CI/CD Pipeline (GitLab)
- Lint → Test → Build → Push to **AWS ECR** → Deploy to **AWS ECS**
- **Monitoring** via **CloudWatch** (logs + `/health`)
- **Weekly re-training** triggered by **Lambda + EventBridge**

### Manual Deployment (optional)
1. Build the image:
   ```bash
   docker build -t ml-service .
   ```
2. Push to ECR and deploy to ECS using AWS CLI or Console.
