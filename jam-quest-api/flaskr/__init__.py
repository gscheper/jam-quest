import os
from flask import Flask
from flask_cors import CORS
from datetime import datetime
from dotenv import load_dotenv
from . import spotify_auth, playback, quest

def create_app():
    # Frontend url
    frontend_url = "http://localhost:5173"

    app = Flask(__name__)
    CORS(app, resources={r"/*": {"origins": frontend_url}})
    app.SECRET_KEY='dev' #os.urandom(24)

    with open("tempdb/CLIENT_ID.txt", "w") as file:
        file.write(os.getenv('CLIENT_ID'))
    with open("tempdb/CLIENT_SC.txt", "w") as file:
        file.write(os.getenv('CLIENT_SC'))
    with open("tempdb/AUTHORIZATION.txt", "w") as file:
        file.write("\n")
        file.write("\n")
        file.write(str(datetime.now()))
    
    app.register_blueprint(spotify_auth.bp)
    app.register_blueprint(playback.bp)
    app.register_blueprint(quest.bp)
    
    return app