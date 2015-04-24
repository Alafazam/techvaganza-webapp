from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_security import Security, SQLAlchemyUserDatastore, \
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
# db.create_all()

# @app.before_first_request
# def create_role():
#     db.create_all()
#     user_datastore.create_role(name='event_organisor', description='Event Organisors')
#     db.session.commit()


from .views.admin import admin
app.register_blueprint(admin)


from .views.events import events
app.register_blueprint(events)


# user_datastore.create_role(name='User',description='Casual')
# alaf = user_datastore.find_user(email='alaf@gmail.com')
# ankit = user_datastore.find_user(email='ankitstarski@gmail.com')
# dino = user_datastore.find_user(email='sonugauti@hotmail.com')
# user_datastore.add_role_to_user(dino,'event_organisor')
# db.session.commit()


