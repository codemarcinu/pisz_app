from flask import Blueprint, jsonify
from app.models import Paragon
from flask import current_app as app  # Dodano import current_app

paragony_bp = Blueprint('paragony', __name__, url_prefix='/paragony')

@paragony_bp.route('/')
def index():
    try:
        with app.app_context():
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
    except Exception as e:
        return jsonify({'error': str(e)}), 500