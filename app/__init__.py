from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.debug = True
app.config.from_object('config.Config')
app.config['SECRET_KEY'] = 'Q8Q41a1aHnSVVvik2uXjL0GIvvuqJ//TNI4VgoHlU9g='

db = SQLAlchemy(app)

from app.controller import auth_controller, chatroom_controller, user_controller