#!/usr/bin/python3
from models.basemodel import Base
from models.basemodel import BaseModel
from sqlalchemy import Column, String, Integer

class User(BaseModel, Base):
    __tablename__ = "users"
    first_name = Column(String(128), nullable=False) #nulable is set to True because of testing
    last_name = Column(String(128),  nullable=True)
    password = Column(String(128),  nullable=True)
    email = Column(String(128), nullable=True)
    xp = Column(Integer, nullable=True)
