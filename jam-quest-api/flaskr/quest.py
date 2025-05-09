from flask import Blueprint, request, session, jsonify
from .utils import generate_key, load_data, save_data, get_all_questions, check_if_correct
import random

bp = Blueprint('quest', __name__, url_prefix='/quest')

@bp.route('', methods=['GET','POST', 'OPTIONS'])
def question():
    '''
    Route to interface with questions.
    GET: 
        Returns random question from the question database under the key [Quest]
    POST: 
        Takes two parameters, [Quest] and [Answer], checks to see if there is a 
        document in the question database with that question and that answer. 
        Returns True if a document has been found and false otherwise.
    Parameters:
        - name: Quest
          in: params
          type: string
          description: Question to be answered, only used in POST
        - name: Answer
          in: params
          type: string
          description: Answer to check against [Quest], only used in POST
    Responses:
        200:
          description: Request made successfully
        405:
          Description: Request method not allowed
        400:
          Description: Request args missing (only in POST)
    '''
    if request.method == 'OPTIONS':
        response = jsonify({})
        response.headers['Access-Control-Allow-Credentials'] = 'true'
        return response
    if 'id' not in session:
        session['id'] = generate_key()
    if request.method == 'GET':
        questions = get_all_questions()
        response = jsonify({
            "Quest": questions[random.randint(0, len(questions)-1)]})
        response.headers['Access-Control-Allow-Credentials'] = 'true'
        return response
    elif request.method == 'POST':
        if 'Quest' not in request.args:
            return 'Question [Quest] not in body', 400
        if 'Answer' not in request.args:
            return 'Answer [Answer] not in body', 400
        response = jsonify({"Check": check_if_correct(request.args.get('Quest'), request.args.get('Answer'))})
        if response["Check"]:
            auth = load_data()
            auth["king"] = session['id']
            save_data(auth)
        response.headers['Access-Control-Allow-Credentials'] = 'true'
        return response
    else:
        return 'Method Not Allowed', 405

@bp.route('/king', methods=['GET', 'OPTIONS'])
def king():
    '''
    Route to check if the current user is the king of the hill.
    Responses:
        200:
          description: Request made successfully
        405:
          Description: Request method not allowed
    '''
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
    
    return 'Method Not Allowed', 405