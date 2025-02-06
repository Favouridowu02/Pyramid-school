#!/usr/bin/env python3
"""
    This Module contains the API End Points for the Programs
"""
from models.program import Program
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
    program = storage.get(Program, program_id)
    if program is None:
        abort(404)
    return jsonify(program.to_dict()), 200

@app_views.route("/programs/<program_id>", methods=['DELETE'], strict_slashes=False)
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
      - name
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
        if not request_json.get('name'):
            error_message = "Program Name Missing"
        else:
            try:
                program = Program()
                program.name = request_json.get('name')
                program.save()
                return jsonify(program.to_dict()), 201
            except Exception as e:
                error_message = "Can't create a Program: {}".format(e)
    return jsonify({"error": error_message}), 404

@app_views.route('/programs/<program_id>', methods=["PUT"], strict_slashes=False)
def update_program(program_id: str = None) -> str:
    """ PUT /api/v1/program/:id
    Update a program Data
    Request JSON body
      - name
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
        try:
            program = storage.get(Program, program_id)
            if program is None:
                abort(404)
            program.name = request_json.get('name', program.name)
            program.save()
            return jsonify(program.to_dict()), 200
        except Exception as e:
            error_message = "Can't update Program: {}".format(e)
    return jsonify({"error": error_message}), 400