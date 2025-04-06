import os
import requests
import json
import base64
from datetime import date, timedelta, datetime
from dotenv import load_dotenv
import urllib.parse
from flask import Flask, render_template, redirect, request, session
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "http://localhost:5173"}})
app.secret_key = os.urandom(24)

load_dotenv('.env')
client_ID = os.getenv('CLIENT_ID')
client_SC = os.getenv('CLIENT_SC')
AccessAuthorization = {"access_token":""}

auth_url = 'https://accounts.spotify.com/authorize?' + urllib.parse.urlencode({
        'response_type': 'code',
        'client_id': client_ID,
        'scope': 'streaming user-read-private',
        'redirect_uri': 'http://localhost:5000/callback'})

@app.route('/login')
def login():
    return redirect(auth_url)

@app.route('/playback/pump_up_the_jam')
def pump_up_the_jam():
    requests.post("https://api.spotify.com/v1/me/player/queue?uri=spotify%3Atrack%3A21qnJAMtzC6S5SESuqQLEK", 
                                 headers={"Authorization":"Bearer "+AccessAuthorization["access_token"]})
    return 'Success!', 200

@app.route('/playback/search')
def search():
    make_request = requests.get("https://api.spotify.com/v1/search", 
                                 headers={"Authorization":"Bearer "+AccessAuthorization["access_token"]},
                                 params={"q":request.args.get('q'),"type":"album"})
    return make_request.json()

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
        
        AccessAuthorization["access_token"] = auth_request.json()["access_token"]
        AccessAuthorization["expiration_time"] = datetime.now() + timedelta(seconds=auth_request.json()["expires_in"])

        return redirect("http://localhost:5173/admin.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)