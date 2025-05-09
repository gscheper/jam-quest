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

def delete_question(question):
    # Connect to database
    uri = "mongodb://localhost:27017/"
    client = MongoClient(uri)
    db = client["test_database"]
    auth = db["questions"]

    auth.delete_many({"Question": question})

    # Disconnect from database
    client.close()

def get_all_questions():
    # Connect to database
    uri = "mongodb://localhost:27017/"
    client = MongoClient(uri)
    db = client["test_database"]
    auth = db["questions"]
    
    result = []

    for i in auth.find(""):
        if (i["Question"] not in result):
            result.append(i["Question"])
    
    # Disconnect from database
    client.close()

    return result

def save_question(question, answers):
    # Connect to database
    uri = "mongodb://localhost:27017/"
    client = MongoClient(uri)
    db = client["test_database"]
    auth = db["questions"]

    # Save question
    for i in answers:
        if auth.find_one({"Answer": i})==None:
            auth.insert_one({
                "Question": question,
                "Answer": i
            })

    # Disconnect from database
    client.close()

def check_if_correct(question, answer):
    # Connect to database
    uri = "mongodb://localhost:27017/"
    client = MongoClient(uri)
    db = client["test_database"]
    auth = db["questions"]

    answers = auth.find({"Question": question})

    for i in answers:
        if (i["Answer"] == answer):
            return True

    # Disconnect from database
    client.close()

    return False
