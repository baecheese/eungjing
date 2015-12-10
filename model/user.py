class User :
	
	def __init__ (self, id, name) :
		self.id = id
		self.name = name

	def to_str(self) :
		return str(self.id)

