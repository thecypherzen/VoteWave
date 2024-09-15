#!/usr/bin/python3
"""Defines the Activites view """

from api.v1.views import app_views
from flask import json, abort, Response
from models import storage
from models.base_activity import Activity
from models.elections import Election
from models.polls import Poll

models = {"Activity": Activity, "Election": Election,
          "Poll": Poll}

@app_views.route("/activities", strict_slashes=False)
def all_activities():
    """Fetches all activites that are public"""
    session = storage.session()
    all_activities = session.query(Poll).filter_by(is_public=True).all() + \
        session.query(Election)\
            .filter_by(is_public=True).all()
    activities = [activity.to_dict()
                  for activity in all_activities]
    res = json.dumps(activities, indent=2) + '\n'
    session.close()
    return Response(res, mimetype="application/json")

@app_views.route(
        "/activities/live", strict_slashes=False)
def live_activities():
    """Returns all live activities that are public"""
    data = all_activities().get_json()
    live = [item for item in data
            if item["status"] == "live"]
    res = json.dumps(live, indent=2) + '\n'
    return Response(res, mimetype="application/json")

@app_views.route("/activities/<string:activity_id>")
def activity_detail(activity_id):
    """Returns the details of an activity by id
    if the activity is public
    """
    print("CALLED.....")
    session = storage.session()
    first = session.query(Activity)\
        .filter_by(id=activity_id).first()
    if not first:
        abort(404)
    type = first.type.capitalize()
    activity = storage.get(type, activity_id)
    if not activity:
        abort(404)
    print("GOT HERE .....")
    res = json.dumps(activity.to_dict(), indent=2) + '\n'
    return Response(res, mimetype="application/json")