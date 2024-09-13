#!/usr/bin/python3
"""An application that manages the api"""

from flask import Flask, json, Response
from flask_cors import CORS
from api.v1.views import app_views
from models import storage
from os import env


# configure application
app = Flask(__name__)
app.register_bluprint(app_views)
CORS(app, resources={r"/api/v1/*": {"origins": ["*"]}})



# define routes
@app.teardown_appcontext
def close_storage(exc):
    """Closes db session on exit"""
    storage.close()

@app.errorhandler(400)
def not_found(e):
    """Handles error code 400"""
    res = json.dumps({"error": "Not Found"},
                     indent=2) + '\n'
    return Response(res, mime_type="application/json",
                    status=400)


# start server
if __name__ == "__main__":
    app.run(host=env("VW_TEST_HOST" or "0.0.0.0"),
            port=env("VW_API_PORT" or 5000),
            threaded=True)

