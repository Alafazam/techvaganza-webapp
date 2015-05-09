# manage.py
from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for
from flask.ext.security import Security, SQLAlchemyUserDatastore, \
    UserMixin, RoleMixin, login_required,roles_required,roles_accepted,current_user
from flask_mail import Mail
from flask.ext.script import  Command, Manager, Option
from app import app,db,user_datastore,User,Role,Events
from app.utils import add_event_to_user,get_user,get_role,get_event,get_all_events,get_all_organisors,unregister_to_event,get_all_user_events
from werkzeug import secure_filename

import os

manager = Manager(app)

@manager.command
def hello():
    print "hello"


# utility methods to create role , adding roles to user etc
@manager.command
def add_new_role(name,description):
	user_datastore.create_role(name=name,description=description)
	db.session.commit()

@manager.command
def add_role_to_user(email,role):
	user = user_datastore.find_user(email=email)
	user_datastore.add_role_to_user(user,role)
	db.session.commit()


@manager.command
def user(email):
	res = get_user(email)
	print res
	# return res

@manager.command
def role(role):
	res = Role.query.filter_by(name=role).first()
	print res
	# return res

@manager.command
def user_events(email):
	user = get_user(email)
	print user.events

@manager.command
def event(event):
	res = Events.query.filter_by(name=events).first()
	print res
	# return res



@manager.command
def create_all():
	db.create_all()
	db.session.commit()


@manager.command
def add_event_to_userz(email,event):
	user = get_user(email)
	event = Events.query.filter_by(name=event).first()
	print add_event_to_user(user,event)

@manager.command
def unregister(email,event):
	print unregister_to_event(email,event)



@manager.command
def see_events():
	print get_all_events()

@manager.command
def organisors():
	print get_all_organisors()


# @manager.command
# def pathname(filename):
# 	print os.path.join(app.config['UPLOAD_FOLDER'], filename)


# @manager.command
# def secame(filename):
# 	print secure_filename(filename)











if __name__ == "__main__":
    manager.run()