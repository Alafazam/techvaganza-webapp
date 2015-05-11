import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_security import Security, SQLAlchemyUserDatastore, \
    UserMixin, RoleMixin, login_required,roles_required,roles_accepted
from flask_mail import Mail

from flask.ext.login import LoginManager
from flask.ext.social.views import connect_handler
from flask.ext.social import Social, SQLAlchemyConnectionDatastore, \
     login_failed
from flask.ext.social.datastore import SQLAlchemyConnectionDatastore
from flask.ext.social.utils import get_provider_or_404,get_connection_values_from_oauth_response
from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for
from flask_security import Security, SQLAlchemyUserDatastore, \
    UserMixin, RoleMixin, login_required,login_user,roles_required,roles_accepted,current_user
from flask import Flask, request, redirect, url_for



app = Flask(__name__)



app.config.from_object('config')
app.config['SOCIAL_FACEBOOK'] = {
    'consumer_key': '1484405811783447',
    'consumer_secret': 'ee8930d2e57550ceaf12b04b158c38d1'
}

db = SQLAlchemy(app)

# from app.views.user import mod as usersModule
from models import User,Role,Events,Connection
from forms import ExtendedConfirmRegisterForm

# flask_mail
mail = Mail(app)

# Setup Flask-Security
user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore,confirm_register_form=ExtendedConfirmRegisterForm)
connection_datastore = SQLAlchemyConnectionDatastore(db, Connection)
social= Social(app, connection_datastore)

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
    return render_template('all.html',facebook_conn=social.facebook.get_connection())

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

 

#Social Routes
#
#

@app.route('/registerS/<provider_id>', methods=['GET', 'POST'])
def registerS(provider_id=None):
        
##        register_user_form = RegisterForm()

        if provider_id:
                
                provider = get_provider_or_404(provider_id)
                connection_values = session.get('failed_login_connection',None)
        else:
                
                provider = None
                connection_values = None

        print connection_values

                
        

##        print user.id
##        db.session.commit()
##        access_token=connection_values[u'access_token']
        if connection_values:
                
                email=connection_values[u'email']
##                print email
                user=user_datastore.find_user(email=email)
                if(user):
                        
                        connectionE=connection_datastore.find_connection(**connection_values)
                        if connectionE is None:
                                connection_values['user_id'] = user.id
                                connection=connection_datastore.create_connection(**connection_values)
                                if login_user(user):
                                        db.session.commit()
                                        flash('Facebook account linked successfully with existing id', 'info')
                                        return redirect('/user')
                                else:
                                        flash('Failed to link with Facebook!Try Again', 'info')
                                        return redirect('/user')
                                        
                        else:
                                if login_user(user):
##                                        flash(' Facebook Already linked', 'info')
                                        return redirect('/user')
                                
                                
                else:
                        
##                        print "hello"
                        user = user_datastore.create_user()
                        db.session.commit()
                        connection_values['user_id'] = user.id
##                        print connection_values['user_id']
                        connectionE=connection_datastore.find_connection(**connection_values)

                        if connectionE is None:
                                
                                connection=connection_datastore.create_connection(**connection_values)
                                if login_user(user):
                                        
                                        db.session.commit()
                                        flash('Account created successfully', 'info')
                                        api=provider.get_api()
##                                        print api
                                        profile=api.get_object("me")
##                                        print profile
                                        email = profile["email"]
                                        
                                        user.email=email
                                        user.username=email
                                        user.first_name=profile["first_name"]
                                        user.last_name=profile["last_name"]
                                        user.gender=profile["gender"]
                                        user.active=1
                                        db.session.commit()
        ##                                flash('Account created successfully', 'info')
                                        return redirect('/user')
                                
                                else:
                                        
                                        flash('Failed!Try Again', 'info')
                                        return redirect("/register")
                                
                        else:
                                
                                flash('Failed!Try Again', 'info')
                                return redirect("/register")
                
        else:
                        
                flash('Connection Refused','info')
                return redirect("/register")


class SocialLoginError(Exception):
    def __init__(self, provider):
        self.provider = provider


@app.before_first_request
def before_first_request():
    try:
        models.db.create_all()
    except Exception, e:
        app.logger.error(str(e))

@login_failed.connect_via(app)
def on_login_failed(sender, provider, oauth_response):
    app.logger.debug('Social Login Failed via %s; '
                     '&oauth_response=%s' % (provider.name, oauth_response))

    # Save the oauth response in the session so we can make the connection
    # later after the user possibly registers
    session['failed_login_connection'] = \
        get_connection_values_from_oauth_response(provider, oauth_response)

    raise SocialLoginError(provider)


@app.errorhandler(SocialLoginError)
def social_login_error(error):
    return redirect(
        url_for('registerS', provider_id=error.provider.id, login_failed=1))





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



