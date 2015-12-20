# -*- coding: utf-8 -*-

import sys

reload(sys)
sys.setdefaultencoding('utf-8')

class Log :
    def __init__(self, drip, weather, size, feature, satisfaction, datetime, id):
        self.drip = drip
        self.weather = self.__setWeatherString__(weather)
        self.size = self.__setSizeString__(size)
        self.feature = self.__setFeatureString__(feature)
        self.satisfaction = self.__setSatisfactionString__(satisfaction)
        self.datetime = datetime
        self.id = id

    def __setWeatherString__(self, weather):
        if weather == u'1' :
            return u'맑음'
        elif weather == u'2' :
            return u'흐림'
        elif weather == u'3' :
            return u'구림'
        elif weather == u'4' :
            return u'비'
        elif weather == u'5' :
            return u'눈'
        elif weather == u'6' :
            return u'불벼락'

    def __setSizeString__(self, size):
        if size == u'1' :
            return u'인간초월'
        elif size == u'2' :
            return u'크다'
        elif size == u'3' :
            return u'중간'
        elif size == u'4' :
            return u'작다'
        elif size == u'5' :
            return u' . <- 요 정도?'
        elif size == u'6' :
            return u'실패..'

    def __setFeatureString__(self, feature):
        if feature == u'1' :
            return u'없음'
        elif feature == u'2' :
            return u'급똥'
        elif feature == u'3' :
            return u'치질'
        elif feature == u'4' :
            return u'변비'
        elif feature == u'5' :
            return u'그 외의 무언가'

    def __setSatisfactionString__(self, satisfaction):
        if satisfaction == u'1' :
            return u'인생최고의 날'
        elif satisfaction == u'2' :
            return u'극상의 만족'
        elif satisfaction == u'3' :
            return u'보통'
        elif satisfaction == u'4' :
            return u'애매함'
        elif satisfaction == u'5' :
            return u'불만족'
        elif satisfaction == u'6' :
            return u'분노'






