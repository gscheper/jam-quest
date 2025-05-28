import urllib
import base64
from flask import Blueprint, request, redirect
from datetime import timedelta, datetime
import requests
from .utils import load_data, save_data

bp = Blueprint('spotify_auth', __name__, url_prefix='/spotify_auth')

@bp.route('/stub')
def stub():
    auth = load_data()
    return auth, 200

@bp.route('/callback', methods=['GET'])
def callback():
    '''
    Callback function for Spotify Web API authentication. Makes a request for
    the authentication token and stores the required information (access token, 
    refresh token, and expiration time) in a global dictionary. Redirects to 
    frontend admin page on success, redirect to frontend root page on failure.
    '''
    if request.method != 'GET':
        return 'Method Not Allowed', 405
    if 'error' in request.args:
        return redirect("http://localhost:5173")
    else:
        # Make request
        auth = load_data()
        auth_code = base64.b64encode((auth["client_ID"]+":"+auth["client_SC"]).encode("ascii")).decode("ascii")
        auth_request = requests.post("https://accounts.spotify.com/api/token", 
                                     data={
                                         "grant_type":"authorization_code",
                                         "code":request.args["code"], 
                                         "redirect_uri": "http://localhost:5000/spotify_auth/callback"},
                                     headers={
                                         "content-type":"application/x-www-form-urlencoded",
                                         "Authorization":"Basic " + auth_code})
        
        # Store authorization information
        auth["access_token"] = auth_request.json()["access_token"]
        auth["refresh_token"] = auth_request.json()["refresh_token"]
        auth["expiration_time"] = datetime.now() + timedelta(seconds=auth_request.json()["expires_in"])
        save_data(auth)
        
        return redirect("http://localhost:5173/admin")

@bp.route('/login', methods=['GET'])
def login():
    '''
    Immediately redirects user to spotify authentication website.
    '''
    if request.method != 'GET':
        return 'Method Not Allowed', 405
    auth = load_data()
    return redirect('https://accounts.spotify.com/authorize?' + urllib.parse.urlencode({
                    'response_type': 'code',
                    'client_id': auth['client_ID'],
                    'scope': 'streaming user-read-private',
                    'redirect_uri': 'http://localhost:5000/spotify_auth/callback'}))