from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for
from app import db
from flask.ext.security import Security, SQLAlchemyUserDatastore, \
    UserMixin, RoleMixin, login_required,roles_required,roles_accepted
from flask_mail import Mail


admin = Blueprint('admin', __name__)

@admin.route('/admin')
@roles_required('admin')
def admin_home():
    return render_template('index.html')


@admin.route('/create_organisor/', methods=['GET', 'POST'])
@roles_required('admin')
def create_organisor():
  return render_template('create_organisor.html')
