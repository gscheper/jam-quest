import atexit
import os
from flask import Flask, session
from flask_cors import CORS
from datetime import datetime
from dotenv import load_dotenv
from . import spotify_auth, playback, quest
from pymongo import MongoClient

def init_db():
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
    uri = "mongodb://localhost:27017/"
    client = MongoClient(uri)
    db = client["test_database"]

    db.drop_collection("authorization")

    client.close()

def create_app():
    app = Flask(__name__)
    CORS(app, origins=["http://localhost:5173"])
    app.config['SECRET_KEY'] = 'dev' #os.urandom(24)

    init_db()
    atexit.register(reset_db)

    app.register_blueprint(spotify_auth.bp)
    app.register_blueprint(playback.bp)
    app.register_blueprint(quest.bp)
    
    return app