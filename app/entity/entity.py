from app import db

user_chatroom = db.Table('user_chatroom',
                      db.Column('user_id', db.BigInteger, db.ForeignKey('users.id')),
                      db.Column('chatroom_id', db.BigInteger, db.ForeignKey('chatrooms.id')),
                    #   db.Column('is_admin', db.Boolean),
                      db.PrimaryKeyConstraint('user_id', 'chatroom_id')
                      )

class Chatroom(db.Model):
    __tablename__ = "chatrooms"

    id = db.Column(db.BigInteger, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"<Chatroom {self.id}: {self.name}>"
    
class Message(db.Model):
    __tablename__ = "messages"

    id = db.Column(db.BigInteger, primary_key=True)
    message = db.Column(db.String(100), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    chatroom_id = db.Column(db.Integer, db.ForeignKey('chatroom.id'), nullable=False)
    attachment = db.Column(db.Text, nullable=True)

    def __repr__(self):
        return f"<Chatroom {self.id}: {self.task}>"
    
class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.BigInteger, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    phone_number = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"<User {self.id}: {self.name}>"