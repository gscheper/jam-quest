from flask import Blueprint, request, session, jsonify
from .utils import generate_key, load_data, save_data, get_all_questions, check_if_correct
import random

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
        questions = get_all_questions()
        response = jsonify({
            "message": "Works", 
            "Quest": questions[random.randint(0, len(questions)-1)]
            })
        return response
    
    elif request.method == 'POST':
        response = jsonify({
            "message": "Works", 
            "Check": check_if_correct(request.headers.get('Quest'), request.headers.get('Answer'))
            })
        return response
    
    else:
        return 'Method Not Allowed', 405

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