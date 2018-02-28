

class Dashboard(object):

	def __init__(self, user):

		self.user = user
		self.email = user.email
		

	def getEmail(self):
		return self.email