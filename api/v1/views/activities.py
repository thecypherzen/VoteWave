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
    for act in all_activities:
        act.set_live_end()

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
def activity_details(activity_id):
    """Returns the details of an activity by id
    if the activity is public
    """
    session = storage.session()
    # get activity
    first = session.query(Activity)\
        .filter_by(id=activity_id).first()
    if not first:
        abort(404)
    type = first.type.capitalize()

    # get activity details
    activity = storage.get(type, activity_id)
    if not activity:
        abort(404)
    act_dict = activity.to_dict()
    act_dict["blacklist"] = [
        usr.to_dict() for usr in activity.blacklist_entries]
    act_dict["meta_data"] = [
        md.to_dict() for md in activity._metadata]
    act_dict["chatroom_id"] = activity.chatroom.id \
        if activity.chatroom else None
    res = ["admins", "candidates", "invitations",
           "notices", "redflags", "reviews",
           "voters"]
    for ri in res:
        if hasattr(activity, ri):
            act_dict[ri] = [
                  val.id for val in
                      getattr(activity, ri)]

    act_dict["sent_messages"] = [
        msg.id for msg in activity.sent_messages] \
        if activity.sent_messages else []

    act_dict["received_messages"] = [
        msg.id for msg in activity.received_messages] \
        if activity.received_messages else []

    res = json.dumps(act_dict, indent=2) + '\n'
    session.close()
    return Response(res, mimetype="application/json")