import atexit
from flask import Flask
from flask_cors import CORS
from . import spotify_auth, playback, quest
from .utils import init_db, reset_db

def create_app():
    # Initalize app
    app = Flask(__name__)
    CORS(app, origins=["http://localhost:5173"])
    app.config['SECRET_KEY'] = 'dev' #os.urandom(24)

    # Initalize authentication document and ensure it resets on exit
    init_db()
    atexit.register(reset_db)
    
    # Register blueprints
    app.register_blueprint(spotify_auth.bp)
    app.register_blueprint(playback.bp)
    app.register_blueprint(quest.bp)
    
    return app