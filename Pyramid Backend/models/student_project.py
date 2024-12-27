#!/usr/bin/python3
from models.base_model import Base, BaseModel
from sqlalchemy import Column, String
from sqlalchemy.dialects.mysql import ENUM

class StudentProject(BaseModel, Base):
    __tablename__ = "student_projects"
    student_id = Column(String(60), nullable=False)
    project_id = Column(String(60), nullable=False)
    status = Column('status', ENUM('done', 'pending', name="status_enum"), nullable=False)

    @classmethod
    def set_status(self, status, student_id, project_id):
        student_project = self.query.filter_by(student_id=student_id, project_id=project_id).first()
        student_project.status = status
        student_project.save()