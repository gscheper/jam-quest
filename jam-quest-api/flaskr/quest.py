from flask import Blueprint, request, session
from .utils import generate_key, load_data

bp = Blueprint('quest', __name__, url_prefix='/quest')

@bp.route('/', methods=['GET','POST'])
def question():
    if 'id' not in session:
        session['id'] = generate_key()
    if request.method == 'GET':
        print(session['id'])
    elif request.method == 'POST':
        print(session['id'])
    else:
        return 'Method Not Allowed', 405
    return 'Success', 200

