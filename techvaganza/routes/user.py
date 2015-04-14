from techvaganza import app, forms, models, db
from techvaganza.models.core import User
from techvaganza.models.scenes import City, Moderator, Modnotification
import urllib, os, datetime, random
from werkzeug import secure_filename
from flask_user import current_user, login_required
from pygeocoder import Geocoder
from flask.ext.googlemaps import Map
from flask import render_template, request, jsonify, redirect, url_for, session

@login_required
@app.route("/dashboard", methods=['GET','POST'])
def dashboard():
	dishes = Dish.query.all()
	favdish = random.choice(dishes)
	return render_template("basic/dashboard.html", message = current_user.email, user = current_user, favdish = favdish)

@login_required
@app.route("/edit", methods=['GET','POST'])
def edit_profile():
	form = forms.superadmin.UpdatePassword()
	if request.method == "POST":
		user = current_user
		if user.check_password(form.password.data) and form.new_password.data == form.repeat_password.data:
			user.set_password(form.new_password.data + user.salt)
			db.session.commit()
			return render_template("admin/edit.html", form = form, user = current_user, note = "Successfully Changed Password!")
		else:
			return render_template("admin/edit.html", form = form, user = current_user, note = "Check the details and try again!")
	return render_template("admin/edit.html", form = form, user = current_user)

@login_required
@app.route('/removemoderator', methods=['GET', 'POST'])
def remove_moderator():
	city_name = request.args.get('cityname', '0')
	email = request.args.get('email', '0')

	city = City.query.filter_by(name = city_name).first()
	mod = Moderator.query.filter_by(email = email).first()
	
	db.session.delete(mod)
	db.session.commit()

	return jsonify(string = "200 OK")

@app.route("/notifications", methods=["GET"])
def notifications():
	if current_user.user_status == 1:
		my_mod = Moderator.query.filter_by(email = current_user.email).all()
		notifs = []

		for mod in my_mod:
			n = Modnotification.query.filter_by(moderator = mod).all()
			for i in n:
				notifs.append(i)
				i.read = True

		db.session.commit()

		return render_template("admin/admin.html", current_user = current_user, user = current_user, notifications = notifs)
	else:
		return redirect('home')

def clean_name(name):
	t = name.lower().strip()
	return t.replace (" ", "_")

