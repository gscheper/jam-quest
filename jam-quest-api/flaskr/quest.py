from flask import Blueprint, request, session, jsonify
from .utils import generate_key, load_data, save_data

bp = Blueprint('quest', __name__, url_prefix='/quest')

@bp.route('', methods=['GET','POST', 'OPTIONS'])
def question():
    if request.method == 'OPTIONS':
        response = jsonify({"message": "Works"})
        response.headers['Access-Control-Allow-Credentials'] = 'true'
        return response
    if 'id' not in session:
        session['id'] = generate_key()
    if request.method == 'GET':
        print(session['id'])
    elif request.method == 'POST':
        print(session['id'])
    else:
        return 'Method Not Allowed', 405
    response = jsonify({"message": "Works"})
    response.headers['Access-Control-Allow-Credentials'] = 'true'
    return response

@bp.route('/king', methods=['GET','POST', 'OPTIONS'])
def king():
    auth = load_data()
    if request.method == 'OPTIONS':
        response = jsonify({"message": "Works"})
        response.headers['Access-Control-Allow-Credentials'] = 'true'
        return response
    if request.method == 'GET':
        response = jsonify({"king": False})
        if 'id' in session:
            print(auth['king'])
            print(session['id'])
            response = jsonify({"king": auth['king']==session['id']})
        response.headers['Access-Control-Allow-Credentials'] = 'true'
        return response
    elif request.method == 'POST':
        auth["king"] = session['id']
        save_data(auth)
        response = jsonify({"message": "success"})
        response.headers['Access-Control-Allow-Credentials'] = 'true'
        return response
    return 'Method Not Allowed', 405