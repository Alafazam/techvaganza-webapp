from flask_wtf import Form
from wtforms import StringField, SubmitField, validators, PasswordField, TextField, FileField, SelectField

class AddModerator(Form):
	email = TextField("Email", [validators.Required("Enter your email")])
	password = PasswordField("Password", [validators.Required("Enter a password")])

class UpdatePassword(Form):
	password = PasswordField("Enter your Password", [validators.Required("Enter your existing password")])
	new_password = PasswordField("Add a new Password", [validators.Required("Enter a New Password")])
	repeat_password = PasswordField("Re-enter your new Password", [validators.Required("Re-enter new password")])
		

