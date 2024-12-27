#!/usr/bin/python3
from models.base_model import Base
from models.base_model import BaseModel
from sqlalchemy import Column, String, Integer, Text
from sqlalchemy.orm import relationship

class Project(BaseModel, Base):
    __tablename__ = "projects"
    name = Column(String(128), nullable=False)
    description = Column(Text, nullable=False)
    duration = Column(Integer)
    extimatedTime = Column(Integer)
    markdown = Column(Text)
