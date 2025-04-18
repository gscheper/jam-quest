import base64
from datetime import datetime
import requests
from flask import Blueprint, request
from . import db

bp = Blueprint('playback', __name__, url_prefix='/playback')

def refresh_token():
    '''
    Helper function for refreshing the spotify authorization token, which 
    expires every hour.
    '''
    auth = db.load_data()
    if (auth["expiration_time"] <= datetime.now()):
        auth_code = base64.b64encode((auth['client_ID']+":"+auth['client_SC']).encode("ascii")).decode("ascii")
        refresh_request = requests.post("https://api.spotify.com/api/token",
                                        data={
                                            "grant_type":"refresh_token",
                                            "refresh_token":auth["refresh_token"]},
                                        headers={
                                            "Content-Type":"application/x-www-form-urlencoded",
                                            "Authorization":"Basic " + auth_code})
        if 'error' in refresh_request.json():
            return refresh_request.json()["error"], 500
    return 'Success', 200

@bp.route('/search', methods=['GET'])
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
    auth = db.load_data()
    search_request = requests.get("https://api.spotify.com/v1/search", 
                                  headers={
                                      "Authorization":"Bearer "+auth["access_token"]},
                                  params={
                                      "q":request.args.get('q'),
                                      "type":"track",
                                      "limit":"5"})
    return search_request.json()['tracks'], 200

@bp.route('/add', methods=['POST'])
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
    auth = db.load_data()
    print(auth)
    requ = requests.post("https://api.spotify.com/v1/me/player/queue", 
                                headers={
                                    "Authorization":"Bearer "+auth["access_token"]},
                                params={
                                    "uri":request.args.get('uri')})
    
    return 'Success!', 200