from models import storage
from models.users import User
from api.v1.views import app_views
from flask import redirect
from os import getenv



@app_views.route("/login", strict_slashes=False)
def login():
	"""login user"""
	print("loging user in....")
	return redirect(
		"http://0:{}/login".\
			format(getenv('VW_SERVER_PORT')))


