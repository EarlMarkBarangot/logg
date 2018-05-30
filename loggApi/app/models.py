from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from itsdangerous import JSONWebSignatureSerializer as Serializer
from sqlalchemy.orm import relationship
from sqlalchemy import Integer, String, Column
from flask_login import AnonymousUserMixin

class Users(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key= True)
    username = db.Column(db.String(60), unique=True)
    email = db.Column(db.String(60))
    password = db.Column(db.String(1000))

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = generate_password_hash(password)

    def __repr__(self):
        return '<username {}>'.format(self.username)

    @staticmethod
    def verify_token(token):
        s =Serializer(app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except:
            return None
        id = data.get('user')
        if id:
            return Users.query.get(id)
        return None

