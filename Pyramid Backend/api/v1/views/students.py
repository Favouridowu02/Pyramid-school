#!/usr/bin/env python3
"""
    This Module contains the API Points for the Students
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
      - A List of all students Object representation
    """
    all_students = storage.all(Student)
    all_students_list = [student.to_dict() for student in all_students]
    print("\n\n", all_students_list, "\n\n")
    return jsonify(all_students_list), 200