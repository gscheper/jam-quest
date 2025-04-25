from datetime import datetime
from pymongo import MongoClient

def save_data(change):
    uri = "mongodb://localhost:27017/"
    client = MongoClient(uri)
    db = client["test_database"]
    auth = db["authorization"]

    auth.update_one({"_id":"0"}, {"$set":change}, upsert=False)

    client.close()

def load_data():
    uri = "mongodb://localhost:27017/"
    client = MongoClient(uri)
    db = client["test_database"]
    auth = db["authorization"]

    result = auth.find_one({"_id":"0"})
    result["id_iter"] = int(result["id_iter"])
    result["king"] = int(result["king"])

    client.close()
    return result

def generate_key():
    auth = load_data()
    auth['id_iter'] += 1
    save_data(auth)
    return auth['id_iter']