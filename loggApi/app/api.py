from flask import jsonify, request, session
from app import app, db
from models import Users
from flask.ext.cors import cross_origin
import os
from werkzeug.security import generate_password_hash, check_password_hash
from models import Users

@app.route('/api/login', methods=['GET', 'POST'])
@cross_origin('*')
def api_login():
	uname, pw = request.args.get('username'), request.args.get('password')
	if uname and pw:
		user = Users.query.filter_by(username=uname).first()
		if user:
			if check_password_hash(user.password, pw):

				print 'yey'
				return jsonify({'msg': 'ok', 'next_node':'/home'})
	return jsonify({'msg': 'login failed!'})


@app.route('/api/signup', methods=['GET', 'POST'])
@cross_origin('*')
def api_signup():
	uname = request.form.get('username')
	pw = request.form.get('password')
	email = request.form.get('email')

	if uname and pw and email:
		if (uname!="") and (pw!="") and (email!=""):
			user = Users(username=uname, email=email, password=pw)
			db.session.add(user)
			db.session.commit()
			print 'b'
			return jsonify({'msg': 'ok', 'next_node': '/login'})

	return jsonify({'msg': 'something went wrong!'})

@app.route('/api/home', methods=['GET', 'POST'])
@cross_origin('*')
def api_home():
	uname = request.args.get('username')
	if uname:
		user = Users.query.filter_by(username=uname).first()
		return jsonify({'msg':'ok', 'email':user.email})
	return jsonify({'msg': 'login failed!'})
