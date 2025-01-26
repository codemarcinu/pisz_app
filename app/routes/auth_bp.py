from flask import Blueprint

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

@auth_bp.route('/login')
def login():
    return "Auth Login Blueprint"

@auth_bp.route('/register')
def register():
    return "Auth Register Blueprint"