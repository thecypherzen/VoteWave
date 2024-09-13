#!/usr/bin/python3
"""Defines the index view of our api"""

from api.v1.views import app_views
from flask import json, Response




@app_views.route("/status", strict_slashes=False)
def status():
    """Returns a status OK"""
    res = json.dumps({"status": "OK"}, indent=2) + '\n'
    return Response(res, mime_type="application/json")
