#!/usr/bin/python3
"""
    This script populates the database with instances of the models
"""
from models import storage
from models.user import User, Student, Mentor, Admin
from models.project import Project
from models.course import Course
from models.program import Program
from models.user import StudentProject
from models.task import Task

# Reload storage to ensure database is initialized
storage.reload()

# Create and save a User instance
user1 = User(first_name="Favour", last_name="Smith", email="favour@example.com", password="password123")
storage.new(user1)
storage.save()

# Create and save Student instances
student1 = Student(first_name="John", last_name="Doe", user_name="johndoe", email="john.doe@example.com", password="password456", xp=200)
student2 = Student(first_name="Alice", last_name="Johnson", user_name="alicejohnson", email="alice.johnson@example.com", password="password789", xp=150)
storage.new(student1)
storage.new(student2)
storage.save()

# Create and save a Mentor instance
mentor1 = Mentor(first_name="Jane", last_name="Doe", email="jane.doe@example.com", password="password789")
storage.new(mentor1)
storage.save()

# Create and save an Admin instance
admin1 = Admin(first_name="Mark", last_name="Johnson", email="mark.johnson@example.com", password="adminpass789")
storage.new(admin1)
storage.save()

# Create and save a Program instance
program1 = Program(name="Computer Science")
storage.new(program1)
storage.save()

# Create Courses under the Program
course1 = Course(name="Introduction to Programming", program_id=program1.id)
course2 = Course(name="Data Structures", program_id=program1.id)
storage.new(course1)
storage.new(course2)
storage.save()

# Create Projects under Courses
project1 = Project(
    name="Build a Calculator",
    description="A project to build a simple calculator application.",
    duration=7,
    estimated_time=5,
    markdown="### Calculator Project",
    course_id=course1.id
)
project2 = Project(
    name="Binary Search Implementation",
    description="A project to implement binary search.",
    duration=5,
    estimated_time=4,
    markdown="### Binary Search",
    course_id=course2.id
)
storage.new(project1)
storage.new(project2)
storage.save()

# Assign Projects to Students
student_project1 = StudentProject(
    student_id=student1.id,
    project_id=project1.id,
    status="pending"
)
student_project2 = StudentProject(
    student_id=student2.id,
    project_id=project2.id,
    status="done"
)
storage.new(student_project1)
storage.new(student_project2)
storage.save()

# Create and save a Task instance
task1 = Task(name="Task 1", github_link="https://github.com/example/repo", img_url="https://example.com/image.png")
storage.new(task1)
storage.save()

# Print the created instances
print(f"User: {user1}")
print(f"Student: {student1}")
print(f"Student: {student2}")
print(f"Mentor: {mentor1}")
print(f"Admin: {admin1}")
print(f"Program: {program1}")
print(f"Course: {course1}")
print(f"Course: {course2}")
print(f"Project: {project1}")
print(f"Project: {project2}")
print(f"StudentProject: {student_project1}")
print(f"StudentProject: {student_project2}")
print(f"Task: {task1}")