# -*- coding: utf-8 -*-

import pymysql
import sys
import traceback

from model.log import Log

reload(sys)
sys.setdefaultencoding('utf-8')

class EungalogDao :

    def create_log(self, eungalog) :
        try :
            db = pymysql.connect("localhost","eungjing","eungjing","EUNGJING", charset='utf8', init_command='SET NAMES UTF8')
            cursor = db.cursor()
            sql = "INSERT INTO eungalog(user_name, weather, size, feature, satisfaction, eunga_drip) value ('%s', '%s', '%s', '%s', '%s', '%s');" % \
                  (eungalog.user_name, eungalog.weather, eungalog.size, eungalog.feature, eungalog.satisfaction, eungalog.drip )
            print(sql)
            cursor.execute(sql)
            db.commit()
            db.close()
        except Exception as e:
            print(e.__class__.__name__)
            db.rollback()
            db.close()

    def find_all_log(self, user_name) :
        try :
            db = pymysql.connect("localhost","eungjing","eungjing","EUNGJING", charset='utf8', init_command='SET NAMES UTF8')
            cursor = db.cursor()
            sql = "select * from eungalog where user_name='%s' order by createDate desc;" % (user_name)
            print(sql)
            cursor.execute(sql)
            result = []
            for row in cursor :
                result.append(Log(row[6], row[2], row[3], row[4], row[5], row[7], row[0]))
            return result
        except Exception as e:
            print(e.__class__.__name__)
            db.rollback()
            db.close()

    def delete_by_log_id(self, logId):
        print 1
        try :
            db = pymysql.connect("localhost","eungjing","eungjing","EUNGJING", charset='utf8', init_command='SET NAMES UTF8')
            cursor = db.cursor()
            sql = "DELETE from eungalog where id='%s';" % logId
            print(sql)
            cursor.execute(sql)
            db.commit()
            db.close()
            return True
        except :
            print(traceback.format_exc())
            db.rollback()
            db.close()
            return False
