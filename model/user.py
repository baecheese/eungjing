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
			return "where is your born location?"
		elif hint_Q == "2" :
			return "what your like color?"
		elif hint_Q == "3" :
			return "who is your pat?"
		else :
			None;

	def select_job (self, job) :
		if job == "1" :
			return "man"
		elif job == "2" :
			return "woman"
		elif job == "3" :
			return "cat"
		elif job == "4" :
			return "dog"
		elif job == "5" :
			return "etc"
		else :
			"none";

	def select_smoking (self, smoking) :
		if smoking == "YES" :
			return True
		elif smoking == "NO" :
			return False
		else :
			return None;


