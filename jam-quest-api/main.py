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

frontend_url = "http://localhost:5173"

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": frontend_url}})
app.secret_key = os.urandom(24)

load_dotenv('.env')
client_ID = os.getenv('CLIENT_ID')
client_SC = os.getenv('CLIENT_SC')
AccessAuthorization = {"access_token":"","refresh_token":"","expiration_time":datetime.now()}

auth_url = 'https://accounts.spotify.com/authorize?' + urllib.parse.urlencode({
        'response_type': 'code',
        'client_id': client_ID,
        'scope': 'streaming user-read-private',
        'redirect_uri': 'http://localhost:5000/callback'})

def refresh_token():
    print(AccessAuthorization)
    if (AccessAuthorization["expiration_time"] <= datetime.now()):
        refresh_request = requests.post("https://api.spotify.com/api/token",
                                     data={"grant_type":"refresh_token","refresh_token":AccessAuthorization["refresh_token"]},
                                     headers={"Content-Type":"application/x-www-form-urlencoded","Authorization":"Basic " + base64.b64encode((str(client_ID)+":"+str(client_SC)).encode("ascii")).decode("ascii")})
    return 'Success!', 200

@app.route('/login')
def login():
    return redirect(auth_url)

@app.route('/playback/search')
def search():
    refresh_token()
    make_request = requests.get("https://api.spotify.com/v1/search", 
                                 headers={"Authorization":"Bearer "+AccessAuthorization["access_token"]},
                                 params={"q":request.args.get('q'),"type":"track","limit":"5"})
    
    return make_request.json()['tracks']

@app.route('/playback/add')
def add():
    refresh_token()
    make_request = requests.post("https://api.spotify.com/v1/me/player/queue", 
                                 headers={"Authorization":"Bearer "+AccessAuthorization["access_token"]},
                                 params={"uri":request.args.get('uri')})
    print(make_request)
    return 'Success!', 200

@app.route('/callback')
def callback():
    if 'error' in request.args:
        return redirect("http://localhost:5173")
    else:
        auth_request = requests.post("https://accounts.spotify.com/api/token", 
                                     data={
                                         "grant_type":"authorization_code",
                                         "code":request.args["code"], 
                                         "redirect_uri": "http://localhost:5000/callback"},
                                     headers={
                                         "content-type":"application/x-www-form-urlencoded",
                                         "Authorization":"Basic " + base64.b64encode((str(client_ID)+":"+str(client_SC)).encode("ascii")).decode("ascii")})
        
        print(auth_request.json())
        AccessAuthorization["access_token"] = auth_request.json()["access_token"]
        AccessAuthorization["refresh_token"] = auth_request.json()["refresh_token"]
        AccessAuthorization["expiration_time"] = datetime.now() + timedelta(seconds=auth_request.json()["expires_in"])
        
        refresh_token()
        return redirect("http://localhost:5173/admin")

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5000)