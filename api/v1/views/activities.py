#!/usr/bin/python3
"""Defines the Activites view """

from api.v1.views import app_views
from flask import json, abort, Response
from models import storage
from models.base_activity import Activity


@app_views.route("/activities", strict_slashes=False)
def activities():
    """Fetches all activites that are public"""
    session = storage.session()
    all_activities = session.query(Activity).filter_by(is_public=True).all()
    activities = [activity.to_dict()
                  for activity in all_activities]
    res = json.dumps(activities, indent=2) + '\n'
    session.close()
    return Response(res, mimetype="application/json")

