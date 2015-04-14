from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager
from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand
from flask.ext import assets
from flask_mail import Mail
import os

app = Flask(__name__, instance_relative_config=True)
app.config.from_pyfile('config.py')

db = SQLAlchemy(app)
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

login_manager = LoginManager()
login_manager.init_app(app)

env = assets.Environment(app)
env.load_path = [
    os.path.join(os.path.dirname(__file__), 'sass'),
    os.path.join(os.path.dirname(__file__), 'coffee'),
    os.path.join(os.path.dirname(__file__), 'bower_components'),
]

env.register(
    'js_all',
    assets.Bundle(
        'jquery/dist/jquery.min.js',
        'bootstrap-sass-official/assets/javascripts/bootstrap.min.js',
        'jquery-ui/jquery-ui.min.js',
        assets.Bundle(
            'main.coffee',
            filters=['coffeescript']
        ),
        output='js_all.js'
    )
)

env.register(
    'css_all',
    assets.Bundle(
        '_style.sass',
        filters='sass',
        output='css_all.css'
    )
)

env.versions = 'timestamp'

from techvaganza import methods, routes, models