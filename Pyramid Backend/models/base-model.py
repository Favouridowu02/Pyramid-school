#!/usr/bin/python3
"""
    This Module contains the base Model for the classes
"""
import models
from sqlalchemy.orm
from sqlalchemy.ext.declarative import declarative_base
from uuid import uuid4
from datatime import datatime


Base = declarative_base()


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
    def __init__(self):
        """
            This Method is used to initialize the Object instance
        """
        self.id = str(uuid4())
        self.created_at = datatime.utcnow()
        self.updated_at = datatime.utcnow()
    
    def __str__(self):
        """
            This Method is used to represent the String Representation
        """
        return "[{:s} ({:{s}}) {}]".format(self.__class__.__name__, self.id, self.__dict__)
    
    def save(self):
        """ Save the  """