#!/usr/bin/python3
"""The entry point of the votewave application"""

from authlib.integrations.flask_client import OAuth
from datetime import datetime, timedelta
from flask import Flask, redirect, request, Response, session, url_for
from flask_cors import CORS
from flask_login import LoginManager, login_user, login_required, logout_user
import json
from os import getenv
from urllib.parse import quote, quote_plus, urlencode
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

    token_info = oauth.auth0.authorize_access_token()
    user_info = token_info["userinfo"]
    base_url = f"http://0:{getenv('VW_CLIENT_PORT')}"

    if not (email_stat := user_info["email_verified"]):
        res_data = {
            "email_verified": email_stat,
            "access_token": token_info["access_token"],
        }
        url = f"{base_url}/login/verify/"
        return redirect(url + '?' + urlencode(res_data))

    session["user"] = token_info
    user = User.find_by_info(
        email=user_info["email"], username=user_info["nickname"])
    if user:
        # login user and send them to their dashboard
        login_user(user, remember=True,
                   duration=timedelta(weeks=2))
        session["user"]["id"] = user.id
        print("REDIRECTING TO DASHBOARD")
        return redirect(url_for("dashboard"))
    else:
        print(f"USER with email {user_info['email']} not found")
        print(user_info)
        last_name = None
        # send user to onboarding
        url = f"{base_url}/users/onboarding"
        if not user_info.get("family_name"):
            if len(user_info.get("name").split()) > 1:
                last_name = user_info["name"].split()[1]
        else:
            last_name = user_info["family_name"]
        res_data = {
            "nickname": user_info.get("nickname"),
            "first_name": user_info.get("given_name") or
                user_info.get("name").split()[0],
            "last_name": last_name,
            "email": user_info.get("email"),
        }
        print(res_data)
        return redirect(url + "?" + urlencode(res_data))


@app.route("/dashboard")
@login_required
def dashboard():
    print("dashboard url...")
    base_url = f"http://0:{getenv('VW_CLIENT_PORT')}"
    user_id = session["user"]["id"]
    print("user_id: ", user_id)
    url = f"{base_url}/users/{user_id}/dashboard"
    return redirect(url)


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

