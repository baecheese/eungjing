# -*- coding: utf-8 -*-

class User :
	
	def __init__ (self, name, password, hint_Q, hint_A) :
		self.name = name
		self.password = password
		self.hint_Q = self.select_hint_Q(hint_Q)
		self.hint_A = hint_A

	def select_hint_Q (self, hint_Q) :
		if hint_Q == "1" :
			return "당신의 이름은 무엇인가요?"
		elif hint_Q == "2" :
			return "당신의 태어난 해는 언제인가요?"
		elif hint_Q == "3" :
			return "당신의 반려동물 이름은 무엇인가요?"
		else :
			"none";




