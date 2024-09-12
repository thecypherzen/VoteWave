#!/usr/bin/python3
"""The entry point of the votewave application"""


from flask import Flask
from flask_login import UserMixin, LoginManager, login_user,\
    login_required, logout_user



app = Flask(__name__)

@app.route("/")
def index():
    """defined the index page"""
    return "This is the home page"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)

