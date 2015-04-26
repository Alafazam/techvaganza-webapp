from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for
from app import db
from flask.ext.security import Security, SQLAlchemyUserDatastore, \
    UserMixin, RoleMixin, login_required,roles_required,roles_accepted,current_user
from flask_mail import Mail


events = Blueprint('events', __name__)

@events.route('/events')
def events_main():
	return render_template('test.html')


@events.route('/register_event/<event_name>', methods=['POST'])
@login_required
def register_event(event_name):
	# if request.method == 'POST':
        # register_to_event()
    # else:
    	# pass
		# show_the_login_form()
	return render_template('test.html')


@events.route('/unreg/', methods=['GET', 'POST'])
def unreg():
	return render_template('test.html')
 
