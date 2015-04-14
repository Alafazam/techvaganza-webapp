import main, test_routes
from flask import render_template
from vedge import vedge
from flask.ext.login import current_user

@vedge.errorhandler(404)
def page_not_found(e):
    return render_template('basic/404.html'), 404

@vedge.errorhandler(500)
def page_not_found(e):
    return render_template('basic/500.html'), 500