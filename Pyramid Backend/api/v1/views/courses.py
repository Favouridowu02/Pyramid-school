#!/usr/bin/env python3
"""
    This Module contains the API End Points for the Courses
"""
from models.course import Course
from flask import request, jsonify, abort
from models import storage
from api.v1.views import app_views


storage.reload()

@app_views.route('/courses', methods=["GET"], strict_slashes=False)
def all_courses() -> str:
    """ GET /api/v1/courses
    Description: Gets information of all registered courses
    Return:
      - A List of all courses Object representation, 200
    """
    all_courses = storage.all(Course)
    all_courses_list = [course.to_dict() for course in all_courses]
    return jsonify(all_courses_list), 200

@app_views.route('/courses/<course_id>', methods=["GET"], strict_slashes=False)
def one_course(course_id: str = None) -> str:
  """ GET /api/v1/courses/:id
  Path Parameter:
    - Course ID
  Description: Gets information of one registered course
  Return:
    - A JSON representation of the course, 200
    - 404 if the course does not exist
  """
  if course_id is None:
    abort(404)
  if course_id == "me":
    if request.current_user is None:
      abort(404)
    else:
      return jsonify(request.current_user.to_dict()), 200
  course = storage.get(Course, course_id)
  if course is None:
    abort(404)
  return jsonify(course.to_dict()), 200


@app_views.route("/courses/<course_id>", methods=['DELETE'],
                 strict_slashes=False)
def delete_course(course_id: str = None) -> str:
  """ DELETE /api/v1/courses/:id
  Path Parameter:
    - Course ID
  Description: Deletes information of one registered course
  Return:
    - Empty JSON id, Course has been correctly deleted, 204
    - 404 if the Course ID doesn't exist
  """
  if course_id is None:
    abort(404)
  course = storage.get(Course, course_id)
  if course is None:
    abort(404)
  try:
    course.delete()
  except Exception as e:
    abort(404)
  return jsonify({}), 204


@app_views.route("/courses", methods=["POST"], strict_slashes=False)
def create_course():
  """ POST /api/v1/courses
  Description: Create a new Course
  Request JSON body:
    - name
    - program_id
  Return:
    - JSON representation of the created course, 201
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
      error_message = "Course Name Missing"
    elif not request_json.get("program_id"):
      error_message = "Missing or Wrong Program ID"
    else:
      try:
        course = Course()
        course.name = request_json.get('name')
        course.program_id = request_json.get('program_id')
        course.save()
        return jsonify(course.to_dict()), 201
      except Exception as e:
        error_message = "Can't create a Course: {}".format(e)
  return jsonify({"error": error_message}), 404


@app_views.route('/courses/<course_id>', methods=["PUT"], strict_slashes=False)
def update_course(course_id: str = None) -> str:
  """ PUT /api/v1/course/:id
  Update a course Data
  Request JSON body
    - name
    - program_id
  Return:
    - JSON representation of the created course
    - 400 if any required field is missing or if there is an error
  """
  if course_id is None:
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
      course = storage.get(Course, course_id)
      print("\n\n", course, f'"{course_id}"')
      if course is None:
        abort(404)
      course.name = request_json.get('name', course.name)
      course.program_id = request_json.get('program_id', course.program_id)
      course.save()
      return jsonify(course.to_dict()), 200
    except Exception as e:
        error_message = "Can't update Course: {}".format(e)
  return jsonify({"error": error_message}), 400