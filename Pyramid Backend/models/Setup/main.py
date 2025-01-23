#!/usr/bin/env python3
"""
    This module is used to set up the database and create instances
"""
from models import storage
from models.user import Mentor, Student, Admin
from models.project import Project
from models.program import Program
from models.course import Course
from models.student_project import StudentProject

# Reload storage to ensure database is initialized
storage.reload()

# Create and save a Student instance
student1 = Student(first_name="John", last_name="Doe", email="john.doe@example.com", password="password456", xp=200)
storage.add(student1)
storage.save()

# Create and save a Mentor instance
student1 = Student(first_name="John", last_name="Doe", email="john.doe@example.com", password="password456", xp=200)
storage.add(student1)
storage.save()

# Create and save an Admin instance
admin1 = Admin(first_name="Admin", last_name="User", email="admin@example.com", password="adminpass", xp=300)
storage.add(admin1)
storage.save()

# Create and save a project1
program1 = Program(name="Introduction to Programming")
storage.add(program1)
storage.save()

# Create and save a Course instance
course1 = Course(name="Python Programming")
storage.add(course1)
storage.save()

# Create and save a Project instance
project1 = Project(name="Software Engineering", description="Say cheese", duration=10, estimatedTime=5, markdown="## Project 1", course=course1, course_id=course1.id)
storage.add(project1)
storage.save()

# Create and save a StudentProject instance
student_project1 = StudentProject(student_id=student1.id, project_id=project1.id, status="pending")
storage.add(student_project1)
storage.save()

# Print the created instances
print(f"Student: {student1}")
print(f"Admin: {admin1}")
print(f"Course: {course1}")
print(f"Project: {project1}")
print(f"StudentProject: {student_project1}")