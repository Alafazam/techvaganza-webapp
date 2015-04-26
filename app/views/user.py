from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for
from app import db
from flask_security import Security, SQLAlchemyUserDatastore, \
    UserMixin, RoleMixin, login_required,roles_required,roles_accepted,current_user
from flask_mail import Mail
import pprint


user = Blueprint('user', __name__)

@user.route('/')
@user.route('/index')
def home():
	namez=""
	if current_user.is_authenticated(): namez = current_user.first_name
	return render_template('index.html',name=namez)	



@user.route('/myEvents')
@login_required
def myEvents():
    return render_template('myEvents.html')


@user.route('/test')
@login_required
def test():
    print current_user
    return render_template('test.html',name='bogie')
