#!/usr/bin/env python3
"""
    This Module contains the API End Points for the Students
"""
from models.user import Student
from flask import request, jsonify, abort
from models import storage
from api.v1.views import app_views

storage.reload()

@app_views.route('/students', methods=["GET"], strict_slashes=False)
def all_students() -> str:
    """ GET /api/v1/students
    Description: Gets information of all registered students
    Return:
      - A List of all students Object representation, 200
    """
    all_students = storage.all(Student)
    all_students_list = [student.to_dict() for student in all_students]
    return jsonify(all_students_list), 200

@app_views.route('/students/<student_id>', methods=["GET"], strict_slashes=False)
def one_student(student_id: str = None) -> str:
    """ GET /api/v1/students/:id
    Path Parameter:
      - Student ID
    Description: Gets information of one registered student
    Return:
      - A JSON representation of the student, 200
      - 404 if the student does not exist
    """
    if student_id is None:
        abort(404)
    student = storage.get(Student, student_id)
    if student is None:
        abort(404)
    return jsonify(student.to_dict()), 200

@app_views.route("/students/<student_id>", methods=['DELETE'], strict_slashes=False)
def delete_student(student_id: str = None) -> str:
    """ DELETE /api/v1/students/:id
    Path Parameter:
      - Student ID
    Description: Deletes information of one registered student
    Return:
      - Empty JSON id, Student has been correctly deleted, 204
      - 404 if the Student ID doesn't exist
    """
    if student_id is None:
        abort(404)
    student = storage.get(Student, student_id)
    if student is None:
        abort(404)
    try:
        student.delete()
    except Exception as e:
        abort(404)
    return jsonify({}), 204

@app_views.route("/students", methods=["POST"], strict_slashes=False)
def create_student():
    """ POST /api/v1/students
    Description: Create a new Student
    Request JSON body:
      - first_name
      - last_name
      - user_name
      - password
      - email
      - xp
    Return:
      - JSON representation of the created student, 201
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
                student = Student()
                student.first_name = request_json.get('first_name')
                student.last_name = request_json.get('last_name')
                student.email = request_json.get("email")
                student.user_name = request_json.get("user_name")
                student.password = request_json.get("password")
                student.save()
                return jsonify(student.to_dict()), 201
            except Exception as e:
                error_message = "Can't create a Student: {}".format(e)
    return jsonify({"error": error_message}), 404

@app_views.route('/students/<student_id>', methods=["PUT"], strict_slashes=False)
def update_student(student_id: str = None) -> str:
    """ PUT /api/v1/student/:id
    Update a student Data
    Request JSON body
      - first_name
      - last_name
      - user_name
      - password
      - email
      - xp
    Return:
      - JSON representation of the created student
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
            student = storage.get(Student, student_id)
            if student is None:
                abort(404)
            student.first_name = request_json.get('first_name', student.first_name)
            student.last_name = request_json.get('last_name', student.last_name)
            student.user_name = request_json.get('user_name', student.user_name)
            student.password = request_json.get('password', student.password)
            student.email = request_json.get('email', student.email)
            student.save()
            return jsonify(student.to_dict()), 200
        except Exception as e:
            error_message = "Can't update Student: {}".format(e)
    return jsonify({"error": error_message}), 400