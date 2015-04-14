from techvaganza import db, app

# We store country name too, because of cities like Amsterdam (There are 2 cities called Amsterdam. One in the U.S, one in Netherland )

class City(db.Model):
	__tablename__ = 'city'
	id = db.Column(db.Integer, primary_key = True)
	name = db.Column(db.String(255), unique = True)
	city_image = db.Column(db.Text())
	country = db.Column(db.String(255))

	restaurant = db.relationship('Restaurant', backref = 'city', lazy = 'dynamic')
	moderator = db.relationship('Moderator', backref = 'city', lazy = 'dynamic')

	def __repr__(self):
		return '<City %r>' % (self.name)

# Moderators per city
# We store the important moderator data here too, for quick reference. I think an independent model will make queries easies than a many-many setup
# Also some folks can be the moderator of 2 or more events this way

class Moderator(db.Model):
	__tablename__= 'moderator'
	id = db.Column(db.Integer, primary_key = True)
	firstname = db.Column(db.String(255))
	lastname = db.Column(db.String(255))
	image_location = db.Column(db.Text())
	email = db.Column(db.String(255))

	city_id = db.Column(db.Integer, db.ForeignKey('city.id'))
	modnotification = db.relationship('Modnotification', backref = 'moderator', lazy = 'dynamic')

	def __repr__(self):
		return '<Moderator %r>' % (self.email)

class Modnotification(db.Model):
	__tablename__ = "modnotification"
	id = db.Column(db.Integer, primary_key = True)
	poster_name = db.Column(db.String(255))
	link = db.Column(db.Text())
	# link to page
	time = db.Column(db.Text())
	read = db.Column(db.Integer)

	moderator_id = db.Column(db.Integer, db.ForeignKey('moderator.id'))

	def __repr__(self):
		return '<Modnotification %r>' % (self.time)

