from flask import jsonify, request
from app import app, db
from app.entity.entity import Chatroom
from app.service.service import protected

@app.route('/api/chatrooms', methods=['GET'])
def get_chatrooms():
    token = request.headers.get('Authorization')

    auth, status = protected(token)
    if status != 200:
        return auth
    
    chatrooms = Chatroom.query.all()
    chatroom_list = [
        {
            'id': chatroom.id, 
            'name': chatroom.name, 
            'description': chatroom.description
        } for chatroom in chatrooms
    ]
    return jsonify({'chatrooms': chatroom_list})

@app.route('/api/chatrooms', methods=['POST'])
def add_chatroom():
    token = request.headers.get('Authorization')

    auth, status = protected(token)
    if status != 200:
        return auth

    data = request.get_json()
    name = data.get('name')
    description = data.get('description')

    new_chatroom = Chatroom(name=name, description=description)
    db.session.add(new_chatroom)
    db.session.commit()

    return jsonify({'message': 'Chatroom added successfully'})

@app.route('/api/chatrooms/enter', methods=['POST'])
def enter_chatroom():
    token = request.headers.get('Authorization')

    protected(token)
