cat << 'EOF' > README.md
# ML Service Project

![Architecture Diagram](arc.png)

## Project Overview
This project is a Machine Learning (ML) service that provides a simple ML pipeline to ingest data, train a model, and serve predictions through a REST API. Built with FastAPI and containerized using Docker, the service is designed for deployment on AWS, featuring automated CI/CD pipelines, monitoring, and scheduled re-training to keep the model updated in production.

The app uses the Iris dataset (located in `data/iris.csv`) as a sample dataset. It stores data in MongoDB, trains a scikit-learn model, and exposes endpoints for data ingestion, model training, prediction, and health checks. This project showcases best practices for production-ready ML systems, including containerization, cloud deployment, and monitoring.

## Objective
The goal of this project is to create a production-ready ML service that:
- Ingests data into MongoDB via a POST /data endpoint.
- Trains a scikit-learn model using a POST /train endpoint.
- Serves predictions through a POST /predict endpoint.
- Provides a health check with a GET /health endpoint.
- Deploys to AWS using Docker and ECS, with CI/CD automation via GitLab.
- Includes monitoring (via AWS CloudWatch) and scheduled re-training (via AWS Lambda and EventBridge).

This project demonstrates skills in Docker, MongoDB, CI/CD, cloud deployment, and ML operations.

## Technology Used
- **FastAPI:** For building the REST API.
- **Scikit-learn:** For training and serving the ML model.
- **MongoDB:** For data storage.
- **Docker:** For containerization.
- **AWS ECS:** For cloud deployment of the app and MongoDB containers.
- **AWS ECR:** For storing Docker images.
- **AWS CloudWatch:** For monitoring logs and the GET /health endpoint.
- **AWS Lambda & EventBridge:** For scheduling weekly re-training (POST /train).
- **GitLab CI/CD:** For automating linting, testing, building, and deployment.
- **Pytest:** For running tests.
- **Python 3.12:** The programming language used throughout the project.

## Setup
1. **Clone the Repository:**
   ```bash
   git clone https://github.com/MrJohn91/ml-service-project.git
   cd ml-service-project
