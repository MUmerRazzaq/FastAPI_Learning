from pymongo import MongoClient

from dotenv import load_dotenv
import os
load_dotenv()

def connect_to_mongo():
    try:# Load environment variables from .env file
        mongo_uri = os.getenv("MONGO_URI")

        # Connect to MongoDB
        client = MongoClient(mongo_uri)
        return client
    except Exception as e:
        print(f"Error connecting to MongoDB: {e}")
        return None

client = connect_to_mongo()
if client:
    print("Connected to MongoDB")
else:
    print("Failed to connect to MongoDB")

db = client["FastAPI"]