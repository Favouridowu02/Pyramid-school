#!/usr/bin/python3
"""
    This Model contains the User class
"""
from models.base_model import Base
from models.base_model import BaseModel
from sqlalchemy import Column, String, Integer

class User(BaseModel, Base):
    """
        This class is used to create the Users Schema
    """
    __tablename__ = "users"
    first_name = Column(String(128), nullable=False) #nulable is set to True because of testing
    last_name = Column(String(128),  nullable=True)
    password = Column(String(128),  nullable=True)
    email = Column(String(128), nullable=True)
    xp = Column(Integer, nullable=True)


# This would be updated soon
class Student(User):
    """
        This Class is used to create the Students Schema
    """
    def __init__(self, first_name, last_name=None, password=None, email=None, xp=None):
        """ Initialize the Student Class
        """
        super.__init__(first_name, last_name, password, email, xp)



class Mentor(User):
    """
        This Class is used to create the Mentor Schema
    """
    __tablename__ = "mentors"
    def __init__(self, first_name, last_name=None, password=None, email=None, xp=None):
        """ Initialize the Student Class
        """
        super.__init__(first_name, last_name, password, email, xp)


class Admin(User):
    """
        This Class is used to create the Admin Schema
    """
    __tablename__ = "admins"
    def __init__(self, first_name, last_name=None, password=None, email=None, xp=None):
        """ Initialize the Student Class
        """
        super.__init__(first_name, last_name, password, email, xp)