from techvaganza import app, forms, models, db
from flask import render_template, request, jsonify, redirect, url_for, session
from app.models.scenes import City, Moderator, Modnotification
from flask.ext.login import LoginManager, login_user, current_user, logout_user, login_required
from werkzeug import secure_filename
import urllib, user
from pygeocoder import Geocoder
from urllib2 import urlopen
from contextlib import closing
import json

@app.route("/")
def home():
	return render_template("basic/home.html")

@app.route("/register", methods = ['GET', 'POST'])
def register():
	if current_user.is_anonymous():	
		form = forms.sessions.UserRegisterForm()
		if request.method == "POST":
			user = models.core.User(username = form.email.data, fullname = form.fullname.data, email = form.email.data, image_location = "../static/img/default.png", password = form.password.data)
			db.session.add(user)
			db.session.commit()
			login_user(user)
			return redirect(url_for('dashboard'))
		return render_template("basic/register.html", form = form)
	else:
		return redirect(url_for('dashboard'))

@app.route("/login", methods=['GET','POST'])
def login():
	if current_user.is_anonymous():	
		form = forms.sessions.LoginForm()
		if request.method == 'POST':
			user = models.core.User.query.filter_by(email = form.email.data).first()
			if user and user.check_password(form.password.data):
				login_user(user)
				return redirect(url_for('dashboard'))
			else:
				form.email.errors.append("Invalid e-mail/username or password")
				return render_template('basic/login.html', form = form)
		elif request.method == 'GET':
			return render_template('basic/login.html', form=form)
	else:
		return redirect(url_for('dashboard'))

@app.route('/logout')
@login_required
def logout():
		logout_user()
		return redirect(url_for('login'))