# -*- coding: utf-8 -*-

import MySQLdb

from model.user import User

class UserDao :
    def __init__(self):
        print('init user_dao')

    ''' 수정 필요
    def create_user(self, user) :
        sql = "INSERT INTO USERS(name, password, hint_Q, hint_A, job, smoking) VALUE ('jing', '1234qwer', 'hint_Q', 'hint_A', 'job', True);"
        print (sql)
        db = MySQLdb.connect("localhost","eungjing","eungjing","EUNGJING" )
        cursor = db.cursor()
        try :
            cursor.execute(sql)
            print (cursor.fetchone())
            db.close()
            return True
        except :
            db.rollback()
            db.close()
            return False
    '''

    def find_user(self, user_name) :
        user = None
        db = MySQLdb.connect("localhost","eungjing","eungjing","EUNGJING" )
        cursor = db.cursor()
        try :
            cursor.execute('select * from USERS where name="%s"' % user_name)
            data = cursor.fetchone()
            user = User(data[0], data[1], data[2], data[3], data[4], data[5])
        except :
            db.rollback()
        db.close()
        return user
