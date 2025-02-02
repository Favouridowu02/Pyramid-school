#!/usr/bin/python3
"""
    This Model contains the Course class
"""
from models.base_model import Base, BaseModel
from sqlalchemy import Column, String, ForeignKey
from models.program import Program
from sqlalchemy.orm import relationship


class Course(BaseModel, Base):
    """
        This Class is used to create the database Schema of the Course
    """
    __tablename__ = "courses"
    name = Column(String(128), nullable=False)
    program_id = Column(String(60), ForeignKey('programs.id', ondelete="CASCADE"), nullable=False)

    program = relationship("Program", back_populates="courses")
    projects = relationship("Project", back_populates="course", cascade="all, delete-orphan")