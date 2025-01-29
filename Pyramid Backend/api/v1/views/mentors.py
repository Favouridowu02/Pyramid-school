#!/usr/bin/env python3
"""
    This Module contains the API End Points for the Mentors
"""
from models.user import Mentor
from flask import request, jsonify, abort
from models import storage
from api.v1.views import app_views


storage.reload()

@app_views.route('/mentors', methods=["GET"], strict_slashes=False)
def all_mentors() -> str:
    """ GET /api/v1/mentors
    Description: Gets information of all registered mentors
    Return:
      - A List of all mentors Object representation, 200
    """
    all_mentors = storage.all(Mentor)
    all_mentors_list = [mentor.to_dict() for mentor in all_mentors]
    print("\n\n", all_mentors_list, "\n\n")
    return jsonify(all_mentors_list), 200

@app_views.route('/mentors/<mentor_id>', methods=["GET"], strict_slashes=False)
def one_mentor(mentor_id: str = None) -> str:
  """ GET /api/v1/mentors/:id
  Path Parameter:
    - Mentor ID
  Description: Gets information of one registered mentor
  Return:
    - A JSON representation of the mentor, 200
    - 404 if the mentor does not exist
  """
  if mentor_id is None:
    abort(404)
  if mentor_id == "me":
    if request.current_user is None:
      abort(404)
    else:
      return jsonify(request.current_user.to_dict()), 200
  mentor = storage.get(Mentor, mentor_id)
  if mentor is None:
    abort(404)
  return jsonify(mentor.to_dict()), 200


@app_views.route("/mentors/<mentor_id>", methods=['DELETE'],
                 strict_slashes=False)
def delete_mentor(mentor_id: str = None) -> str:
  """ DELETE /api/v1/mentors/:id
  Path Parameter:
    - Mentor ID
  Description: Deletes information of one registered mentor
  Return:
    - Empty JSON id, Mentor has been correctly deleted, 204
    - 404 if the Mentor ID doesn't exist
  """
  if mentor_id is None:
    abort(404)
  mentor = storage.get(Mentor, mentor_id)
  if mentor is None:
    abort(404)
  try:
    mentor.delete()
  except Exception as e:
    abort(404)
  return jsonify({}), 204


@app_views.route("/mentors", methods=["POST"], strict_slashes=False)
def create_mentor():
  """ POST /api/v1/mentors
  Description: Create a new Mentor
  Request JSON body:
    - first_name
    - last_name
    - user_name
    - password
    - email
    - xp
  Return:
    - JSON representation of the created mentor, 201
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
        mentor = Mentor()
        mentor.first_name = request_json.get('first_name')
        mentor.last_name = request_json.get('last_name')
        mentor.email = request_json.get("email")
        mentor.password = request_json.get("password")
        mentor.save()
        return jsonify(mentor.to_dict()), 201
      except Exception as e:
        error_message = "Can't create a Mentor: {}".format(e)
  return jsonify({"error": error_message}), 404


@app_views.route('/mentors/<mentor_id>', methods=["PUT"], strict_slashes=False)
def update_mentor(mentor_id: str = None) -> str:
  """ PUT /api/v1/mentor/:id
  Update a mentor Data
  Request JSON body
    - first_name
    - last_name
    - user_name
    - password
    - email
    - xp
  Return:
    - JSON representation of the created mentor
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
      mentor = storage.get(Mentor, mentor_id)
      if mentor is None:
        abort(404)
      first_name = request_json.get('first_name',
                                    mentor.first_name)
      last_name = request_json.get('last_name',
                                    mentor.last_name)
      mentor.first_name = first_name
      mentor.last_name = last_name
      mentor.password = request_json.get('password', mentor.password)
      mentor.email = request_json.get('email', mentor.email)

      mentor.save()
      return jsonify(mentor.to_dict()), 200
    except Exception as e:
        error_message = "Can't update Mentor: {}".format(e)
  return jsonify({"error": error_message}), 400