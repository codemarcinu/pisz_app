from flask import Blueprint
from . import db

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def home():
    return "API Zakupy działa!"