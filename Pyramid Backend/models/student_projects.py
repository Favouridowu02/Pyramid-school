#!/usr/bin/python3
"""
    This Model contains the Student project class
"""
from models.base_model import Base, BaseModel
from sqlalchemy import Column, String, Integer, ForeignKey, Enum
from sqlalchemy.orm import relationship


class StudentProject(BaseModel, Base):
    """
        This class is used to create the StudentProject Schema
    """
    __tablename__ = "student_projects"
    student_id = Column(String(60), ForeignKey('students.id'), nullable=False)
    project_id = Column(String(60), ForeignKey('projects.id'), nullable=False)
    status = Column(Enum('done', 'pending', name="status_enum"), nullable=False)

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

# Define relationships after both classes have been defined
# from models.user import Student
# from models.project import Project

# Student.student_projects = relationship("StudentProject", back_populates="student")
# StudentProject.student = relationship("Student", back_populates="student_projects")
# StudentProject.project = relationship("Project", back_populates="student_projects")