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

DATABASE_URL = os.getenv('DATABASE_URL')
print(DATABASE_URL)

class DBEngine():
    """
        This Engine is used represent the Database Engine
    """
    __engine = None
    __session = None

    def __init__(self):
        self.__engine = create_engine(DATABASE_URL)
        """this Part will be updated when the dotenv is used"""
        if PYRAMID_TEST == "test":
            Base.metadata.drop_all(self.__engine)
    
    def new(self, obj):
        """
            This Method is used to add the object to the database session
        """
        self.__session.add(obj)

    def save(self):
        """
            This Method is used to save the object to the database 
        """
        self.__session.commit()

    def delete(self, obj=None):
        """
            This Method is used to delete the object from the database session 
        """
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """
            This Method is used to reload data from the session
        """
        Base.metadata.create_all(self.__engine)
        sess_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sess_factory)
        self.__session = Session()

    def close(self):
        """
            This session is used to close the private session
        """
        self.__session.remove()

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
        if cls is None or id is None:
            return None
        objects = self.all(cls)

