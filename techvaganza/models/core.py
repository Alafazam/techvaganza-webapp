from vedge import db, vedge
from werkzeug import generate_password_hash, check_password_hash
import datetime, hashlib, uuid, flask.ext.whooshalchemy

class User(db.Model):
	__tablename__ = 'user'
	id = db.Column(db.Integer, primary_key = True)
	username = db.Column(db.String(255), unique = True)
	firstname = db.Column(db.String(255))
	lastname = db.Column(db.String(255))
	email = db.Column(db.String(255), unique = True)
	image_location = db.Column(db.String(255))
	user_status = db.Column(db.Integer)
	pwdhash = db.Column(db.String(255))
	salt = db.Column(db.String(255))
	
	def __init__(self, username, fullname, email, image_location, password):
		self.set_username(username)
		self.set_name(fullname)
		self.email = email
		self.salt = uuid.uuid4().hex
		if email in vedge.config['MASTER_EMAIL']:
			self.user_status = 1
		else:
			self.user_status = 0
		self.set_password(password + self.salt)
		self.set_defaults()
		self.image_location = image_location

	# Required for Client-Side Session Management

	def is_authenticated(self):
		return True

	def is_active(self):
		return True

	def is_anonymous(self):
		return False

	def get_id(self):
		return self.id

	# Required for Administrative Interface

	def __unicode__(self):
		return self.username

	def set_username(self, username):
		for i in username:
			if i != " ":
				pass
			else:
				raise Exception("Invalid username")
		self.username = username		

	def set_name(self, fullname):
		for i in fullname:
			if i != " ":
				try:
					int(i)
				except ValueError:
					pass
				else:
					raise Exception("Invalid Input")	
		try:
			self.firstname, self.lastname = fullname.split(" ")
		except ValueError:
			self.firstname = fullname
			self.lastname = None

	def set_password(self, password):
		self.pwdhash = generate_password_hash(password)

	def check_password(self, password):
		salt = uuid.uuid4().hex
		return check_password_hash(self.pwdhash, password + self.salt)

	def set_defaults(self):
		self.image_location = "/static/img/default.png"

	def __repr__(self):
		return '<User %r>' % (self.username)