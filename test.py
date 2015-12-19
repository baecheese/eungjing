# -*- coding: utf-8 -*-


# eungjing module
from model.user import User
from model.eungalog import Eungalog
from repository.userDao import UserDao
from repository.eungalogDao import EungalogDao

import sys

reload(sys)
sys.setdefaultencoding('utf-8')

user_dao = UserDao()
eungalog_dao = EungalogDao()

def test_find_user ():
    print('>> find_user test....')
    print user_dao.find_user("jing").__dict__

def test_create_user() :
    print('>> create_user test....')
    user = User("pfdd2dfdf", "1234qwer", "1", "1", "1", '1')
    print user_dao.create_user(user) == True

def test_find_all_log() :
    print('>> find_all_log test')
    data = eungalog_dao.find_all_log("testID")
    print (data[0].__dict__)


if __name__ == "__main__" :
    print ("> user dao test")
    #test_find_user()
    #test_create_user()
    test_find_all_log()