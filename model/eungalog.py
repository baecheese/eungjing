# -*- coding: utf-8 -*-

class Eungalog :
	
	def __init__ (self, sex, age, height, weight, time, symptom, satisfaction, etc_note) :
		self.sex = sex # 남,여에 대한 이후 선택지 있어야 할지 묻기
		self.age = age
		self.height = height
		self.weight = weight
		self.time = time
		self.symptom = symptom # 목록 추가
		self.satisfaction = satisfaction # 목록 추가
		self.etc_note = etc_note

	# def select_hint_Q (self, hint_Q) :
	# 	if hint_Q == "1" :
	# 		return "당신의 이름은 무엇인가요?"
	# 	elif hint_Q == "2" :
	# 		return "당신의 태어난 해는 언제인가요?"
	# 	elif hint_Q == "3" :
	# 		return "당신의 반려동물 이름은 무엇인가요?"
	# 	else :
	# 		"none";

