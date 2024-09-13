#!/usr/bin/python3
"""The entry point of the votewave application"""

from authlib.integrations.flask_client import OAuth
from flask import Flask, redirect, url_for, session
from flask_cors import CORS
from flask_login import LoginManager, login_user, login_required,\
    logout_user
import json
from os import getenv
from urllib.parse import quote_plus, urlencode
import requests


app = Flask(__name__)
CORS(app, supports_credentials=True)
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


@app.route("/")
def index():
    """defined the index page"""
    return redirect(f"http://{getenv('VW_TEST_HOST')}:{getenv('VW_CLIENT_PORT')}")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)

