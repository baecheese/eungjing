# -*- coding: utf-8 -*-
from flask import Flask, jsonify, render_template, request, url_for, redirect
from flask.ext.bcrypt import Bcrypt

import sys

reload(sys)
sys.setdefaultencoding('utf-8')


app = Flask(__name__)
bcrypt = Bcrypt(app)

# eungjing module
from model.user import User
from model.eungalog import Eungalog
from repository.userDao import UserDao
from repository.eungalogDao import EungalogDao
from utility.session import *

user_dao = UserDao()
eungalog_dao = EungalogDao()

@app.route('/')
def index () :
	if isLogined() :
		return redirect(url_for('form_eungalog'))
	else :
		return render_template('index.html')

@app.route('/user/form', methods=['GET'])
def user_form() :
	return render_template('user_form.html')

@app.route('/user', methods=['POST'])
def create_user() :
	json = request.json
	password = bcrypt.generate_password_hash(json['password'])
	user = User(json['name'], password, json['hint_Q'], json['hint_A'], json['job'], json['smoking'])
	if user_dao.create_user(user) :
		return "success"
	else :
		return "fail", 406

@app.route('/user/login', methods=['POST'])
def login() :
	user = request.form
	if isMember(user) :
		setLoginedUserName(user['name'])
		return redirect(url_for('form_eungalog'))
	else :
		return render_template('index.html')

def isMember(user) :
	try :
		db_user = user_dao.find_user(user['name'])
		return bcrypt.check_password_hash(db_user.password, user['password'])
	except :
		return False

@app.route('/user/logout', methods=['GET'])
def logout ():
	session_logout()
	return redirect(url_for('index'))


@app.route('/user/<string:user_name>', methods=['GET'])
def read_user(user_name) :
	user = user_dao.find_user(user_name)
	return jsonify(user.__dict__)

# ----------- 응가 일지 ---------------------

@app.route('/eungalog', methods=['GET'])
def form_eungalog () :
	if isLogined() :
		user = user_dao.find_user(getLoginedUserName())
		log_list = eungalog_dao.find_all_log(user.name)
		return render_template('eungalog.html', user_name=user.name, user_image=user.job, log_list=log_list)
	else :
		return render_template('index.html')

@app.route('/eungalog', methods=['POST'])
def create_eungalog() :
	form = request.form
	user = user_dao.find_user(getLoginedUserName())
	eungalog = Eungalog(form['weather'], form['size'], form['feature'], form['satisfaction'], user.name)
	eungalog_dao.create_log(eungalog)
	log_list = eungalog_dao.find_all_log(user.name)
	return render_template('eungalog.html', user_name=user.name, user_image=user.job, log_list=log_list)

# 비밀키
app.secret_key="dfdsfdafsdfa181280083ljkandfan12974ldsfjassfasdfalsknfafnsd"

# start server
if __name__ == "__main__" :
	print('starting server....')
	app.run(host='127.0.0.1', port=3000)