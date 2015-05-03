from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_security import Security, SQLAlchemyUserDatastore, \
    UserMixin, RoleMixin, login_required,roles_required,roles_accepted
from flask_mail import Mail
from flask.ext.login import LoginManager
from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for
from flask_security import Security, SQLAlchemyUserDatastore, \
    UserMixin, RoleMixin, login_required,roles_required,roles_accepted,current_user


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


# login_manager = LoginManager()
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


@app.route('/test')
@login_required
def test():
    # print current_user
    return render_template('test.html',name='bogie')


@app.route('/saveProfile', methods = ['POST'])
@login_required
def saveProfile():
	# print request.form
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
	return render_template('test.html')


@app.route('/register_event/<event_name>', methods=['POST'])
@login_required
def register_event(event_name):
	# if request.method == 'POST':
        # register_to_event()
    # else:
    	# pass
		# show_the_login_form()
	return render_template('test.html')


@app.route('/unreg/', methods=['GET', 'POST'])
def unreg():
	return render_template('test.html')
 











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



