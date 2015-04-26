from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for
from app import db
from flask.ext.security import Security, SQLAlchemyUserDatastore, \
    UserMixin, RoleMixin, login_required,roles_required,roles_accepted,current_user
from flask_mail import Mail
from ..models import User,Role,roles_users
from ..utils import add_event_to_user,get_role,get_event

admin = Blueprint('admin', __name__)

@admin.route('/admin')
@roles_required('admin')
def admin_home():
	# res = get_all_organisors()
	return render_template('test.html',current_user=current_user)


@admin.route('/create_organisor/', methods=['GET', 'POST'])
@roles_required('admin')
def create_organisor():
  return render_template('create_organisor.html')


@admin.route('/create_admin/', methods=['GET', 'POST'])
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
