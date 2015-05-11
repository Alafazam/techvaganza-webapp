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

events_users = db.Table('events_users',
        db.Column('user_id', db.Integer(), db.ForeignKey('user.id')),
        db.Column('event_id', db.Integer(), db.ForeignKey('events.id')))


class Role(db.Model, RoleMixin):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))
    def __str__(self):
        return self.name
    def __repr__(self):
        return self.name


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username=db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    first_name = db.Column(db.String(255))
    last_name = db.Column(db.String(255))
    email = db.Column(db.String(255), unique=True)
    cell  = db.Column(db.String(255))
    gender= db.Column(db.String(6))
    college = db.Column(db.String(255))
    batch = db.Column(db.Integer(255))
    branch= db.Column(db.String(255))
    accomodation =db.Column(db.Boolean(255))
    time = db.Column(db.DateTime())
    special= db.Column(db.String(255))
    active = db.Column(db.Boolean())
    confirmed_at = db.Column(db.DateTime())
    roles = db.relationship('Role', secondary=roles_users,
            backref=db.backref('users', lazy='dynamic'))
    events = db.relationship('Events', secondary=events_users,
            backref=db.backref('users', lazy='dynamic'))
    connections = db.relationship('Connection',
            backref=db.backref('user', lazy='joined'), cascade="all")
    def __str__(self):
        return "<username :%s , first_name :%s , last_name :%s , email :%s , cell :%s , gender :%s , college :%s , batch :%s , branch :%s , accomodation :%s , time :%s , special :%s , active :%s , confirmed_at :%s , roles :%s , events:%s>"%(self.username,self.first_name,self.last_name,self.email,self.cell,self.gender,self.college,self.batch,self.branch,self.accomodation,self.time,self.special,self.active,self.confirmed_at,self.roles,self.events)
    def __repr__(self):
        return "<username :%s , first_name :%s , last_name :%s , email :%s , cell :%s , gender :%s , college :%s , batch :%s , branch :%s , accomodation :%s , time :%s , special :%s , active :%s , confirmed_at :%s , roles :%s , events:%s>"%(self.username,self.first_name,self.last_name,self.email,self.cell,self.gender,self.college,self.batch,self.branch,self.accomodation,self.time,self.special,self.active,self.confirmed_at,self.roles,self.events)

class Connection(db.Model):
    __tablename__ = "connections"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    provider_id = db.Column(db.String(255))
    email = db.Column(db.String(255), unique=True)
    provider_user_id = db.Column(db.String(255))
    access_token = db.Column(db.String(255))
    secret = db.Column(db.String(255))
    full_name=db.Column(db.String(255))
    display_name = db.Column(db.String(255))
    profile_url = db.Column(db.String(512))
    image_url = db.Column(db.String(512))
    rank = db.Column(db.Integer)      

class Events(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    event_id = db.Column(db.String(255), unique=True)
    name = db.Column(db.String(255))
    view_name=db.Column(db.String(255))
    time = db.Column(db.DateTime())
    category=db.Column(db.String(255))
    description=db.Column(db.String(255))   
    def __str__(self):
        return"<name:%s,view_name:%s>"%(self.name,self.view_name)
    def __repr__(self):
        return"<name:%s,view_name:%s>"%(self.name,self.view_name)

        # return "id :%s , event_id :%s , name :%s , view_name :%s , time :%s , category :%s , description:%s "%(self.id,self.event_id, self.name, self.view_name, self.time, self.category, self.description)
    
