import unittest
from models.user import Student, Mentor, Admin
from models.task import Task
from models.student_projects import StudentProject
from models.project import Project
from models.program import Program
from models.course import Course
from models.base_model import BaseModel, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class TestModels(unittest.TestCase):
    def setUp(self):
        """Set up test database and session"""
        self.engine = create_engine('sqlite:///:memory:')
        Base.metadata.create_all(self.engine)
        Session = sessionmaker(bind=self.engine)
        self.session = Session()

    def tearDown(self):
        """Tear down test database"""
        self.session.close()
        Base.metadata.drop_all(self.engine)

    def test_create_student(self):
        """Test creating a Student instance"""
        student = Student(first_name="John", last_name="Doe", user_name="johndoe", password="password", email="john@example.com")
        self.session.add(student)
        self.session.commit()
        self.assertIsNotNone(student.id)

    def test_create_mentor(self):
        """Test creating a Mentor instance"""
        mentor = Mentor(first_name="Jane", last_name="Doe", password="password", email="jane@example.com")
        self.session.add(mentor)
        self.session.commit()
        self.assertIsNotNone(mentor.id)

    def test_create_admin(self):
        """Test creating an Admin instance"""
        admin = Admin(first_name="Admin", last_name="User", password="adminpass", email="admin@example.com")
        self.session.add(admin)
        self.session.commit()
        self.assertIsNotNone(admin.id)

    def test_create_task(self):
        """Test creating a Task instance"""
        project = Project(name="Project 1", description="Description", course_id="course1")
        self.session.add(project)
        self.session.commit()
        task = Task(name="Task 1", project_id=project.id)
        self.session.add(task)
        self.session.commit()
        self.assertIsNotNone(task.id)

    def test_create_student_project(self):
        """Test creating a StudentProject instance"""
        student = Student(first_name="John", last_name="Doe", user_name="johndoe", password="password", email="john@example.com")
        project = Project(name="Project 1", description="Description", course_id="course1")
        self.session.add(student)
        self.session.add(project)
        self.session.commit()
        student_project = StudentProject(student_id=student.id, project_id=project.id, status="pending")
        self.session.add(student_project)
        self.session.commit()
        self.assertIsNotNone(student_project.id)

    def test_create_project(self):
        """Test creating a Project instance"""
        project = Project(name="Project 1", description="Description", course_id="course1")
        self.session.add(project)
        self.session.commit()
        self.assertIsNotNone(project.id)

    def test_create_program(self):
        """Test creating a Program instance"""
        program = Program(name="Program 1")
        self.session.add(program)
        self.session.commit()
        self.assertIsNotNone(program.id)

    def test_create_course(self):
        """Test creating a Course instance"""
        program = Program(name="Program 1")
        self.session.add(program)
        self.session.commit()
        course = Course(name="Course 1", program_id=program.id)
        self.session.add(course)
        self.session.commit()
        self.assertIsNotNone(course.id)

if __name__ == '__main__':
    unittest.main()
