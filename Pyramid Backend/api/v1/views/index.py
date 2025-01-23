#!/usr/bin/env python3
"""
    This module defines the basic routes for the Pyramid Backend API.
    It includes endpoints for checking the status of the API and handling
    unauthorized access.
"""
from flask import jsonify, abort
from api.v1.views import app_views


@app_views.route("/status", methods=["GET"], strict_slashes=False)
def status() -> str:
    """ GET /api/v1/status
    Return:
      - the status of the API
    """
    return jsonify({"status": "OK"})


@app_views.route('/unauthorized', strict_slashes=False)
def unauthorized():
    """ GET /api/v1/unauthorised
    Return:
        - Abort unauthorised
    """
    abort(401)


@app_views.route("/forbidden", strict_slashes=False)
def forbidden():
    """ GET /api/v1/forbidden
    Return:
      - Abort Forbidden
    """
    abort(403)