from flask import session

def getLoginedUserName () :
    return session['username']

def setLoginedUserName(user_name) :
    session['username'] = user_name

def isLogined ():
    return None != session['username']