from flask import Blueprint, jsonify, request
from ..models import Paragony, Produkty
from .. import db

paragony_bp = Blueprint('paragony', __name__)
produkty_bp = Blueprint('produkty', __name__)

@paragony_bp.route('/paragony', methods=['POST'])
def dodaj_paragon():
    try:
        data = request.get_json()
        new_paragon = Paragony(
            data=data['data'],
            sklep=data['sklep'],
            cena=data['cena']
        )
        db.session.add(new_paragon)
        db.session.commit()
        return jsonify({"message": "Paragon dodany"}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

@paragony_bp.route('/paragony', methods=['GET'])
def lista_paragonow():
    try:
        paragony = Paragony.query.order_by(Paragony.data.desc()).all()
        return jsonify([{
            "id": p.id,
            "data": p.data.isoformat(),
            "sklep": p.sklep,
            "cena": p.cena
        } for p in paragony])
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@produkty_bp.route('/produkty', methods=['GET'])
def lista_produktow():
    try:
        produkty = Produkty.query.all()
        return jsonify([{
            "id": p.id,
            "nazwa": p.nazwa
        } for p in produkty])
    except Exception as e:
        return jsonify({"error": str(e)}), 500