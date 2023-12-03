from flask import jsonify, request
from app import app, db
from app.entity.entity import User
from app.service.service import protected

@app.route('/api/users', methods=['GET'])
def get_users():
    token = request.headers.get('Authorization')

    auth, status = protected(token)
    if status != 200:
        return auth

    users = User.query.all()
    user_list = [
        {
            'id': user.id, 
            'name': user.name, 
            'phone_number': user.phone_number
        } for user in users
    ]
    return jsonify({'users': user_list})

@app.route('/api/users', methods=['POST'])
def add_user():
    data = request.get_json()
    name = data.get('name')
    phone_number = data.get('phone_number')

    new_user = User(name=name, phone_number=phone_number)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'User added successfully'})
    