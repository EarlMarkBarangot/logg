from flask_login import AnonymousUserMixin

class User:
	idd = None
	username = None

	def __init__(self, idd, username):
		self.idd = idd
		self.username = username

	def is_authenticated(self):
		return True

	def is_anonymous(self):
		return False

	def is_active(self):
		return True

	def get_id(self):
		return self.idd

	def getid(idd):
		return User

class Anonymous(AnonymousUserMixin):
	def __init__(self):
		self.username = 'Guest'

	def isAuthenticated(Self):
		return False

	def is_active(self):
		return False

	def is_anonymous(self):
		return True