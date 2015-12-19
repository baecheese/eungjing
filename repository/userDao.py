# -*- coding: utf-8 -*-

import pymysql

from model.user import User

import sys

reload(sys)
sys.setdefaultencoding('utf-8')

class UserDao :

    def create_user(self, user) :
        try :
            db = pymysql.connect("localhost","eungjing","eungjing","EUNGJING", charset='utf8', init_command='SET NAMES UTF8')
            cursor = db.cursor()
            sql = "INSERT INTO USERS(name, password, hint_Q, hint_A, job, smoking) \
            VALUE ('%s', '%s', '%s', '%s', '%s', '%i');" % \
            (user.name, user.password, user.hint_Q, user.hint_A, user.job, user.smoking)
            cursor.execute(sql)
            db.commit()
            db.close()
            return True
        except Exception as exception:
            print(exception.__class__.__name__)
            db.rollback()
            db.close()
            return False

    def find_user(self, user_name) :
        user = None
        try :
            db = pymysql.connect("localhost","eungjing","eungjing","EUNGJING")
            cursor = db.cursor()
            cursor.execute('select * from USERS where name="%s"' % user_name)
            data = cursor.fetchone()
            user = User(data[0], data[1], data[2], data[3], data[4], data[5])
        except :
            db.rollback()
        db.close()
        return user
