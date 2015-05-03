from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_security import Security, SQLAlchemyUserDatastore, \
    UserMixin, RoleMixin, login_required,roles_required,roles_accepted
from flask_mail import Mail
from flask.ext.login import LoginManager
from flask.ext.social.views import connect_handler
from flask.ext.social.utils import get_provider_or_404
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
 

#Social Routes
#
#

@app.route('/registerS/<provider_id>', methods=['GET', 'POST'])
def registerS(provider_id=None):
        
        register_user_form = RegisterForm()

        if provider_id:
                
                provider = get_provider_or_404(provider_id)
                connection_values = session.get('failed_login_connection',None)
        else:
                
                provider = None
                connection_values = None

        print connection_values
        user = user_datastore.create_user()
        db.session.commit()
        print user.id
##        db.session.commit()
        access_token=connection_values[u'access_token']
        if connection_values:
                print "hello"
                connection_values['user_id'] = user.id
                print connection_values['user_id']
                connectionE=connection_datastore.find_connection(**connection_values)
                if connectionE is None:
                        
                        connection=connection_datastore.create_connection(**connection_values)
                        if login_user(user):
                                
                                db.session.commit()
                                flash('Account created successfully', 'info')
                                api=provider.get_api()
                                print api
                                profile=api.get_object("me")
                                print profile
                                email = profile["email"]
                                user.email=email
                                user.username=email
                                user.first_name=profile["first_name"]
                                user.last_name=profile["last_name"]
                                user.gender=profile["gender"]
                                user.active=1
                                db.session.commit()
                                flash('Account created successfully', 'info')
                                return redirect(url_for('profile'))
                        
                        else:
                                
                                flash('Failed!Try Again', 'info')
                                return redirect("/register")
                        
                else:
                        
                        flash('Failed!Try Again', 'info')
                        return redirect("/register")
        else:
                flash('Connection Refused','info')
                return redirect("/register")







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



