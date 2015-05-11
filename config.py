import os
_basedir = os.path.abspath(os.path.dirname(__file__))


WTF_CSRF_ENABLED = True

SECRET_KEY = "6LeYIbsSAAAAACRPIllxA7wvXjIE411PfdB2gt2J6LeYIbsSAAAAACRPIllxA7wvXjIE411PfdB2gt2J"


# SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(_basedir, 'bogie.db')
DATABASE_CONNECT_OPTIONS = {}

#/ Production 
SQLALCHEMY_DATABASE_URI = 'mysql://techvklu:@techvaganza.org/bogie'
SQLALCHEMY_DATABASE_URI = 'mysql://root:@localhost/bogie'

THREADS_PER_PAGE = 8

CSRF_ENABLED = True
CSRF_SESSION_KEY = "somethingimpossibletoguess"

RECAPTCHA_USE_SSL = False
RECAPTCHA_PUBLIC_KEY = '6LeYIbsSAAAAACRPIllxA7wvXjIE411PfdB2gt2J'
RECAPTCHA_PRIVATE_KEY = '6LeYIbsSAAAAAJezaIq3Ft_hSTo0YtyeFG-JgRtu'
RECAPTCHA_OPTIONS = {'theme': 'white'}


MAIL_SERVER = 'localhost'
MAIL_PORT = 1125
# 


# MAil server seeting to be changed for MAIL GUN API
# MAIL_SERVER = 'smtp.mailgun.org'
# MAIL_PORT = 587
# MAIL_USE_SSL = True
# MAIL_USERNAME = 'postmaster@sandboxa729357f36b64ad994722adc22aa84d4.mailgun.org'
# MAIL_PASSWORD = 'b22d5961ef11557fd7b4f77391911136'



SECURITY_PASSWORD_HASH = 'pbkdf2_sha512'
SECURITY_PASSWORD_SALT ='f1a4xxd4W!pef'
SECURITY_EMAIL_SENDER = 'noreply@techvaganza.org'
SECURITY_CONFIRMABLE =  True 
SECURITY_RECOVERABLE =  True
SECURITY_REGISTERABLE =  True
SECURITY_CHANGEABLE =  True
SECURITY_POST_CONFIRM_VIEW='user'
SECURITY_POST_LOGIN_VIEW='user'
