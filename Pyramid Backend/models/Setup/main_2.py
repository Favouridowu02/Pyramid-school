#!/usr/bin/python3
"""
    This Module contains the Test file to delete a Model instance - Object
"""
from models import storage
from models.program import Program


storage.reload()


program = storage.get(Program, "bb108af2-0af7-41fb-89b6-e22e10fef187")
print(program)
# program.delete()
