import os
import requests
import json
from dotenv import load_dotenv
from pymongo.mongo_client import MongoClient
import pymongo
load_dotenv()

mongo_uri = "mongodb+srv://%s:%s@cluster0.x72dw2i.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0" % (
    os.getenv("MONGO_USERNAME"),
    os.getenv("MONGO_PASSWORD"),
)

currency_uri=os.getenv("CURRENCY_URL") + os.getenv("CURRENCY_API")

response = requests.get(currency_uri)
data=response.json()

db= MongoClient(mongo_uri)   
collection= db["currency"]["rates"]
result = collection.insert_one(data)
print(f"Data stored with ID:{result.inserted_id}")
