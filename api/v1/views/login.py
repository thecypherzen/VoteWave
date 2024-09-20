from models import storage
from models.users import User
from api.v1.views import app_views
from flask import redirect, request, json, Response
from os import getenv
import requests



@app_views.route("/login", strict_slashes=False)
def login():
    """login user"""
    print("loging user in....")
    return redirect(
        "http://0:{}/login".\
            format(getenv('VW_SERVER_PORT')))


@app_views.route("/login/verify-email", methods=["POST"])
def verify_user_email():
    """Handle Email verification"""
    auth_header = request.headers.get("Authorization")
    if not auth_header:
        res_data = {"error": "Missing Authorization headers"}
        res = json.dumps(res_data, indent=2) + '\n'
        return Response(res, mimetype="application/json", status=401)
    access_token = auth_header.split()[1]
    url = f"https://{getenv('AUTH0_DOMAIN')}/userinfo"
    headers = {"Authorization": f"Bearer {access_token}"}
    res = requests.get(url, headers=headers)

    if res.status_code != 200:
        return Response(json.dumps(
            {"error": "Couldn't get user info"}, indent=2) + '\n',
            mimetype="application/json", status=401)

    user_info = res.json()
    email_status = user_info["email_verified"]
    res  = json.dumps({"email_verified": email_status}, indent=2) + '\n'
    return Response(res, mimetype="application/json", status=200)