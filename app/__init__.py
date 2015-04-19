from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.security import Security, SQLAlchemyUserDatastore, \
    UserMixin, RoleMixin, login_required,roles_required,roles_accepted
from flask_mail import Mail
from flask.ext.login import LoginManager


app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy(app)

# from app.views.user import mod as usersModule
from models import User,Role

# security = Security(app, user_datastore)

mail = Mail(app)

# Setup Flask-Security
user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore)

# login_manager = LoginManager()
# login_manager.init_app(app)

from .views.user import user
app.register_blueprint(user)

# @app.before_first_request
# def create_user():
#     db.create_all()
#     # user_datastore.create_user(email='matt@nobien.net', password='password')
#     db.session.commit()
