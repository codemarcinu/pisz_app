from flask import Blueprint, jsonify, request
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from ..models import User
from ..extensions import db, bcrypt
from datetime import timedelta
import re

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/api/auth/register', methods=['POST'])
def register():
    data = request.get_json()
    
    # Walidacja danych
    if not data.get('username') or not data.get('password'):
        return jsonify({"error": "Username and password are required"}), 400
    
    if len(data['password']) < 8:
        return jsonify({"error": "Password must be at least 8 characters"}), 400
    
    if User.query.filter_by(username=data['username']).first():
        return jsonify({"error": "Username already exists"}), 409
    
    # Tworzenie nowego użytkownika
    hashed_password = bcrypt.generate_password_hash(data['password']).decode('utf-8')
    new_user = User(
        username=data['username'],
        password_hash=hashed_password,
        email=data.get('email')
    )
    
    db.session.add(new_user)
    db.session.commit()
    
    return jsonify({"message": "User registered successfully"}), 201

@auth_bp.route('/api/auth/login', methods=['POST'])
def login():
    data = request.get_json()
    
    user = User.query.filter_by(username=data.get('username')).first()
    
    if not user or not bcrypt.check_password_hash(user.password_hash, data.get('password')):
        return jsonify({"error": "Invalid username or password"}), 401
    
    access_token = create_access_token(
        identity=user.id,
        expires_delta=timedelta(hours=24)
    )
    
    return jsonify({
        "access_token": access_token,
        "user_id": user.id,
        "username": user.username
    }), 200

@auth_bp.route('/api/auth/protected', methods=['GET'])
@jwt_required()
def protected():
    current_user_id = get_jwt_identity()
    user = User.query.get(current_user_id)
    
    if not user:
        return jsonify({"error": "User not found"}), 404
    
    return jsonify({
        "message": f"Hello {user.username}!",
        "user_id": user.id
    }), 200