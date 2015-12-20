# -*- coding: utf-8 -*-

from flask import session

import traceback

def getLoginedUserName () :
    try :
        return session['user']
    except :
        print(traceback.format_exc())

def setLoginedUserName(user_name) :
    session['user'] = user_name
    print(session['user'])

def isLogined ():
    try :
        return session['user'] is not None
    except :
        False

def session_logout() :
    session['user'] = None