# -*- coding: utf-8 -*-

import pymysql

from model.user import User

class UserDao :

    def create_user(self, user) :
        db = pymysql.connect("localhost","eungjing","eungjing","EUNGJING" )
        cursor = db.cursor()

        sql = "INSERT INTO USERS(name, password, hint_Q, hint_A, job, smoking) VALUE ('%s', '%s', '%s', '%s', '%s', '%i');" % (user.name, user.password, user.hint_Q, user.hint_A, user.job, user.smoking)
        print(sql)
        try :
            cursor.execute(sql)
            db.commit()
            db.close()
            return True
        except :
            db.rollback()
            db.close()
            return False

    def find_user(self, user_name) :
        user = None
        db = pymysql.connect("localhost","eungjing","eungjing","EUNGJING")
        cursor = db.cursor()
        try :
            cursor.execute('select * from USERS where name="%s"' % user_name)
            data = cursor.fetchone()
            user = User(data[0], data[1], data[2], data[3], data[4], data[5])
        except :
            db.rollback()
        db.close()
        return user
