#!/usr/bin/python3
"""Defines the users view """

from api.v1.views import app_views
from flask import json, abort, Response
from models import storage
from models.users import User


@app_views.route("/users/<string:user_id>", strict_slashes=False)
def user_details(user_id):
    """Returns details of a user by Id if
    found else 404
    """
    session = storage.session()
    user = session.query(User).filter_by(id=user_id).first()
    if not user:
        abort(404)
    res = json.dumps(user.to_dict(), indent=2) + '\n'
    return Response(res, mimetype="application/json")
