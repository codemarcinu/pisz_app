from flask import Blueprint

paragony_bp = Blueprint('paragony', __name__, url_prefix='/paragony')

@paragony_bp.route('/')
def index():
    return "Paragony Blueprint"