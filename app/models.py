# import app
from app import db
from flask.ext.security import Security, SQLAlchemyUserDatastore, \
    UserMixin, RoleMixin, login_required,roles_required,roles_accepted
from flask_mail import Mail
from wtforms import Form, BooleanField, TextField, PasswordField, validators


# Define models
roles_users = db.Table('roles_users',
        db.Column('user_id', db.Integer(), db.ForeignKey('user.id')),
        db.Column('role_id', db.Integer(), db.ForeignKey('role.id')))

class Role(db.Model, RoleMixin):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    active = db.Column(db.Boolean())
    first_name = db.Column(db.String(255))
    last_name = db.Column(db.String(255))
    college_name = db.Column(db.String(255))
    cell  = db.Column(db.String(255))
    gender= db.Column(db.String(6))
    batch = db.Column(db.String(255))
    accomodation =db.Column(db.Boolean(255))
    confirmed_at = db.Column(db.DateTime())
    roles = db.relationship('Role', secondary=roles_users,
                            backref=db.backref('users', lazy='dynamic'))

