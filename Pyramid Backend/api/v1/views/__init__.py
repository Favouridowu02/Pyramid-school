#!/usr/bin/env python3
"""
    This Module is used to set up the blueprint for the models
"""
from flask import Blueprint

app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')

# Import all the views
from api.v1.views import index
from api.v1.views.students import *
from api.v1.views.mentors import *
from api.v1.views.admins import *
from api.v1.views.programs import *
from api.v1.views.courses import *
from api.v1.views.projects import *
from api.v1.views.tasks import *
from api.v1.views.student_projects import *


