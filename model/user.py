# -*- coding: utf-8 -*-

class User :
	def __init__ (self, name, password, hint_Q, hint_A, job, smoking) :
		self.name = name
		self.password = password
		self.hint_Q = self.select_hint_Q(hint_Q)
		self.hint_A = hint_A
		self.job = self.select_job(job)
		self.smoking = self.select_smoking(smoking)

	def select_hint_Q (self, hint_Q) :
		if hint_Q == "1" :
			return u"당신이 태어난 지역은 어디인가요?"
		elif hint_Q == "2" :
			return u"당신이 좋아하는 색깔은 무엇인가요?"
		elif hint_Q == "3" :
			return u"당신의 반려동물 이름은 무엇인가요?"
		else :
			"none";

	def select_job (self, job) :
		if job == "1" :
			return u"남자 사람"
		elif job == "2" :
			return u"여자 사람"
		elif job == "3" :
			return u"고양이"
		elif job == "4" :
			return u"개"
		elif job == "5" :
			return u"그 외의 무언가.."
		else :
			"none";

	def select_smoking (self, smoking) :
		if smoking == u"YES" :
			return True
		elif smoking == u"NO" :
			return False
		else :
			"none";

	def toString(self) :
		return "name: %s\npassword: %s\nhint_Q: %s\nhint_A: %s\njob: %s\nsmoking: %r" %\
			   (self.name, self.password, self.hint_Q, self.hint_A, self.job, self.smoking)


