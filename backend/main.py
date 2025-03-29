import os
import requests
from dotenv import load_dotenv
import urllib.parse
from flask import Flask, render_template, redirect, request

app = Flask(__name__)
app.secret_key = os.urandom(24)

load_dotenv('.env')
client_ID = os.getenv('CLIENT_ID')
client_SC = os.getenv('CLIENT_SC')
code = ''

auth_url = 'https://accounts.spotify.com/authorize?' + urllib.parse.urlencode({
        'response_type': 'code',
        'client_id': client_ID,
        'scope': 'user-read-private user-read-email',
        'redirect_uri': 'http://localhost:5000/callback'})

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    print(auth_url)
    return redirect(auth_url)

@app.route('/callback')
def callback():
    code = request.args['code']
    return redirect('/admin')

@app.route('/admin')
def admin():
    return render_template('admin.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)