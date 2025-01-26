#!/usr/bin/python3
"""
    This script populates the database with instances of the models
"""
from models import storage
from models.user import Student, Mentor, Admin
from models.student_projects import StudentProject
from models.project import Project
from models.course import Course
from models.program import Program
from models.task import Task


# Reload storage to ensure database is initialized
storage.reload()

# Create a Program
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

# Create Students
student1 = Student(
    first_name="John", 
    last_name="Doe", 
    user_name="jodo",
    email="john.doe@example.com", 
    password="password456", 
    xp=200
)
student2 = Student(
    first_name="Jane", 
    last_name="Smith", 
    user_name="jo",
    email="jane.smith@example.com", 
    password="password123", 
    xp=150
)
storage.new(student1)
storage.new(student2)
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

# Create Mentors
mentor1 = Mentor(
    first_name="Alice",
    last_name="Brown",
    email="alice.brown@example.com",
    password="mentorpass123"
)
storage.new(mentor1)
storage.save()

# Create Admins
admin1 = Admin(
    first_name="Mark",
    last_name="Johnson",
    email="mark.johnson@example.com",
    password="adminpass789"
)
storage.new(admin1)
storage.save()

# Create and save a Task instance
task1 = Task(name="Task 1", github_link="https://github.com/example/repo", img_url="https://example.com/image.png")
storage.new(task1)
storage.save()

# Print the created instances
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

print("\n\n Database populated successfully!")
