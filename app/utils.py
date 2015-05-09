from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_security import Security, SQLAlchemyUserDatastore, \
    UserMixin, RoleMixin, login_required,roles_required,roles_accepted,current_user
# import pprint
from models import User,Role,Events

from app import user_datastore,db


def contains(list, filter):
    for x in list:
        if filter(x):
            return x
    return None




def add_event_to_user(userO, Event):
	"""Adds an event to a user.
	:param user: The user to manipulate
	:param role: The role to add to the user
	user is email 
	Event is Event name.
	alafazam@gmail.com fulcrum
	"""
	user = get_user(userO)
	event = Events.query.filter_by(view_name=Event).first()
	# print user.id
	# print user.events
	check2 = contains(user.events, lambda x: x.view_name == event.view_name)
	# print check2
	# if Event not in user.events:
	if check2 is None:
		user.events.append(event)
		user_datastore.put(user)
		db.session.commit()
		return True
	return False


def unregister_to_event(userO,Event):
	user = get_user(userO)
	event = Events.query.filter_by(view_name=Event).first()
	check2 = contains(user.events, lambda x: x.view_name == event.view_name)
	# print check2
	if check2 is not None:
		user.events.remove(event)
		user_datastore.put(user)
		db.session.commit()
		return True
	return False




def get_role(role):
	res = Role.query.filter_by(name=role).first()
	return res

def get_event(event):
	res = Events.query.filter_by(event_id=event).first()
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

def get_all_user_events(userE):
	user = get_user(userE)
	return user.events
# filter(Blog.keywords.any(Keyword.name.in_(['keyword1', 'keyword2', ...])))

# utils = __name__
# def _prepare_role_modify_args(self, user, Event):
#         if isinstance(user, string_types):
#             user = self.find_user(email=user)
#         if isinstance(role, string_types):
#             role = self.find_role(role)
#         return user, role


