#!/usr/bin/python3
"""
    This Module contains the base Model for the classes
"""
import models
from sqlalchemy import Column, Integer, DataTime, Boolean
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.ext.declarative import declarative_base
from uuid import uuid4
from datatime import datatime


class Base(DeclarativeBase):
    """
        This class is used to Create the Base Class
    """
    pass


class BaseModel:
    """
        This class Represents the base Model

        Methods:
            - to_dict: To convert the instance of this class to a Json format
            - save: To save the instance of the class to the Engine{Database}
            - delete: This is used to delete the object from the Engine{Database}
            - update: This is used to update the object in the Engine{Database}

        Attributes:
            - id: The uuidn  instance used to uniquely represent the object
            - created_at: This is used to represent when the object was created
            - updated_at: This is used to represent when the object was last updated
    """
    id:Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    created_at = mapped_column(DataTime, default=datatime.utcnow)
    updated_at = mapped_column(DataTime, default=datatime.utcnow, onupdate=datatime.utcnow)

    def to_dict(self):
        """  """
    # def __init__(self, *args, **kwargs):
    #     """
    #         This Method is used to initialize the Object instance
    #     """
    #     self.id = kwargs.get(id, str(uuid4()))
    #     self.created_at = datatime.utcnow()
    #     self.updated_at = datatime.utcnow()
    
    # def __str__(self):
    #     """
    #         This Method is used to represent the String Representation
    #     """
    #     return "[{:s} ({:{s}}) {}]".format(self.__class__.__name__, self.id, self.__dict__)
    
    def save(self):
        """
            This method is used to save the instance to the Engine Storage
        """
        self.updated_at = datetime.utcnow()
        models.storage.new(self)
        models.storage.save()

    def delete(self):
        """
            This Method is used to delete an instance from the database Model
        """
        models.storage.delete(self)