from pymongo import MongoClient
import os
import pandas as pd

mongo_host = os.getenv("MONGO_HOST", "mongo")
mongo_uri = f"mongodb://{mongo_host}:27017"

client = MongoClient(mongo_uri)
db = client.ml_db

def insert_sample(sample):
    # Add a single data sample to the database
    db.samples.insert_one(sample)

def get_samples(species=None):
    # Retrieve samples, optionally filtered by species
    query = {"species": species} if species else {}
    return list(db.samples.find(query, {"_id": 0}))

def initialize_db_with_iris():
    # Load Iris dataset if database is empty
    try:
        if db.samples.count_documents({}) == 0:
            iris_df = pd.read_csv('/app/data/iris.csv')
            db.samples.insert_many(iris_df.to_dict("records"))
            print("Initialized database with Iris dataset")
            return True
        print("Database already contains samples")
        return False
    except Exception as e:
        print(f"Error initializing database: {e}")
        return False