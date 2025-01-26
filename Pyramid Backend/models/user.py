#!/usr/bin/python3
"""
    This Model contains the User class
"""
from models.base_model import Base, BaseModel
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship


class Student(BaseModel, Base):
    """
        This Class is used to create the Students Schema
    """
    __tablename__ = "students"
    first_name = Column(String(128), nullable=False)
    last_name = Column(String(128),  nullable=False)
    user_name = Column(String(128), nullable=False, unique=True)
    password = Column(String(128),  nullable=False)
    email = Column(String(128), nullable=False, unique=True)
    xp = Column(Integer, nullable=False, default=0)

    # student_projects = relationship("StudentProject", back_populates="student")


class Mentor(BaseModel, Base):
    """
        This Class is used to create the Mentor Schema
    """
    __tablename__ = "mentors"
    first_name = Column(String(128), nullable=False)
    last_name = Column(String(128),  nullable=False)
    password = Column(String(128),  nullable=False)
    email = Column(String(128), nullable=False, unique=True)


class Admin(BaseModel, Base):
    """
        This Class is used to create the Admin Schema
    """
    __tablename__ = "admins"
    first_name = Column(String(128), nullable=False)
    last_name = Column(String(128),  nullable=False)
    password = Column(String(128),  nullable=False)
    email = Column(String(128), nullable=False, unique=True)
