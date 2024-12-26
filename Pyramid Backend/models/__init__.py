#!/usr/bin/python3
"""
    This Module is used to create an instance of the Database Engine
"""
from models.engine.db_engine import DBEngine

storage = DBEngine()
if storage:
    storage.reload()