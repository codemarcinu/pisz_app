from flask import Blueprint

produkty_bp = Blueprint('produkty', __name__, url_prefix='/produkty')

@produkty_bp.route('/')
def index():
    return "Produkty Blueprint"