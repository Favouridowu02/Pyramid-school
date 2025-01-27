#!/usr/bin/env python3
"""
    This Module contains the API End Points for the Programs
"""
from models.user import Program
from flask import request, jsonify, abort
from models import storage
from api.v1.views import app_views


storage.reload()

@app_views.route('/programs', methods=["GET"], strict_slashes=False)
def all_programs() -> str:
    """ GET /api/v1/programs
    Description: Gets information of all registered programs
    Return:
      - A List of all programs Object representation, 200
    """
    all_programs = storage.all(Program)
    all_programs_list = [program.to_dict() for program in all_programs]
    print("\n\n", all_programs_list, "\n\n")
    return jsonify(all_programs_list), 200

@app_views.route('/programs/<program_id>', methods=["GET"], strict_slashes=False)
def one_program(program_id: str = None) -> str:
  """ GET /api/v1/programs/:id
  Path Parameter:
    - Program ID
  Description: Gets information of one registered program
  Return:
    - A JSON representation of the program, 200
    - 404 if the program does not exist
  """
  if program_id is None:
    abort(404)
  if program_id == "me":
    if request.current_user is None:
      abort(404)
    else:
      return jsonify(request.current_user.to_dict()), 200
  program = storage.get(Program, program_id)
  if program is None:
    abort(404)
  return jsonify(program.to_dict()), 200


@app_views.route("/programs/<program_id>", methods=['DELETE'],
                 strict_slashes=False)
def delete_program(program_id: str = None) -> str:
  """ DELETE /api/v1/programs/:id
  Path Parameter:
    - Program ID
  Description: Deletes information of one registered program
  Return:
    - Empty JSON id, Program has been correctly deleted, 204
    - 404 if the Program ID doesn't exist
  """
  if program_id is None:
    abort(404)
  program = storage.get(Program, program_id)
  if program is None:
    abort(404)
  try:
    program.delete()
  except Exception as e:
    abort(404)
  return jsonify({}), 204


@app_views.route("/programs", methods=["POST"], strict_slashes=False)
def create_program():
  """ POST /api/v1/programs
  Description: Create a new Program
  Request JSON body:
    - first_name
    - last_name
    - user_name
    - password
    - email
    - xp
  Return:
    - JSON representation of the created program, 201
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
    elif not request_json.get("user_name"):
      error_message = "User Name missing"
    elif not request_json.get("password"):
      error_message = "Password Missing"
    elif not request_json.get("email"):
      error_message = "Missing Email"
    else:
      try:
        program = Program()
        program.first_name = request_json.get('first_name')
        program.last_name = request_json.get('last_name')
        program.email = request_json.get("email")
        program.user_name = request_json.get("user_name")
        program.password = request_json.get("password")
        program.save()
        return jsonify(program.to_dict()), 201
      except Exception as e:
        error_message = "Can't create a Program: {}".format(e)
  return jsonify({"error": error_message}), 404


@app_views.route('/programs/<program_id>', methods=["PUT"], strict_slashes=False)
def update_program(patient_id: str = None) -> str:
  """ PUT /api/v1/program/:id
  Update a program Data
  Request JSON body
    - first_name
    - last_name
    - user_name
    - password
    - email
    - xp
  Return:
    - JSON representation of the created program
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
    program = storage.get(Program, program_id)
    if program is None:
      abort(404)
    first_name = request_json.get('first_name',
                                  program.first_name)
    last_name = request_json.get('last_name',
                                  program.last_name)
    program.first_name = first_name
    program.last_name = last_name
    program.user_name = request_json.get('user_name', program.user_name)
    program.password = request_json.get('password', program.password)
    program.email = request_json.get('email', program.email)

    program.save()
    return jsonify(program.to_dict()), 200
  except Exception as e:
      error_message = "Can't update Program: {}".format(e)
return jsonify({"error": error_message}), 400