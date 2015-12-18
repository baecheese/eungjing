# -*- coding: utf-8 -*-
from flask import Flask, jsonify, render_template, request, url_for, redirect

app = Flask(__name__)

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
		return render_template('eungalog.html')
	else :
		return render_template('index.html')

@app.route('/user', methods=['POST'])
def create_user() :
	print(">>> create user")
	json = request.json
	user = User(json['name'], json['password'], json['hint_Q'], json['hint_A'], json['job'], json['smoking'])
	if user_dao.create_user(user) :
		return "success"
	else :
		return "fail", 406

@app.route('/user/form', methods=['GET'])
def user_form() :
	return render_template('user_form.html')

@app.route('/user/login', methods=['POST'])
def login() :
	user = request.form
	if True : # db에 해당하는 user name이 있고 pw가 일치한다면,
		setLoginedUserName(user['name'])
		return redirect(url_for('form_eungalog'))
	else :
		return False

@app.route('/user/<string:user_name>', methods=['GET'])
def read_user(user_name) :
	user = user_dao.find_user(user_name)
	return jsonify(user.__dict__)

# ----------- 응가 일지 ---------------------

@app.route('/eungalog', methods=['POST'])
def create_eungalog() :
	json = request.json
	eungalog = Eungalog(json['weather'], json['size']
						, json['feature'], json['satisfaction'], json['user_name'])
	# databas에 eungalog를 저장한다.
	return jsonify(eungalog.__dict__)

@app.route('/user/<string:user_name>/eungalog', methods=['GET'])
def read_eungalog(user_name) :
	# 유저 데이터를 받을 것.
	# 데이터베이스에서 user_name 기준으로 데이터를 꺼내올 것. 리스트로.
	# 시간 역순 대로 돌려줄 것.(가장 최근 것이 가장 위로)
	eungalog = Eungalog("1", "1", "2", "7", user_name)
	# user class를 json으로 변경.
	return jsonify(eungalog.__dict__)

@app.route('/eungalog', methods=['GET'])
def form_eungalog () :
	user_name = getLoginedUserName() # 활용해서 페이지 렌더링.
	return render_template('eungalog.html', user_name=user_name)


# 비밀키
app.secret_key="dfdsfdafsdfa181280083ljkandfan12974ldsfjassfasdfalsknfafnsd"

# start server
if __name__ == "__main__" :
	print('starting server....')
	app.run(host='127.0.0.1', port=3000)