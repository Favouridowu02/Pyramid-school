#!/usr/bin/env python3
"""
    This Module contains the API End Points for the Tasks
"""
from models.user import Task
from flask import request, jsonify, abort
from models import storage
from api.v1.views import app_views


storage.reload()

@app_views.route('/tasks', methods=["GET"], strict_slashes=False)
def all_tasks() -> str:
    """ GET /api/v1/tasks
    Description: Gets information of all registered tasks
    Return:
      - A List of all tasks Object representation, 200
    """
    all_tasks = storage.all(Task)
    all_tasks_list = [task.to_dict() for task in all_tasks]
    print("\n\n", all_tasks_list, "\n\n")
    return jsonify(all_tasks_list), 200

@app_views.route('/tasks/<task_id>', methods=["GET"], strict_slashes=False)
def one_task(task_id: str = None) -> str:
  """ GET /api/v1/tasks/:id
  Path Parameter:
    - Task ID
  Description: Gets information of one registered task
  Return:
    - A JSON representation of the task, 200
    - 404 if the task does not exist
  """
  if task_id is None:
    abort(404)
  if task_id == "me":
    if request.current_user is None:
      abort(404)
    else:
      return jsonify(request.current_user.to_dict()), 200
  task = storage.get(Task, task_id)
  if task is None:
    abort(404)
  return jsonify(task.to_dict()), 200


@app_views.route("/tasks/<task_id>", methods=['DELETE'],
                 strict_slashes=False)
def delete_task(task_id: str = None) -> str:
  """ DELETE /api/v1/tasks/:id
  Path Parameter:
    - Task ID
  Description: Deletes information of one registered task
  Return:
    - Empty JSON id, Task has been correctly deleted, 204
    - 404 if the Task ID doesn't exist
  """
  if task_id is None:
    abort(404)
  task = storage.get(Task, task_id)
  if task is None:
    abort(404)
  try:
    task.delete()
  except Exception as e:
    abort(404)
  return jsonify({}), 204


@app_views.route("/tasks", methods=["POST"], strict_slashes=False)
def create_task():
  """ POST /api/v1/tasks
  Description: Create a new Task
  Request JSON body:
    - first_name
    - last_name
    - user_name
    - password
    - email
    - xp
  Return:
    - JSON representation of the created task, 201
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
        task = Task()
        task.first_name = request_json.get('first_name')
        task.last_name = request_json.get('last_name')
        task.email = request_json.get("email")
        task.user_name = request_json.get("user_name")
        task.password = request_json.get("password")
        task.save()
        return jsonify(task.to_dict()), 201
      except Exception as e:
        error_message = "Can't create a Task: {}".format(e)
  return jsonify({"error": error_message}), 404


@app_views.route('/tasks/<task_id>', methods=["PUT"], strict_slashes=False)
def update_task(patient_id: str = None) -> str:
  """ PUT /api/v1/task/:id
  Update a task Data
  Request JSON body
    - first_name
    - last_name
    - user_name
    - password
    - email
    - xp
  Return:
    - JSON representation of the created task
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
    task = storage.get(Task, task_id)
    if task is None:
      abort(404)
    first_name = request_json.get('first_name',
                                  task.first_name)
    last_name = request_json.get('last_name',
                                  task.last_name)
    task.first_name = first_name
    task.last_name = last_name
    task.user_name = request_json.get('user_name', task.user_name)
    task.password = request_json.get('password', task.password)
    task.email = request_json.get('email', task.email)

    task.save()
    return jsonify(task.to_dict()), 200
  except Exception as e:
      error_message = "Can't update Task: {}".format(e)
return jsonify({"error": error_message}), 400