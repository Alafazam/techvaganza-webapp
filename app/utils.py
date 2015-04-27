from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_security import Security, SQLAlchemyUserDatastore, \
    UserMixin, RoleMixin, login_required,roles_required,roles_accepted,current_user
# import pprint
from models import User,Role,Events

from app import user_datastore,db


def add_event_to_user(user, Event):
	"""Adds an event to a user.
	:param user: The user to manipulate
	:param role: The role to add to the user
	user is user.id 
	event is event.
	"""
	# print user.id
	if Event not in user.events:
		user.events.append(Event)
		user_datastore.put(user)
		db.session.commit()
		return True
	return False


def get_role(role):
	res = Role.query.filter_by(name=role).first()
	return res

def get_event(event):
	res = Events.query.filter_by(name=events).first()
	return res

def get_all_events():
	res = Events.query.order_by(Events.id).all()
	return res

def get_user(email):
	res = user_datastore.find_user(email=email)
	return res

def get_all_organisors():
	res = User.query(User.username).filter(User.roles.any(name='event_organisor'))
	return res
# filter(Blog.keywords.any(Keyword.name.in_(['keyword1', 'keyword2', ...])))

# utils = __name__
# def _prepare_role_modify_args(self, user, Event):
#         if isinstance(user, string_types):
#             user = self.find_user(email=user)
#         if isinstance(role, string_types):
#             role = self.find_role(role)
#         return user, role

