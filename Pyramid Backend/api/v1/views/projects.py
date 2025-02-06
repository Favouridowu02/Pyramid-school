#!/usr/bin/env python3
"""
    This Module contains the API End Points for the Projects
"""
from models.project import Project
from flask import request, jsonify, abort
from models import storage
from api.v1.views import app_views

storage.reload()

@app_views.route('/projects', methods=["GET"], strict_slashes=False)
def all_projects() -> str:
    """ GET /api/v1/projects
    Description: Gets information of all registered projects
    Return:
      - A List of all projects Object representation, 200
    """
    all_projects = storage.all(Project)
    all_projects_list = [project.to_dict() for project in all_projects]
    return jsonify(all_projects_list), 200

@app_views.route('/projects/<project_id>', methods=["GET"], strict_slashes=False)
def one_project(project_id: str = None) -> str:
    """ GET /api/v1/projects/:id
    Path Parameter:
      - Project ID
    Description: Gets information of one registered project
    Return:
      - A JSON representation of the project, 200
      - 404 if the project does not exist
    """
    if project_id is None:
        abort(404)
    project = storage.get(Project, project_id)
    if project is None:
        abort(404)
    return jsonify(project.to_dict()), 200

@app_views.route("/projects/<project_id>", methods=['DELETE'], strict_slashes=False)
def delete_project(project_id: str = None) -> str:
    """ DELETE /api/v1/projects/:id
    Path Parameter:
      - Project ID
    Description: Deletes information of one registered project
    Return:
      - Empty JSON id, Project has been correctly deleted, 204
      - 404 if the Project ID doesn't exist
    """
    if project_id is None:
        abort(404)
    project = storage.get(Project, project_id)
    if project is None:
        abort(404)
    try:
        project.delete()
    except Exception as e:
        abort(404)
    return jsonify({}), 204

@app_views.route("/projects", methods=["POST"], strict_slashes=False)
def create_project():
    """ POST /api/v1/projects
    Description: Create a new Project
    Request JSON body:
      - name
      - description
      - duration
      - estimated_time
      - markdown
      - course_id
    Return:
      - JSON representation of the created project, 201
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
            error_message = "Project Name Missing"
        elif not request_json.get("description"):
            error_message = "Description Missing"
        elif not request_json.get("course_id"):
            error_message = "Missing or Wrong Course ID"
        else:
            try:
                project = Project()
                project.name = request_json.get('name')
                project.description = request_json.get('description')
                project.duration = request_json.get('duration')
                project.estimated_time = request_json.get('estimated_time')
                project.markdown = request_json.get('markdown')
                project.course_id = request_json.get('course_id')
                project.save()
                return jsonify(project.to_dict()), 201
            except Exception as e:
                error_message = "Can't create a Project: {}".format(e)
    return jsonify({"error": error_message}), 404

@app_views.route('/projects/<project_id>', methods=["PUT"], strict_slashes=False)
def update_project(project_id: str = None) -> str:
    """ PUT /api/v1/project/:id
    Update a project Data
    Request JSON body
      - name
      - description
      - duration
      - estimated_time
      - markdown
      - course_id
    Return:
      - JSON representation of the created project
      - 400 if any required field is missing or if there is an error
    """
    if project_id is None:
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
            project = storage.get(Project, project_id)
            if project is None:
                abort(404)
            project.name = request_json.get('name', project.name)
            project.description = request_json.get('description', project.description)
            project.duration = request_json.get('duration', project.duration)
            project.estimated_time = request_json.get('estimated_time', project.estimated_time)
            project.markdown = request_json.get('markdown', project.markdown)
            project.course_id = request_json.get('course_id', project.course_id)
            project.save()
            return jsonify(project.to_dict()), 200
        except Exception as e:
            error_message = "Can't update Project: {}".format(e)
    return jsonify({"error": error_message}), 400