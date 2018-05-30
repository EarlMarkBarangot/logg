from app import app
from flask import Flask, render_template, request, redirect, url_for, session
from flask_login import login_user, login_required, logout_user, LoginManager, current_user
import random
from models import *


#login_manager = LoginManager()
#login_manager.init_app(app)
#login_manager.anonymous_user = Anonymous

#@login_manager.user_loader
#def load_user(id):
#	pass
    #return User.query.get(int(id))

@app.route('/', methods=['GET', 'POST'])
@app.route('/login', methods=['GET', 'POST'])
@app.route('/login/', methods=['GET', 'POST'])
def login():
	if request.method=='POST': 
		user = User(random.randint(1,20), request.form['username'])
		session["current_user"] = {
			"id": user.idd,
			"username": user.username
		}
		return redirect(url_for('home'))
	return render_template('login.html')

@app.route('/signup')
@app.route('/signup/')
def register():
	return render_template('signup.html')

@app.route('/home', methods=['GET', 'POST'])
@app.route('/home/', methods=['GET', 'POST'])
def home():
	return render_template('home.html', user=str(session['current_user']['username']))

@app.route('/logout')
@app.route('/logout/')
def logout():
	return redirect(url_for('login'))
