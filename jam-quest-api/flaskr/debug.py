from flask import Blueprint

bp = Blueprint('debug', __name__, url_prefix='/debug')

@bp.route('/ping', methods=['GET'])
def search():
    return 'pong'