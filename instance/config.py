from techvaganza import app
import os, flask.ext.whooshalchemy

CSRF_ENABLED = True
SECRET_KEY = "BULLsh*t"
MASTER_EMAIL = ["mail@arsalanbashir.com"]

basedir = os.path.abspath(os.path.dirname(__file__))
BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

if os.environ.get('DATABASE_URL') is None:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
    app.config['WHOOSH_BASE'] = os.path.join(basedir, 'search-index')
else:
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']

SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')