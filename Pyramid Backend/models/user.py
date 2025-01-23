#!/usr/bin/python3
"""
    This Model contains the User class
"""
from models.base_model import Base, BaseModel
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship


class Student(BaseModel, Base):
    """
        This Class is used to create the Students Schema
    """
    __tablename__ = "students"
    first_name = Column(String(128), nullable=False)
    last_name = Column(String(128),  nullable=True)
    password = Column(String(128),  nullable=True)
    email = Column(String(128), nullable=True)
    xp = Column(Integer, nullable=True)

    student_projects = relationship("StudentProject", back_populates="student")


class Mentor(BaseModel, Base):
    """
        This Class is used to create the Mentor Schema
    """
    __tablename__ = "mentors"
    first_name = Column(String(128), nullable=False)
    last_name = Column(String(128),  nullable=True)
    password = Column(String(128),  nullable=True)
    email = Column(String(128), nullable=True)


class Admin(BaseModel, Base):
    """
        This Class is used to create the Admin Schema
    """
    __tablename__ = "admins"
    first_name = Column(String(128), nullable=False)
    last_name = Column(String(128),  nullable=True)
    password = Column(String(128),  nullable=True)
    email = Column(String(128), nullable=True)