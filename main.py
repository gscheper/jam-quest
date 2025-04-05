import os
import requests
import json
import base64
from dotenv import load_dotenv
import urllib.parse
from flask import Flask, render_template, redirect, request, session

app = Flask(__name__)
app.secret_key = os.urandom(24)

load_dotenv('.env')
client_ID = os.getenv('CLIENT_ID')
client_SC = os.getenv('CLIENT_SC')

auth_url = 'https://accounts.spotify.com/authorize?' + urllib.parse.urlencode({
        'response_type': 'code',
        'client_id': client_ID,
        'redirect_uri': 'http://localhost:5000/callback'})

class admin:
    def __init__(self, auth_id):
        self.auth_id = auth_id

@app.route('/')
def index():
    return "index page"

@app.route('/login')
def login():
    return auth_url

@app.route('/playback/state')
def playback():
    request = requests.get("https://api.spotify.com/v1/me/player", headers={'Authorization':"Bearer " + session["access_token"]})
    return request.json()

@app.route('/callback')
def callback():
    if 'error' in request.args:
        return redirect("/")
    else:
        auth_request = requests.post("https://accounts.spotify.com/api/token", 
                                     data={
                                         "grant_type":"authorization_code",
                                         "code":request.args["code"], 
                                         "redirect_uri": "http://localhost:5000/callback"},
                                     headers={
                                         "content-type":"application/x-www-form-urlencoded",
                                         "Authorization":"Basic " + base64.b64encode((str(client_ID)+":"+str(client_SC)).encode("ascii")).decode("ascii")})
        session["access_token"] = auth_request.json()["access_token"]
        return str(session["access_token"])

if __name__ == '__main__':
    #init()
    app.run(host='0.0.0.0', debug=True)