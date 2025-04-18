from flask import Blueprint, request

bp = Blueprint('quest', __name__, url_prefix='/quest')

@bp.route('/', methods=['GET','POST'])
def question():
    if request.method == 'GET':
        print("get found")
    elif request.method == 'POST':
        print("post found")
    else:
        return 'Method Not Allowed', 405
    return 'Success', 200