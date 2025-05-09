from datetime import datetime
from pymongo import MongoClient
import base64
import os
import requests
from dotenv import load_dotenv

def refresh_token():
    '''
    Helper function for refreshing the spotify authorization token, which 
    expires every hour.
    Returns: 
        Success on successful refresh, error message on unsuccessful refresh
    '''
    auth = load_data()
    if (auth["expiration_time"] <= datetime.now()):
        auth_code = base64.b64encode((auth['client_ID']+":"+auth['client_SC']).encode("ascii")).decode("ascii")
        refresh_request = requests.post("https://api.spotify.com/api/token",
                                        data={
                                            "grant_type":"refresh_token",
                                            "refresh_token":auth["refresh_token"]},
                                        headers={
                                            "Content-Type":"application/x-www-form-urlencoded",
                                            "Authorization":"Basic " + auth_code})
        if 'error' in refresh_request.json():
            return refresh_request.json()["error"]
    return "Success"

def save_data(change):
    '''
    Saves changes to the authentication document
    '''
    uri = "mongodb://localhost:27017/"
    client = MongoClient(uri)
    db = client["test_database"]
    auth = db["authorization"]

    auth.update_one({"_id":"0"}, {"$set":change}, upsert=False)

    client.close()

def load_data():
    '''
    Loads the authentication document into a python dictionary
    Returns:
        The python dictionary
    '''
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
    '''
    Generates a session id for a user
    Returns:
        The session id
    '''
    auth = load_data()
    auth['id_iter'] += 1
    save_data(auth)
    return auth['id_iter']

def delete_question(question):
    '''
    Deletes any document in the question database containing a given question
    '''
    # Connect to database
    uri = "mongodb://localhost:27017/"
    client = MongoClient(uri)
    db = client["test_database"]
    auth = db["questions"]

    auth.delete_many({"Question": question})

    # Disconnect from database
    client.close()

def get_all_questions():
    '''
    Gets every distinct question in the question database
    Returns:
        A python array containing each question in the question database
    '''
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
    '''
    Saves a question and a list of answers to the question database. 
    '''
    # Connect to database
    uri = "mongodb://localhost:27017/"
    client = MongoClient(uri)
    db = client["test_database"]
    auth = db["questions"]

    # Save question
    for i in answers:
        if auth.find_one({"Question":question, "Answer": i})==None:
            auth.insert_one({
                "Question": question,
                "Answer": i
            })

    # Disconnect from database
    client.close()

def check_if_correct(question, answer):
    '''
    Checks to see if a given question has a corresponding answer in the question database
    Returns:
        True if the question has the corresponding answer, False otherwise.
    '''
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

def init_db():
    '''
    Initialize an instance of the authentication document in the database
    '''
    uri = "mongodb://localhost:27017/"
    client = MongoClient(uri)
    db = client["test_database"]
    auth = db["authorization"]

    load_dotenv(dotenv_path=os.path.join("instance", ".env"))
    info = {}
    info["_id"] = "0"
    info["access_token"] = ""
    info["refresh_token"] = ""
    info["expiration_time"] = datetime.now()
    info["client_SC"] = os.getenv('CLIENT_SC')
    info["client_ID"] = os.getenv('CLIENT_ID')
    info["id_iter"] = "0"
    info["king"] = "-1"
    
    auth.insert_one(info)

    client.close()

def reset_db():
    '''
    Delete the authenticaiton document, for use at exit
    '''
    uri = "mongodb://localhost:27017/"
    client = MongoClient(uri)
    db = client["test_database"]

    db.drop_collection("authorization")

    client.close()