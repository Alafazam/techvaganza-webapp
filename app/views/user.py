from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for
from app import db
from flask_security import Security, SQLAlchemyUserDatastore, \
    UserMixin, RoleMixin, login_required,roles_required,roles_accepted,current_user
from flask_mail import Mail
import pprint


user = Blueprint('user', __name__)

@user.route('/')
@user.route('/index')
@user.route('/home')
def home():
	return render_template('index.html')	



@user.route('/user')
@login_required
def myEvents():
    return render_template('users/all.html')


@user.route('/test')
@login_required
def test():
    print current_user
    return render_template('test.html',name='bogie')


@user.route('/saveProfile', methods = ['POST'])
@login_required
def saveProfile():
	print request.form
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
