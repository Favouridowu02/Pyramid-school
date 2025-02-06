#!/usr/bin/env python3
"""
    This Module contains the API End Points for the Admins
"""
from models.user import Admin
from flask import request, jsonify, abort
from models import storage
from api.v1.views import app_views

storage.reload()

@app_views.route('/admins', methods=["GET"], strict_slashes=False)
def all_admins() -> str:
    """ GET /api/v1/admins
    Description: Gets information of all registered admins
    Return:
      - A List of all admins Object representation, 200
    """
    all_admins = storage.all(Admin)
    all_admins_list = [admin.to_dict() for admin in all_admins]
    return jsonify(all_admins_list), 200

@app_views.route('/admins/<admin_id>', methods=["GET"], strict_slashes=False)
def one_admin(admin_id: str = None) -> str:
    """ GET /api/v1/admins/:id
    Path Parameter:
      - Admin ID
    Description: Gets information of one registered admin
    Return:
      - A JSON representation of the admin, 200
      - 404 if the admin does not exist
    """
    if admin_id is None:
        abort(404)
    admin = storage.get(Admin, admin_id)
    if admin is None:
        abort(404)
    return jsonify(admin.to_dict()), 200

@app_views.route("/admins/<admin_id>", methods=['DELETE'], strict_slashes=False)
def delete_admin(admin_id: str = None) -> str:
    """ DELETE /api/v1/admins/:id
    Path Parameter:
      - Admin ID
    Description: Deletes information of one registered admin
    Return:
      - Empty JSON id, Admin has been correctly deleted, 204
      - 404 if the Admin ID doesn't exist
    """
    if admin_id is None:
        abort(404)
    admin = storage.get(Admin, admin_id)
    if admin is None:
        abort(404)
    try:
        admin.delete()
    except Exception as e:
        abort(404)
    return jsonify({}), 204

@app_views.route("/admins", methods=["POST"], strict_slashes=False)
def create_admin():
    """ POST /api/v1/admins
    Description: Create a new Admin
    Request JSON body:
      - first_name
      - last_name
      - password
      - email
    Return:
      - JSON representation of the created admin, 201
      - 400 if any required field is missing or if there is an error
    """
    request_json = None
    error_message = None

    try:
        request_json = request.get_json()
    except Exception:
        request_json = None

    if request_json is None:
        error_message = "Wrong Format"
    else:
        if not request_json.get('first_name'):
            error_message = "First Name Missing"
        elif not request_json.get("last_name"):
            error_message = "Last Name Missing"
        elif not request_json.get("password"):
            error_message = "Password Missing"
        elif not request_json.get("email"):
            error_message = "Missing Email"
        else:
            try:
                admin = Admin()
                admin.first_name = request_json.get('first_name')
                admin.last_name = request_json.get('last_name')
                admin.email = request_json.get("email")
                admin.password = request_json.get("password")
                admin.save()
                return jsonify(admin.to_dict()), 201
            except Exception as e:
                error_message = "Can't create an Admin: {}".format(e)
    return jsonify({"error": error_message}), 404

@app_views.route('/admins/<admin_id>', methods=["PUT"], strict_slashes=False)
def update_admin(admin_id: str = None) -> str:
    """ PUT /api/v1/admin/:id
    Update an admin Data
    Request JSON body
      - first_name
      - last_name
      - password
      - email
    Return:
      - JSON representation of the created admin
      - 400 if any required field is missing or if there is an error
    """
    request_json = None
    error_message = None

    try:
        request_json = request.get_json()
    except Exception:
        request_json = None

    if request_json is None:
        error_message = "Wrong Format"
    else:
        try:
            admin = storage.get(Admin, admin_id)
            if admin is None:
                abort(404)
            admin.first_name = request_json.get('first_name', admin.first_name)
            admin.last_name = request_json.get('last_name', admin.last_name)
            admin.password = request_json.get('password', admin.password)
            admin.email = request_json.get('email', admin.email)
            admin.save()
            return jsonify(admin.to_dict()), 200
        except Exception as e:
            error_message = "Can't update Admin: {}".format(e)
    return jsonify({"error": error_message}), 400
