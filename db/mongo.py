import os
import time
from pymongo import MongoClient

mongo_url = os.getenv("MONGO_URL", "mongodb://mongo:27017")

for i in range(10):
    try:
        client = MongoClient(mongo_url, serverSelectionTimeoutMS=2000)
        client.server_info()
        break
    except:
        print("Mongo not ready, retrying...")
        time.sleep(2)

db = client["messages_db"]
collection = db["messages"]