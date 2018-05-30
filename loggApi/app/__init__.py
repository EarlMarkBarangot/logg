from flask import Flask
from flask_sqlalchemy import SQLAlchemy  
from flask.ext.cors import CORS

app = Flask(__name__)
db = SQLAlchemy(app)
CORS(app, headers=['Content-Type'])

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/t123'
app.config['CORS_HEADERS'] = "Content-Type, Authorization"
app.config['SECRET_KEY'] = "flasky"

import models
db.create_all()


from app import api

app.debug = True
app.threaded = True