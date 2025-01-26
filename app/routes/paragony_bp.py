from flask import Blueprint, jsonify
from app.models import Paragon

paragony_bp = Blueprint('paragony', __name__, url_prefix='/paragony')

@paragony_bp.route('/')
def index():
    paragony = Paragon.query.all()
    paragony_list = []
    for paragon in paragony:
        paragony_list.append({
            'id': paragon.id,
            'sklep': paragon.sklep,
            'data': paragon.data.isoformat(),
            'laczna_cena': paragon.laczna_cena,
            'rabat': paragon.rabat
        })
    return jsonify(paragony_list)