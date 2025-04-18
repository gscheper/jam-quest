import os
from flask import Flask, session
from flask_cors import CORS
from datetime import datetime
from dotenv import load_dotenv
from . import spotify_auth, playback, quest

def create_app():
    # Frontend url
    frontend_url = "http://localhost:5173"

    app = Flask(__name__)
    CORS(app, resources={r"/*": {"origins": frontend_url}})
    app.config['SECRET_KEY']='dev' #os.urandom(24)

    with open("tempdb/AUTHORIZATION.txt", "w") as file:
        file.write("\n")
        file.write("\n")
        file.write(str(datetime.now()) + "\n")
        file.write(os.getenv('CLIENT_SC') + "\n")
        file.write(os.getenv('CLIENT_ID') + "\n")
        file.write("0")
    
    app.register_blueprint(spotify_auth.bp)
    app.register_blueprint(playback.bp)
    app.register_blueprint(quest.bp)
    
    return app