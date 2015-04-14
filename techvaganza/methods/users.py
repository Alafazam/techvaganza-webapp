from vedge import vedge, db, models, login_manager
from vedge.models import core

login_manager.login_message = "Nauh son. Not here"

@login_manager.user_loader
def load_user(userid):
	try:
		user = core.User.query.filter_by(id = userid).first()
		return user
	except:
		return None