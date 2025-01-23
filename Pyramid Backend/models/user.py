#!/usr/bin/python3
"""
    This Model contains the User class
"""
from models.base_model import Base, BaseModel
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship

class User:
    """
        This class is used to create the Users Schema
    """
    first_name = Column(String(128), nullable=False)
    last_name = Column(String(128),  nullable=True)
    password = Column(String(128),  nullable=True)
    email = Column(String(128), nullable=True)
    def __init__(first_name, last_name=None, password=None, email=None):
        


# This would be updated soon
class Student(BaseModel, User, Base):
    """
        This Class is used to create the Students Schema
    """
    __tablename__ = "students"
    xp = Column(Integer, nullable=True)

    student_projects = relationship("StudentProject", back_populates="student")
    def __init__(self):
        """ Initialize the Student Class
        """
        super().__init__()


class Mentor(BaseModel, User, Base):
    """
        This Class is used to create the Mentor Schema
    """
    __tablename__ = "mentors"
    def __init__(self):
        """ Initialize the Student Class
        """
        super().__init__()


class Admin(BaseModel, User, Base):
    """
        This Class is used to create the Admin Schema
    """
    __tablename__ = "admins"
    def __init__(self):
        """ Initialize the Student Class
        """
        super().__init__()