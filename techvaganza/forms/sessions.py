from flask_wtf import Form
from wtforms import StringField, SubmitField, validators, PasswordField, TextField, FileField

class UserRegisterForm(Form):
	fullname = StringField('First name', validators=[validators.DataRequired('Name is required')])
	email = TextField("Email", [validators.Required("Enter your email")])
	password = PasswordField("Password", [validators.Required("Enter a password")])

class LoginForm(Form):
	email = TextField("Email", [validators.Required("Enter your email")])
	password = PasswordField("Password", [validators.Required("Enter a password")])