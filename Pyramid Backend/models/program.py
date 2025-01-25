#!/usr/bin/python3
"""
    This model is contains the Program class
"""
from models.base_model import Base, BaseModel
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class Program(Base, BaseModel):
    """
        This Class is used to create the Program database Schema
    """
    __tablename__ = "programs"
    name = Column(String(128), nullable=False)
    courses = relationship("Course", back_populates="program")