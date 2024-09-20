#!/usr/bin/python3
"""The entry point of the votewave application"""

from authlib.integrations.flask_client import OAuth
from flask import Flask, redirect, request, url_for, session
from flask_cors import CORS
from flask_login import LoginManager, login_user, login_required, logout_user
import json
from os import getenv
from urllib.parse import quote_plus, urlencode
import requests

from models.users import User

app = Flask(__name__)
CORS(app, supports_credentials=True,
     resources={r"/*":
                {"origins": "*"}})
app.secret_key = getenv("VW_APP_SECRET")
client_base = getenv("VW_CLIENT")

# configure oauth and register application
oauth = OAuth(app)
oauth.register(
    "auth0",
    client_id=getenv("AUTH0_CLIENT_ID"),
    client_secret=getenv("AUTH0_CLIENT_SECRET"),
    client_kwargs={
        "scope": "openid profile email",
    },
    server_metadata_url=\
        f"https://{getenv('AUTH0_DOMAIN')}/.well-known/openid-configuration"
)

login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def fetch_user(user_id):
    return User.get(user_id)

@app.route("/", strict_slashes=False)
def index():
    """defined the index page"""
    return redirect(f"http://{getenv('VW_TEST_HOST')}:{getenv('VW_CLIENT_PORT')}")


@app.route("/login", strict_slashes=False)
def login():
    """handles logins"""
    print("logging in...\n")
    return oauth.auth0.authorize_redirect(
        redirect_uri=url_for("callback", _external=True))


@app.route("/callback", methods=["GET", "POST"],
           strict_slashes=False)
def callback():
    """handles response after authentication"""
    print("verifying user...\n")
    token = oauth.auth0.authorize_access_token()
    user_info = token["userinfo"]
    session["user"] = token
    print(user_info)
    return redirect(url_for("dashboard"))


@app.route("/dashboard")
#@login_required
def dashboard():
    user = session['user']['userinfo']['name']

    return f"<p>User {user if user else 'SOME USER'}'s dashboard </p><br/><a href='{url_for('logout')}'>Logout</a>"


@app.route("/logout")
def logout():
    """Logs a user out"""
    print("logging out .....\n")
    session.clear()
    print("session cleared....\n")
    print(session.get("user"))
    return redirect(
        "https://" + getenv("AUTH0_DOMAIN")
        + "/v2/logout?"
        + urlencode(
            {
                "returnTo": url_for("index", _external=True),
                "client_id": getenv("AUTH0_CLIENT_ID"),
            },
            quote_via=quote_plus,
        )
    )



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001,
    debug=True, threaded=True)

