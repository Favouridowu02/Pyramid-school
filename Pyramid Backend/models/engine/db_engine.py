#!/usr/bin/python3
"""
    This Module contains the Database Engine for the Pyramid

    Technologies:
        - Database: Mysql
        - ORM: Sqlalchemy
        - Language: Python
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from dotenv import load_dotenv
from models.base_model import Base
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
        self.__database_url = os.getenv("DATABASE_URL")
        # print(self.__database_url)
        self.__engine = create_engine(self.__database_url)

        if os.getenv('PYRAMID_STAGE') == "test":
            Base.metadata.drop_all(self.__engine)

    def new(self, obj):
        """
            This Method is used to add the object to the database session
        """
        try:
            self.__session.add(obj)
        except Exception as e:
            print(f"Error adding object: {e}")

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
        self.__session = Session

    def close(self):
        """
            This session is used to close the private session
        """
        self.__session.close()

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

        obj = self.__session(cls).filter_by(cls.id == id)
        return obj

    def all(self, cls=None):
        """query on the current database session"""
        if cls is None:
            return None
        objs = self.__session.query(cls).all()
        return objs