#!/usr/bin/python3
"""
    This Module contains the Database Engine for the Pyramid

    Technologies:
        - Database: Mysql
        - ORM: Sqlalchemy
        - Language: Python
"""
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

load_dotenv()

class DBEngine():
    """
        This Engine is used represent the Database Engine
    """
    __engine = None
    __session = None

    def __init__(self):
        """
            This is the initialization of the Database engine
        """
        pass

    def new(self, obj):
        """
            This Method is used to add the object to the database session
        """
        pass

    def save(self):
        """
            This Method is used to save the object to the database 
        """
        pass

    def delete(self, obj=None):
        """
            This Method is used to delete the object from the database session 
        """
        pass

    def reload(self):
        """
            This Method is used to reload data from the session
        """
        pass

    def close(self):
        """
            This session is used to close the private session
        """
        pass

    def get(self, cls, id):
        """
            This Method is used to retrieve an object based on
            the id from the database

            Atrributes:
                cls: The class
                id: A String representation of the ID

            Return: The object based on the class and its ID, or None
                    id not Found.
        """
        pass

