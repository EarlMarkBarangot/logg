import os
from flask import Flask
from flask_compress import Compress 

app = Flask(__name__)
Compress(app)

app.config['SECRET_KEY'] = 'flasky'

app.debug = True

from app import views