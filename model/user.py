# -*- coding: utf-8 -*-

class User :
	
	def __init__ (self, name, password, hint_Q, hint_A, job, smoking) :
		self.name = name
		self.password = password
		self.hint_Q = self.select_hint_Q(hint_Q)
		self.hint_A = hint_A
		self.job = self.select_job(job)
		self.smoking = self.select_smoking(smoking) 
		    # 흡연여부 - 체크박스 yes, no도 API 만드는지 확인

	def select_hint_Q (self, hint_Q) :
		if hint_Q == "1" :
			return "당신이 태어난 지역은 어디인가요?"
		elif hint_Q == "2" :
			return "당신이 좋아하는 색깔은 무엇인가요?"
		elif hint_Q == "3" :
			return "당신의 반려동물 이름은 무엇인가요?"
		else :
			"none";


	def select_job (self, job) :
		if job == "1" :
			return "남자 사람"
		elif job == "2" :
			return "여자 사람"
		elif job == "3" :
			return "고양이"
		elif job == "4" :
			return "개"
		elif job == "5" :
			return "그 외의 무언가.."
		else :
			"none";

	def select_smoking (self, smoking) :
		if smoking == "1" :
			return "YES"
		elif smoking == "2" :
			return "NO"
		else :
			"none";


