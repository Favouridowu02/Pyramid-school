#!/usr/bin/python3
"""
    This Module contains the Class Model StudentProject
"""
from models.base_model import Base, BaseModel
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.dialects.mysql import ENUM
from sqlalchemy.orm import relationship

class StudentProject(BaseModel, Base):
    """
        This class is used to create the StudentProject Schema
    """
    __tablename__ = "student_projects"
    student_id = Column(String(60), ForeignKey('students.id'), nullable=False)
    project_id = Column(String(60), ForeignKey('projects.id'), nullable=False)
    status = Column(ENUM('done', 'pending', name="status_enum"), nullable=False)

    student = relationship("Student", back_populates="student_projects")
    project = relationship("Project", back_populates="student_projects")

    @classmethod
    def set_status(cls, status, student_id, project_id):
        """
            Set the status of a student project
        """
        student_project = cls.query.filter_by(student_id=student_id, project_id=project_id).first()
        if student_project is None:
            raise ValueError("StudentProject not found")
        if status not in ['done', 'pending']:
            raise ValueError("Invalid status")
        student_project.status = status
        student_project.save()