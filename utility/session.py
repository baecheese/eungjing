from flask import session

def getLoginedUserName () :
    return session['username']

def setLoginedUserName(user_name) :
    session['username'] = user_name
    print(session['username'])

def isLogined ():
    try :
        return session['username'] is not None
    except :
        False

def session_logout() :
    session['username'] = None