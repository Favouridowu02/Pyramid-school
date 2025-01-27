#!/usr/bin/python3
"""
    This module sets up the Flask application for the Pyramid Backend API.
    It configures the application, initializes the database, and registers
    the necessary routes and blueprints for the API endpoints.
"""
from dotenv import load_dotenv
from api.v1.views import app_views
from flask import Flask, jsonify, abort, request
from flask_cors import (CORS, cross_origin)
from os import getenv

app = Flask(__name__)
app.register_blueprint(app_views)
CORS(app, resources={r'/api/v1/*': {'origins': "*"}})

auth = None
if getenv('AUTH_TYPE') == "basic_auth":
    from api.v1.auth.basic_auth import BasicAuth

    auth = BasicAuth()
elif getenv('AUTH_TYPE') == "session_auth":
    from api.v1.auth.session_auth import SessionAuth

    auth = SessionAuth()
elif getenv('AUTH_TYPE') == "session_exp_auth":
    from api.v1.auth.session_exp_auth import SessionExpAuth

    auth = SessionExpAuth()
elif getenv('AUTH_TYPE'):
    from api.v1.auth.auth import Auth

    auth = Auth()


@app.errorhandler(404)
def not_found(error) -> str:
    """ Not found handler
    """
    return jsonify({"error": "Not found"}), 404


@app.before_request
def before_request() -> str:
    """ This Method is ran Before request
    """
    if auth is None:
        return
    paths = ['/api/v1/status/', '/api/v1/unauthorized/',
             '/api/v1/forbidden/', '/api/v1/auth_session/login/']
    if not auth.require_auth(request.path, paths):
        return
    if auth.authorization_header(request) is None and \
            auth.session_cookie(request) is None:
        abort(401)
    if auth.current_user(request) is None:
        abort(403)
    request.current_user = auth.current_user(request)

@app.errorhandler(404)
def not_found(errorhandler) -> str:
    """ Not found handler
    """
    return jsonify({"error": "Not found"}), 404


@app.errorhandler(403)
def forbidden(error) -> str:
    """ Forbidden Handler
    """
    return jsonify({"error": "Forbidden"}), 403


if __name__ == "__main__":
    """ This is used to run the api
    """
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", "5000")
    app.run(host=host, port=port, debug=True)