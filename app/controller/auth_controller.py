from flask import request, jsonify
import jwt
from datetime import datetime, timedelta
from app.entity.entity import User
from app import app

@app.route('/api/login', methods=['POST'])
def login():
    phone_number = request.json.get('phone_number')

    user = User.query.filter_by(phone_number=phone_number).first()

    # Check if phone number is provided
    if not phone_number:
        return jsonify({'error': 'Phone number is required'}), 400
    if not user:
        return jsonify({'error': 'User not found'}), 404

    # Create a token with phone number as payload
    payload = {'phone_number': phone_number, 'exp': datetime.utcnow() + timedelta(days=1)}
    token = jwt.encode(payload, app.config['SECRET_KEY'], algorithm='HS256')

    return jsonify({'token': token})