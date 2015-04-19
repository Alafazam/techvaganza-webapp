import os
_basedir = os.path.abspath(os.path.dirname(__file__))


WTF_CSRF_ENABLED = True

SECRET_KEY = "6LeYIbsSAAAAACRPIllxA7wvXjIE411PfdB2gt2J6LeYIbsSAAAAACRPIllxA7wvXjIE411PfdB2gt2J"


# SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(_basedir, 'app.db')
SQLALCHEMY_DATABASE_URI = 'mysql://root:@localhost/bogie'
DATABASE_CONNECT_OPTIONS = {}

THREADS_PER_PAGE = 8

CSRF_ENABLED = True
CSRF_SESSION_KEY = "somethingimpossibletoguess"

RECAPTCHA_USE_SSL = False
RECAPTCHA_PUBLIC_KEY = '6LeYIbsSAAAAACRPIllxA7wvXjIE411PfdB2gt2J'
RECAPTCHA_PRIVATE_KEY = '6LeYIbsSAAAAAJezaIq3Ft_hSTo0YtyeFG-JgRtu'
RECAPTCHA_OPTIONS = {'theme': 'white'}

MAIL_SERVER = 'localhost'
MAIL_PORT = 1125
# MAIL_USE_SSL = True
# MAIL_USERNAME = 'username'
# MAIL_PASSWORD = 'password'


SECURITY_PASSWORD_HASH = 'pbkdf2_sha512'
SECURITY_PASSWORD_SALT ='f1a4xxd4W!pef'
SECURITY_EMAIL_SENDER = 'noreply@localhost'
SECURITY_CONFIRMABLE =  True 
SECURITY_RECOVERABLE =  True
SECURITY_REGISTERABLE =  True
SECURITY_CHANGEABLE =  True

