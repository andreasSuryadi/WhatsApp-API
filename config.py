import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:password@localhost:3306/whatsapp_api'
    SQLALCHEMY_TRACK_MODIFICATIONS = False