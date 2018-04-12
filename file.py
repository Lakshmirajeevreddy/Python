class name_error(Exception):
	def __init__(self):
		self.name="Over 20 characters"
	def __str__(self):
		return(self.name)
class age_error(Exception):
	def __init__(self):
		self.age="age out of bounds"
	def __str__(self):
		return(self.age)
class sport_error(Exception):
	def __init__(self):
		self.sports="List more than 5"
	def __str__(self):
		return(self.sports)
class nosport_error(Exception):
	def __init__(self):
		self.sports="sport not listed"
	def __str__(self):
		return(self.sports)
		
	
		