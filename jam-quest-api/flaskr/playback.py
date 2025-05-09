import base64
from datetime import datetime
import requests
from flask import Blueprint, request
from .utils import load_data, refresh_token

bp = Blueprint('playback', __name__, url_prefix='/playback')

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
        405:
          Description: Request method not allowed
        400:
          Description: Arguments supplied were not sufficient
    '''
    if request.method != 'GET':
        return 'Method Not Allowed', 405
    if 'q' not in request.args:
        return 'query [q] not in body', 400
    refresh_token()
    auth = load_data()
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
        405:
          Description: Request method not allowed
        400:
          Description: Arguments supplied were not sufficient
    '''
    if request.method != 'POST':
        return 'Method Not Allowed', 405
    if 'uri' not in request.args:
        return 'uri [uri] not in body', 400 
    refresh_token()
    auth = load_data()
    requ = requests.post("https://api.spotify.com/v1/me/player/queue", 
                                headers={
                                    "Authorization":"Bearer "+auth["access_token"]},
                                params={
                                    "uri":request.args.get('uri')})
    return 'Success', 200