#!/usr/bin/env python3
"""
    This Module contains the API End Points for the Student Projects
"""
from models.student_projects import StudentProject
from flask import request, jsonify, abort
from models import storage
from api.v1.views import app_views

storage.reload()

@app_views.route('/student_projects', methods=["GET"], strict_slashes=False)
def all_student_projects() -> str:
    """ GET /api/v1/student_projects
    Description: Gets information of all registered student projects
    Return:
      - A List of all student projects Object representation, 200
    """
    all_student_projects = storage.all(StudentProject)
    all_student_projects_list = [student_project.to_dict() for student_project in all_student_projects]
    return jsonify(all_student_projects_list), 200

@app_views.route('/student_projects/<student_project_id>', methods=["GET"], strict_slashes=False)
def one_student_project(student_project_id: str = None) -> str:
    """ GET /api/v1/student_projects/:id
    Path Parameter:
      - Student Project ID
    Description: Gets information of one registered student project
    Return:
      - A JSON representation of the student project, 200
      - 404 if the student project does not exist
    """
    if student_project_id is None:
        abort(404)
    student_project = storage.get(StudentProject, student_project_id)
    if student_project is None:
        abort(404)
    return jsonify(student_project.to_dict()), 200

@app_views.route("/student_projects/<student_project_id>", methods=['DELETE'], strict_slashes=False)
def delete_student_project(student_project_id: str = None) -> str:
    """ DELETE /api/v1/student_projects/:id
    Path Parameter:
      - Student Project ID
    Description: Deletes information of one registered student project
    Return:
      - Empty JSON id, Student Project has been correctly deleted, 204
      - 404 if the Student Project ID doesn't exist
    """
    if student_project_id is None:
        abort(404)
    student_project = storage.get(StudentProject, student_project_id)
    if student_project is None:
        abort(404)
    try:
        student_project.delete()
    except Exception as e:
        abort(404)
    return jsonify({}), 204

@app_views.route("/student_projects", methods=["POST"], strict_slashes=False)
def create_student_project():
    """ POST /api/v1/student_projects
    Description: Create a new Student Project
    Request JSON body:
      - student_id
      - project_id
      - status
    Return:
      - JSON representation of the created student project, 201
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
        if not request_json.get('student_id'):
            error_message = "Student ID Missing"
        elif not request_json.get('project_id'):
            error_message = "Project ID Missing"
        elif not request_json.get('status'):
            error_message = "Status Missing"
        else:
            try:
                student_project = StudentProject()
                student_project.student_id = request_json.get('student_id')
                student_project.project_id = request_json.get('project_id')
                student_project.status = request_json.get('status')
                student_project.save()
                return jsonify(student_project.to_dict()), 201
            except Exception as e:
                error_message = "Can't create a Student Project: {}".format(e)
    return jsonify({"error": error_message}), 404

@app_views.route('/student_projects/<student_project_id>', methods=["PUT"], strict_slashes=False)
def update_student_project(student_project_id: str = None) -> str:
    """ PUT /api/v1/student_project/:id
    Update a student project Data
    Request JSON body
      - student_id
      - project_id
      - status
    Return:
      - JSON representation of the created student project
      - 400 if any required field is missing or if there is an error
    """
    if student_project_id is None:
        abort(404)

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
            student_project = storage.get(StudentProject, student_project_id)
            if student_project is None:
                abort(404)
            student_project.student_id = request_json.get('student_id', student_project.student_id)
            student_project.project_id = request_json.get('project_id', student_project.project_id)
            student_project.status = request_json.get('status', student_project.status)
            student_project.save()
            return jsonify(student_project.to_dict()), 200
        except Exception as e:
            error_message = "Can't update Student Project: {}".format(e)
    return jsonify({"error": error_message}), 400