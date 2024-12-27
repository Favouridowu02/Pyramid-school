#!/usr/bin/python3
from models.base_model import Base
from models.base_model import BaseModel
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

class Course(BaseModel, Base):
    __tablename__ = "courses"
    name = Column(String(128), nullable=False)
    projects = relationship("Project", back_populates="courses")
    