from flask import jsonify, request
import jwt
from app import app
import logging

def protected(token):
    if not token:
        return jsonify({'error': 'Token is missing'}), 401
    
    logging.debug(token)

    try:
        payload = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
        return payload, 200
    except jwt.ExpiredSignatureError:
        return jsonify({'error': 'Token has expired'}), 401
    except jwt.InvalidTokenError:
        return jsonify({'error': 'Invalid token'}), 401