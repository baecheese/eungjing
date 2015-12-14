# -*- coding: utf-8 -*-
from flask import Flask, jsonify, render_template, request, url_for
app = Flask(__name__)

''' database 관련은 일단 주석처리 해둠. '''
# from flaskext.mysql import MySQL
 
# mysql = MySQL()
# app.config['MYSQL_DATABASE_USER'] = 'jing'
# app.config['MYSQL_DATABASE_PASSWORD'] = ''
# app.config['MYSQL_DATABASE_DB'] = 'eungjing'
# app.config['MYSQL_DATABASE_HOST'] = 'localhost'
# mysql.init_app(app)

# eungjing module
from model.user import User
from model.eungalog import Eungalog

@app.route('/')
def index () :
	return render_template('index.html')

@app.route('/user', methods=['POST'])
def create_user() :
	# json 데이터를 프론트로부터 받아서 user 클래스로 변경.
	json = request.json
	user = User(json['name'], json['password'], json['hint_Q']
				, json['hint_A'], json['job'], json['smoking'])
	return "success"

@app.route('/user', methods=['GET'])
def read_user() :
	user = User("ppu", "1234", "3", "cheese", "1", "1")
	# user class를 json으로 변경.
	return jsonify(user.__dict__)

# ----------- 응가 일지 ---------------------

@app.route('/eungalog', methods=['POST'])
def create_eungalog() :
	json = request.json
	eungalog = Eungalog(json['weather'], json['size']
						, json['feature'], json['satisfaction'], json['user_name'])
	# databas에 eungalog를 저장한다.
	return jsonify(eungalog.__dict__)

@app.route('/eungalog', methods=['GET'])
def read_eungalog() :
	eungalog = Eungalog("1", "1", "2", "7", "jing")
	# user class를 json으로 변경.
	return jsonify(eungalog.__dict__)


# start server
if __name__ == "__main__" :
	print('starting server....')
	app.run(host='127.0.0.1', port=3000)