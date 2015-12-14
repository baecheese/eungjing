# -*- coding: utf-8 -*-

class Eungalog :
	
	def __init__ (self, weather, size, feature, satisfaction, user_name) :
		self.weather = self.select_weather(weather)
		self.size = self.select_size(size)
		self.feature = self.select_feature(feature)
		self.satisfaction = self.select_satisfaction(satisfaction)
		self.create_drip()
		self.user_name = user_name
		# self.date_time = 
		# 파이썬 시간 정보, 날짜 정보 넣는 법 찾아서 넣기.

	def create_drip (self) :
		self.drip = self.select_satisfaction_drip() + " " + self.select_size_drip()+ " " + self.select_feature_drip() + " " + self.select_weather_drip()

	def select_weather (self, weather) :
		if weather == "1" :
			return "맑음"
		elif weather == "2" :
			return "흐림"
		elif weather == "3" :
			return "구림"
		elif weather == "4" :
			return "비"
		elif weather == "5" :
			return "눈"
		elif weather == "6" :
			return "불벼락"
		else :
			"none";

	def select_weather_drip (self):
		result = ""
		if self.weather == "맑음" :
			result = "아름다운 날씨이다. 눈이 부시다.. 크극.. 결계인가..?"
		elif self.weather == "흐림" :
			result = "거사를 치루고 나니 어둠의 다크가 밀려온다.."
		elif self.weather == "구림" :
			result = "날씨가 구리구리 말똥구리."
		elif self.weather == "비" :
			result = "바지가 젖었다.. 아니.. 다른이유는 아니고 비 때문에.."
		elif self.weather == "눈" :
			result = "다음번에는 눈에다가 똥을 싸보고 싶다. 낭만적이군."
		elif self.weather == "불벼락" :
			result = "창밖에 불벼락이 내리고 있다. 세상이 멸망하려나?"
		else :
			"none"
		return result	


	def select_size (self, size) :
		if size == "1" :
			return "인간의 것을 초월"
		elif size == "2" :
			return "크다"
		elif size == "3" :
			return "중간"
		elif size == "4" :
			return "조금"
		elif size == "5" :
			return " . ←이정도..?"
		elif size == "6" :
			return "실패"
		else :
			"none";

	def select_size_drip (self):
		result = ""
		if self.size == "인간의 것을 초월" :
			result = "내 안에 흑룡이 날뛰고 있었다."
		elif self.size == "크다" :
			result = "하여튼 엄청난 것이 또라이를 틀고 있었다.."
		elif self.size == "중간" :
			result = "뭐, 보통의 똥이었다.(새침)"
		elif self.size == "조금" :
			result = "조금 실망스러운 사이즈였다. 이것이 나의 그릇이란 말인가.."
		elif self.size == " . ←이정도..?" :
			result = "물을 내리기가 미안하다."
		elif self.size == "실패" :
			result = "실패한 고통보다 최선을 다하지 못했음을 깨닫는 것이 더 고통스럽다."
		else :
			"none";			
		return result

	def select_feature (self, feature) :
		if feature == "1" :
			return "없음"
		elif feature == "2" :
			return "원인 불명의 급똥"
		elif feature == "3" :
			return "치질"
		elif feature == "4" :
			return "변비"
		elif feature == "5" :
			return "그 외의 설명하기 어려운.."
		else :
			"none";

	def select_feature_drip (self):
		result = ""
		if self.feature == "없음" :
			result = "그치만 특별한 것은 없다."
		elif self.feature == "원인 불명의 급똥" :
			result = "내가 사장님을 밀치고 왔다는 건 이미 거사가 끝난 후에나 생각이 났다."
		elif self.feature == "치질" :
			result = "뭐, 보통의 똥이었다.(새침)"
		elif self.feature == "변비" :
			result = "카네기는 이런 말을 했다. '큰일을 먼저 하라. 작은 일은 저절로 해결 될 것이다.' 관장약을 꺼낼 때가 왔다."
		elif self.feature == "그 외의 설명하기 어려운.." :
			result = "어리석은 닝겐들아!! 니들의 잣대로 날 판단하지마라!!!!"
		else :
			"none";
		return result

	def select_satisfaction (self, satisfaction) :
		if satisfaction == "1" :
			return "인생 최고의 날"
		elif satisfaction == "2" :
			return "극상의 만족"
		elif satisfaction == "3" :
			return "만족"
		elif satisfaction == "4" :
			return "보통"
		elif satisfaction == "5" :
			return "애매함"
		elif satisfaction == "6" :
			return "불만족"
		elif satisfaction == "7" :
			return "분노"
		else :
			"none";

	def select_satisfaction_drip (self):
		result = ""
		if self.satisfaction == "인생 최고의 날" :
			result = "크크크크......캬컄캬컄하하핳!! 쿠퀙웩..쿨ㄹ룩.. (실신)"
		elif self.satisfaction == "극상의 만족" :
			result = "역시 세상의 정답은 내 안에 있었다. 하.하.하.하!"
		elif self.satisfaction == "만족" :
			result = "훗.."
		elif self.satisfaction == "보통" :
			result = "룰루랄라~"
		elif self.satisfaction == "애매함" :
			result = " 화장실에서 나오며 생각했다. 내가 뭘 하고 나왔더라?"
		elif self.satisfaction == "불만족" :
			result = "똥조차도 나를 무시하는군."
		elif self.satisfaction == "분노" :
			result = "이런 시발."
		else :
			"none"
		return result