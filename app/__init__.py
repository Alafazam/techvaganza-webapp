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
from models import User,Role,Events
from forms import ExtendedConfirmRegisterForm

# flask_mail
mail = Mail(app)

# Setup Flask-Security
user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore,confirm_register_form=ExtendedConfirmRegisterForm)

# login_manager = LoginManager()
# login_manager.init_app(app)

from .views.user import user
app.register_blueprint(user)

from .views.admin import admin
app.register_blueprint(admin)


from .views.events import events
app.register_blueprint(events)


from utils import add_event_to_user







