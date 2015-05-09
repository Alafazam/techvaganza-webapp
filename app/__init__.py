import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_security import Security, SQLAlchemyUserDatastore, \
    UserMixin, RoleMixin, login_required,roles_required,roles_accepted
from flask_mail import Mail
from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for
from flask_security import Security, SQLAlchemyUserDatastore, \
    UserMixin, RoleMixin, login_required,roles_required,roles_accepted,current_user
from flask import Flask, request, redirect, url_for



app = Flask(__name__)


app.config.from_object('config')

db = SQLAlchemy(app)

# from app.views.user import mod as usersModule
from models import User,Role,Events
from forms import ExtendedConfirmRegisterForm

# flask_mail
mail = Mail(app)

# Setup Flask-Security
user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore,confirm_register_form=ExtendedConfirmRegisterForm)

from .utils import *
# login_manager.init_app(app)

# from .views import *

# from .views.user import user
# from .views.user import user
# app.register_blueprint(user)

# from .views.admin import admin
# app.register_blueprint(admin)


# from .views.events import events
# app.register_blueprint(events)




@app.route('/')
@app.route('/index')
@app.route('/home')
def home():
	return render_template('index.html')	



@app.route('/user')
@login_required
def myEvents():
    return render_template('all.html')

@app.route('/gallery')
def gallery():
	return render_template('gallery.html')


@app.route('/test')
@login_required
def test():
    return render_template('test.html',name='bogie')


@app.route('/saveProfile', methods = ['POST'])
@login_required
def saveProfile():
	current_user.first_name =request.form['first_name']
	current_user.last_name =request.form.get('last_name')
	current_user.cell =request.form.get('cell')
	# current_user.gender =request.form.get('gender')
	current_user.college =request.form.get('college')
	current_user.batch =request.form.get('batch')
	current_user.branch =request.form.get('branch')
	db.session.commit()
	flash('Details were successfully saved')
	# return redirect(url_for('.user'))
	return redirect('/user')
	# return redirect('users/all.html')







#    ALL EVENTS ROUTES
# 
# 


@app.route('/events')
def events_main():
	events = get_all_events()
	return render_template('events.html',events_list = events)




# 1954B0
@app.route('/register_event', methods=['POST'])
@login_required
def register_event():
	if (request.method == 'POST') and current_user.is_authenticated():
		event = request.form['event']
		events = get_all_events()
		if contains(events, lambda x: x.view_name == event):
			bogie = add_event_to_user(current_user.email,event)
			if bogie==True:
				flash("You are successfully registered for this event")
				return redirect("/event/%s"%(event))
			else:
				return redirect("/events")
		else:
			return redirect("/events")
	else:
		return redirect('/login')
	return render_template('test.html')


@app.route('/unreg/<event>', methods=['GET'])
@login_required
def unregx(event):
	events = get_all_events()
	check = contains(events, lambda x: x.view_name == event)
	if check is not None:
		check2 = contains(current_user.events, lambda x: x.view_name == event)
		if check2 is not None:
			bogie = unregister_to_event(current_user.email,event)
			if bogie==True:
				flash("You are successfully Unregistered for this event")
				return redirect("/event/%s"%(event))
			else:
				flash("Error Occured")
				return redirect("/event/%s"%(event))
		else:
			flash("For Unregistering, you have to register first..!! ")		
			return render_template('events/%s.html'%(event),regiterz=1,event_name=event)
	else:
		flash("Please Enter a valid Event name!!!")		
		return redirect("/events")



@app.route('/unreg', methods=['POST'])
@login_required
def unreg():
	if request.method == 'POST':
		event = request.form['event']
		events = get_all_events()
		check = contains(events, lambda x: x.view_name == event)
		if check is not None:
			check2 = contains(current_user.events, lambda x: x.view_name == event)
			if check2 is not None:
				bogie = unregister_to_event(current_user.email,event)
				if bogie==True:
					flash("You are successfully Unregistered for this event")
					return redirect("/event/%s"%(event))
				else:
					flash("Error Occured")
					return redirect("/event/%s"%(event))
			else:
				flash("For Unregistering, you have to register first..!! ")		
				return render_template('events/%s.html'%(event),regiterz=1,event_name=event)
		else:
			flash("Please Enter a valid Event name!!!")		
			return redirect("/events")
	else:
		return redirect("/events")


@app.route('/event/<event_name>')
def event(event_name):
	# check if user is registered with that 
	have = False
	events = get_all_events()
	check = contains(events, lambda x: x.view_name == event_name)
	if check is not None:
		if current_user.is_authenticated():
			check2 = contains(current_user.events, lambda x: x.view_name == event_name)
			if check2 is not None:
				return render_template('events/%s.html'%(event_name),regiterz=3,event_name=event_name)
			else:	
				return render_template('events/%s.html'%(event_name),regiterz=1,event_name=event_name)
		else:
			return render_template('events/%s.html'%(event_name),regiterz=2,event_name=event_name)
	else:
		return redirect("/events")





#    ALL ADMIN ROUTES
# 
# 
@app.route('/admin')
@roles_required('admin')
def admin_home():
	# res = get_all_organisors()
	return render_template('test.html',current_user=current_user)


@app.route('/create_organisor/', methods=['GET', 'POST'])
@roles_required('admin')
def create_organisor():
  return render_template('create_organisor.html')


@app.route('/create_admin/', methods=['GET', 'POST'])
@roles_required('admin')
def create_admin():
  return render_template('create_organisor.html')


def get_all_organisors():
	# rz = Role.query.filter_by(name='event_organisor').first().id
	# all_of_them = Role.query.filter_by(id=rz).first().users.all()
	# rz = Role.query.filter_by(name='event_organisor').first().id
	# all_of_them = Role.query.filter_by(id=rz).first().users.all()
	# uz = roles_users.query.filter(rz.id).all()
	# res = User.query.filter_by(username='alaf').all()
	return res



