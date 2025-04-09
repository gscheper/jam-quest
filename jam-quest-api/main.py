import os
import requests
import json
import base64
from datetime import date, timedelta, datetime
from dotenv import load_dotenv
import urllib.parse
from flask import Flask, render_template, redirect, request, session
from flask_cors import CORS
import time

# Frontend url
frontend_url = "http://localhost:5173"

# App configuration parameters
app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": frontend_url}})
app.secret_key = os.urandom(24)

# Global authorization variables, allows any user to access the spotify account
AccessAuthorization = {"access_token":"","refresh_token":"","expiration_time":datetime.now()}

# .env variable loading
load_dotenv('.env')
client_ID = os.getenv('CLIENT_ID')
client_SC = os.getenv('CLIENT_SC')

def refresh_token():
    '''
    Helper function for refreshing the spotify authorization token, which 
    expires every hour.
    '''
    if (AccessAuthorization["expiration_time"] <= datetime.now()):
        auth_code = base64.b64encode((str(client_ID)+":"+str(client_SC)).encode("ascii")).decode("ascii")
        refresh_request = requests.post("https://api.spotify.com/api/token",
                                        data={
                                            "grant_type":"refresh_token",
                                            "refresh_token":AccessAuthorization["refresh_token"]},
                                        headers={
                                            "Content-Type":"application/x-www-form-urlencoded",
                                            "Authorization":"Basic " + auth_code})
        if 'error' in refresh_request.json():
            return refresh_request.json()["error"], 500
    return 'Success', 200

@app.route('/login', methods=['GET'])
def login():
    '''
    Immediately redirects user to spotify authentication website.
    '''
    if request.method != 'GET':
        return 'Method Not Allowed', 405
    return redirect('https://accounts.spotify.com/authorize?' + urllib.parse.urlencode({
                    'response_type': 'code',
                    'client_id': client_ID,
                    'scope': 'streaming user-read-private',
                    'redirect_uri': 'http://localhost:5000/callback'}))

@app.route('/playback/search', methods=['GET'])
def search():
    '''
    Searches for the first 5 songs that appear when the query [q] is made.
    Parameters:
        - name: q
          in: params
          type: string
          description: query to be made to spotify api
    Responses:
        200:
          Description: Query was made successfully, returns json with list of 
          tracks among other information
    '''
    if request.method != 'GET':
        return 'Method Not Allowed', 405
    refresh_token()
    search_request = requests.get("https://api.spotify.com/v1/search", 
                                  headers={
                                      "Authorization":"Bearer "+AccessAuthorization["access_token"]},
                                  params={
                                      "q":request.args.get('q'),
                                      "type":"track",
                                      "limit":"5"})
    return search_request.json()['tracks'], 200

@app.route('/playback/add', methods=['POST'])
def add():
    '''
    Forms request to spotify API to add a song to the queue. 
    Parameters:
        - name: uri
          in: params
          type: string
          description: uri of the song to be queued
    Responses:
        200:
          description: song was added successfully
    '''
    if request.method != 'POST':
        return 'Method Not Allowed', 405
    refresh_token()
    add_request = requests.post("https://api.spotify.com/v1/me/player/queue", 
                                headers={
                                    "Authorization":"Bearer "+AccessAuthorization["access_token"]},
                                params={
                                    "uri":request.args.get('uri')})
    return 'Success!', 200

@app.route('/callback', methods=['GET'])
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
        auth_code = base64.b64encode((str(client_ID)+":"+str(client_SC)).encode("ascii")).decode("ascii")
        auth_request = requests.post("https://accounts.spotify.com/api/token", 
                                     data={
                                         "grant_type":"authorization_code",
                                         "code":request.args["code"], 
                                         "redirect_uri": "http://localhost:5000/callback"},
                                     headers={
                                         "content-type":"application/x-www-form-urlencoded",
                                         "Authorization":"Basic " + base64.b64encode((str(client_ID)+":"+str(client_SC)).encode("ascii")).decode("ascii")})
        
        # Store authorization information
        AccessAuthorization["access_token"] = auth_request.json()["access_token"]
        AccessAuthorization["refresh_token"] = auth_request.json()["refresh_token"]
        AccessAuthorization["expiration_time"] = datetime.now() + timedelta(seconds=auth_request.json()["expires_in"])
        
        return redirect("http://localhost:5173/admin")

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5000)