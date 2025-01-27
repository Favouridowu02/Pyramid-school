#!/usr/bin/env python3
"""
    This Module contains the API End Points for the Projects
"""
from models.user import Project
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
    print("\n\n", all_projects_list, "\n\n")
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
  if project_id == "me":
    if request.current_user is None:
      abort(404)
    else:
      return jsonify(request.current_user.to_dict()), 200
  project = storage.get(Project, project_id)
  if project is None:
    abort(404)
  return jsonify(project.to_dict()), 200


@app_views.route("/projects/<project_id>", methods=['DELETE'],
                 strict_slashes=False)
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
    - first_name
    - last_name
    - user_name
    - password
    - email
    - xp
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
        project = Project()
        project.first_name = request_json.get('first_name')
        project.last_name = request_json.get('last_name')
        project.email = request_json.get("email")
        project.user_name = request_json.get("user_name")
        project.password = request_json.get("password")
        project.save()
        return jsonify(project.to_dict()), 201
      except Exception as e:
        error_message = "Can't create a Project: {}".format(e)
  return jsonify({"error": error_message}), 404


@app_views.route('/projects/<project_id>', methods=["PUT"], strict_slashes=False)
def update_project(patient_id: str = None) -> str:
  """ PUT /api/v1/project/:id
  Update a project Data
  Request JSON body
    - first_name
    - last_name
    - user_name
    - password
    - email
    - xp
  Return:
    - JSON representation of the created project
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
    project = storage.get(Project, project_id)
    if project is None:
      abort(404)
    first_name = request_json.get('first_name',
                                  project.first_name)
    last_name = request_json.get('last_name',
                                  project.last_name)
    project.first_name = first_name
    project.last_name = last_name
    project.user_name = request_json.get('user_name', project.user_name)
    project.password = request_json.get('password', project.password)
    project.email = request_json.get('email', project.email)

    project.save()
    return jsonify(project.to_dict()), 200
  except Exception as e:
      error_message = "Can't update Project: {}".format(e)
return jsonify({"error": error_message}), 400