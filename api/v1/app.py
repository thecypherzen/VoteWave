#!/usr/bin/python3
"""An application that manages the api"""

from flask import Flask, json, Response
from flask_cors import CORS
from api.v1.views import app_views
from models import storage
from os import getenv


# configure application
app = Flask(__name__)
app.register_blueprint(app_views)
CORS(app, resources={r"/api/v1/*": {"origins": ["*"]}})



# define routes
@app.teardown_appcontext
def close_storage(exc):
    """Closes db session on exit"""
    storage.close()


@app.errorhandler(404)
def not_found(e):
    """Handles error code 404"""
    res = json.dumps({"error": "Not Found"},
                     indent=2) + '\n'
    return Response(res, mimetype="application/json",
                    status=404)

@app.errorhandler(400)
def bad_request(e):
    """Handles bad request"""
    res = json.dumps({"error": f"{e.description}"},
                  indent=2) + '\n'
    return Response(res, mimetype="application/json",
                    status=400)


# start server
if __name__ == "__main__":
    app.run(host="0.0.0.0",
            port=getenv("VW_API_PORT") or 5000,
            threaded=True, debug=True)

