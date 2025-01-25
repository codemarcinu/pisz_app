from flask import Blueprint, request, jsonify
from .models import Paragony
from . import db
from datetime import datetime
from sqlalchemy.exc import SQLAlchemyError
 
main_bp = Blueprint('main', __name__)
 
@main_bp.route('/paragony', methods=['POST'])
def dodaj_paragon():
    try:
        data = request.get_json()
        nowy_paragon = Paragony(
            data=datetime.strptime(data['data'], '%Y-%m-%d'),
            sklep=data['sklep'],
            laczna_cena=float(data['cena']),
            rabat=float(data.get('rabat', 0))
        )
        db.session.add(nowy_paragon)
        db.session.commit()
        return jsonify({'message': 'Paragon dodany pomyślnie', 'id': nowy_paragon.id}), 201
    except (ValueError, KeyError) as e:
        db.session.rollback()
        return jsonify({'error': 'Nieprawidłowe dane wejściowe'}), 400
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': 'Błąd bazy danych'}), 500

@main_bp.route('/paragony', methods=['GET'])
def lista_paragonow():
    try:
        paragony = Paragony.query.order_by(Paragony.data.desc()).all()
        return jsonify([{
            'id': p.id,
            'data': p.data.isoformat(),
            'sklep': p.sklep,
            'laczna_cena': p.laczna_cena,
            'rabat': p.rabat
        } for p in paragony]), 200
    except SQLAlchemyError as e:
        return jsonify({'error': 'Błąd bazy danych'}), 500