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

    # get user's extra information
    user_dict = user.to_dict()

    own_activities = user.polls + user.elections
    user_dict["own_activites"] = [act.to_dict() for act in own_activities]
    user_dict["admin_of"] = [
        ad.to_dict() for ad in user.admin_of]
    user_dict["ivs_sent"] = [
        iv.to_dict() for iv in user.ivs_sent]
    user_dict["ivs_in"] = [
        iv.to_dict() for iv in user.ivs_received]
    user_dict["reviews"] = [rv.to_dict() for rv in user.reviews]
    user_dict["waitlists"] = [
        wl.to_dict() for wl in user.waitlists]
    user_dict["meta_data"] = [
        md.to_dict() for md in user._metadata]
    res = json.dumps(user_dict, indent=2) + '\n'
    return Response(res, mimetype="application/json")
