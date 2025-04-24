ML Service Project

Project Overview
This project is a Machine Learning (ML) service that provides a simple ML pipeline to ingest data, train a model, and serve predictions through a REST API. Built with FastAPI and containerized using Docker, the service is designed for deployment on AWS, featuring automated CI/CD pipelines, monitoring, and scheduled re-training to keep the model updated in production.
The app uses the Iris dataset (located in data/iris.csv) as a sample dataset. It stores data in MongoDB, trains a scikit-learn model, and exposes endpoints for data ingestion, model training, prediction, and health checks. This project showcases best practices for production-ready ML systems, including containerization, cloud deployment, and monitoring.
Objective
The goal of this project is to create a production-ready ML service that:

Ingests data into MongoDB via a POST /data endpoint.
Trains a scikit-learn model using a POST /train endpoint.
Serves predictions through a POST /predict endpoint.
Provides a health check with a GET /health endpoint.
Deploys to AWS using Docker and ECS, with CI/CD automation via GitLab.
Includes monitoring (via AWS CloudWatch) and scheduled re-training (via AWS Lambda and EventBridge).

This project demonstrates skills in Docker, MongoDB, CI/CD, cloud deployment, and ML operations.
Technology Used

FastAPI: For building the REST API.
Scikit-learn: For training and serving the ML model.
MongoDB: For data storage.
Docker: For containerization.
AWS ECS: For cloud deployment of the app and MongoDB containers.
AWS ECR: For storing Docker images.
AWS CloudWatch: For monitoring logs and the GET /health endpoint.
AWS Lambda & EventBridge: For scheduling weekly re-training (POST /train).
GitLab CI/CD: For automating linting, testing, building, and deployment.
Pytest: For running tests.
Python 3.12: The programming language used throughout the project.

Setup

Clone the Repository:
git clone https://github.com/MrJohn91/ml-service-project.git
cd ml-service-project


Run with Docker:

Ensure Docker is installed and running.
Start the app and MongoDB using Docker Compose:docker-compose up --build




Service Access:

The service runs on http://localhost:8000.
Access the API documentation at http://localhost:8000/docs.


For Developers (Using Devcontainer):

A devcontainer setup is included (.devcontainer/devcontainer.json) for an easier development experience.
If using VS Code, open the project and select "Reopen in Container" to set up the environment automatically with Python, dependencies, and MongoDB. This ensures consistency across development setups.



Endpoints

POST /data: Adds an Iris sample.
Example: {"sepal_length": 5.1, "sepal_width": 3.5, "petal_length": 1.4, "petal_width": 0.2, "species": "setosa"}


GET /data?species=...: Lists Iris samples by species.
POST /train: Trains the model using data from MongoDB.
POST /predict: Predicts species from input.
Example: {"sepal_length": 5.1, "sepal_width": 3.5, "petal_length": 1.4, "petal_width": 0.2}


GET /health: Checks the service status.

Run Tests

Use Docker to run the tests:docker-compose exec app pytest -v tests/



Deployment
The project is configured to deploy to AWS ECS using GitLab CI/CD:

GitLab CI/CD lints the code, runs tests, builds the Docker image, pushes it to AWS ECR, and deploys to AWS ECS.
AWS CloudWatch monitors the app (logs and GET /health).
AWS Lambda and EventBridge schedule weekly re-training by calling POST /train.

To deploy manually:

Build the Docker image:docker build -t ml-service .


Push the image to AWS ECR (after setting up AWS credentials).
Deploy to AWS ECS using the AWS CLI or console.

License
This project is licensed under the MIT License. See the LICENSE file for details (if applicable, or add one to your repository).
Contact
For questions or feedback, reach out to MrJohn91 on GitHub.
