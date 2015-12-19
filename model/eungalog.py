# -*- coding: utf-8 -*-

class Eungalog :
	
	def __init__ (self, weather, size, feature, satisfaction, user_name) :
		self.weather = weather
		self.size = size
		self.feature = feature
		self.satisfaction = satisfaction
		self.create_drip()
		self.user_name = user_name

	def create_drip (self) :
		self.drip = self.select_satisfaction_drip() + " " + self.select_size_drip()+ " " + self.select_feature_drip() + " " + self.select_weather_drip()

	def select_weather_drip (self):
		result = ""
		if self.weather == "1" :
			result = "아름다운 날씨이다. 눈이 부시다.. 크극.. 결계인가..?"
		elif self.weather == "2" :
			result = "거사를 치루고 나니 어둠의 다크가 밀려온다.."
		elif self.weather == "3" :
			result = "날씨가 구리구리 말똥구리."
		elif self.weather == "4" :
			result = "바지가 젖었다.. 아니.. 다른이유는 아니고 비 때문에.."
		elif self.weather == "5" :
			result = "다음번에는 눈에다가 똥을 싸보고 싶다. 낭만적이군."
		elif self.weather == "6" :
			result = "창밖에 불벼락이 내리고 있다. 세상이 멸망하려나?"
		else :
			"none"
		return result

	def select_size_drip (self):
		result = ""
		if self.size == "1" :
			result = "내 안에 흑룡이 날뛰고 있었다."
		elif self.size == "2" :
			result = "하여튼 엄청난 것이 또라이를 틀고 있었다.."
		elif self.size == "3" :
			result = "뭐, 보통의 똥이었다.(새침)"
		elif self.size == "4" :
			result = "조금 실망스러운 사이즈였다. 이것이 나의 그릇이란 말인가.."
		elif self.size == "5" :
			result = "물을 내리기가 미안하다."
		elif self.size == "6" :
			result = "실패한 고통보다 최선을 다하지 못했음을 깨닫는 것이 더 고통스럽다."
		return result

	def select_feature_drip (self):
		result = ""
		if self.feature == "1" :
			result = "그치만 특별한 것은 없다."
		elif self.feature == "2" :
			result = "내가 사장님을 밀치고 왔다는 건 이미 거사가 끝난 후에나 생각이 났다."
		elif self.feature == "3" :
			result = "뭐, 보통의 똥이었다.(새침)"
		elif self.feature == "4" :
			result = "카네기는 이런 말을 했다. '큰일을 먼저 하라. 작은 일은 저절로 해결 될 것이다.' 관장약을 꺼낼 때가 왔다."
		elif self.feature == "5" :
			result = "어리석은 닝겐들아!! 니들의 잣대로 날 판단하지마라!!!!"
		return result

	def select_satisfaction_drip (self):
		result = ""
		if self.satisfaction == "1" :
			result = "크크크크......캬컄캬컄하하핳!! 쿠퀙웩..쿨ㄹ룩.. (실신)"
		elif self.satisfaction == "2" :
			result = "역시 세상의 정답은 내 안에 있었다. 하.하.하.하!"
		elif self.satisfaction == "3" :
			result = "훗.."
		elif self.satisfaction == "4" :
			result = "룰루랄라~"
		elif self.satisfaction == "5" :
			result = " 화장실에서 나오며 생각했다. 내가 뭘 하고 나왔더라?"
		elif self.satisfaction == "6" :
			result = "똥조차도 나를 무시하는군."
		elif self.satisfaction == "7" :
			result = "이런 X발."
		return result