#!/usr/bin/python3
"""
    This Model contains the Task class
"""
from models.base_model import Base, BaseModel
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship

class Task(BaseModel, Base):
    """
        This Class is used to create the database Schema of the Task
    """
    __tablename__ = "tasks"
    name = Column(String(128), nullable=False)
    github_link = Column(String(128), nullable=True)
    img_url = Column(String(128), nullable=True)
