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
		if hint_Q == "1" or hint_Q == "where is your born location?" :
			return "where is your born location?"
		elif hint_Q == "2" or hint_Q == "what your like color?" :
			return "what your like color?"
		elif hint_Q == "3" or  hint_Q == "who is your pat?" :
			return "who is your pat?"
		else :
			return None

	def select_job (self, job) :
		if job == "1" or job == "man" :
			return "man"
		elif job == "2" or job == "woman" :
			return "woman"
		elif job == "3" or job == "cat" :
			return "cat"
		elif job == "4" or job == "dog" :
			return "dog"
		elif job == "5" or job == "etc" :
			return "etc"
		else :
			return None

	def select_smoking (self, smoking) :
		if smoking == "YES" :
			return True
		elif smoking == "NO" :
			return False
		else :
			return None


