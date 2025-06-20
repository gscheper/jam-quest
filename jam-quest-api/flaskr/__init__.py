import atexit
from flask import Flask
from flask_cors import CORS
from . import spotify_auth, playback, quest, debug
from .utils import init_db, reset_db, save_question
from os import environ

def create_app():
    # Initalize app
    app = Flask(__name__)
    
    CORS(app, origins=['http://' + environ.get('FRONTEND_ENDPOINT')])
    app.config['SECRET_KEY'] = 'dev' #os.urandom(24)

    # Initalize authentication document and ensure it resets on exit
    init_db()
    atexit.register(reset_db)
    
    # Debug question !!! DELETE LATER !!!
    save_question("The answer is 42 or 3", ["42", "3"])

    # Register blueprints
    app.register_blueprint(spotify_auth.bp)
    app.register_blueprint(playback.bp)
    app.register_blueprint(quest.bp)
    app.register_blueprint(debug.bp)
    
    return app