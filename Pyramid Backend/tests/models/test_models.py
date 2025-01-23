import unittest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.base_model import Base
from models.user import User, Student
from models.project import Project
from models.course import Course
from models.student_project import StudentProject
from models import storage

class BaseTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.engine = create_engine('mysql+mysqldb://pyramid_dev:pyramid_dev_pwd@localhost/pyramid_dev_db')
        Base.metadata.create_all(cls.engine)
        cls.Session = sessionmaker(bind=cls.engine)
        cls.session = cls.Session()

    @classmethod
    def tearDownClass(cls):
        cls.session.close()
        Base.metadata.drop_all(cls.engine)

class TestUserModel(BaseTestCase):
    def test_create_user(self):
        user = User(first_name="Favour", last_name="Smith", email="favour@example.com")
        self.session.add(user)
        self.session.commit()
        self.assertIsNotNone(user.id)
        self.assertEqual(user.first_name, "Favour")

    def test_update_user(self):
        user = User(first_name="Favour", last_name="Smith", email="favour@example.com")
        self.session.add(user)
        self.session.commit()
        user.first_name = "John"
        self.session.commit()
        self.assertEqual(user.first_name, "John")

    def test_delete_user(self):
        user = User(first_name="Favour", last_name="Smith", email="favour@example.com")
        self.session.add(user)
        self.session.commit()
        self.session.delete(user)
        self.session.commit()
        self.assertIsNone(self.session.query(User).filter_by(id=user.id).first())

class TestStudentModel(BaseTestCase):
    def test_create_student(self):
        student = Student(first_name="Favour", last_name="Smith", email="favour@example.com")
        self.session.add(student)
        self.session.commit()
        self.assertIsNotNone(student.id)
        self.assertEqual(student.first_name, "Favour")

    def test_update_student(self):
        student = Student(first_name="Favour", last_name="Smith", email="favour@example.com")
        self.session.add(student)
        self.session.commit()
        student.first_name = "John"
        self.session.commit()
        self.assertEqual(student.first_name, "John")

    def test_delete_student(self):
        student = Student(first_name="Favour", last_name="Smith", email="favour@example.com")
        self.session.add(student)
        self.session.commit()
        self.session.delete(student)
        self.session.commit()
        self.assertIsNone(self.session.query(Student).filter_by(id=student.id).first())

class TestProjectModel(BaseTestCase):
    def test_create_project(self):
        project = Project(name="Software Engineering", description="Say cheese")
        self.session.add(project)
        self.session.commit()
        self.assertIsNotNone(project.id)
        self.assertEqual(project.name, "Software Engineering")

    def test_update_project(self):
        project = Project(name="Software Engineering", description="Say cheese")
        self.session.add(project)
        self.session.commit()
        project.name = "Data Science"
        self.session.commit()
        self.assertEqual(project.name, "Data Science")

    def test_delete_project(self):
        project = Project(name="Software Engineering", description="Say cheese")
        self.session.add(project)
        self.session.commit()
        self.session.delete(project)
        self.session.commit()
        self.assertIsNone(self.session.query(Project).filter_by(id=project.id).first())

class TestCourseModel(BaseTestCase):
    def test_create_course(self):
        course = Course(name="Python Programming")
        self.session.add(course)
        self.session.commit()
        self.assertIsNotNone(course.id)
        self.assertEqual(course.name, "Python Programming")

    def test_update_course(self):
        course = Course(name="Python Programming")
        self.session.add(course)
        self.session.commit()
        course.name = "Java Programming"
        self.session.commit()
        self.assertEqual(course.name, "Java Programming")

    def test_delete_course(self):
        course = Course(name="Python Programming")
        self.session.add(course)
        self.session.commit()
        self.session.delete(course)
        self.session.commit()
        self.assertIsNone(self.session.query(Course).filter_by(id=course.id).first())

class TestStudentProjectModel(BaseTestCase):
    def test_create_student_project(self):
        student_project = StudentProject(student_id="123", project_id="456", status="pending")
        self.session.add(student_project)
        self.session.commit()
        self.assertIsNotNone(student_project.id)
        self.assertEqual(student_project.status, "pending")

    def test_update_student_project(self):
        student_project = StudentProject(student_id="123", project_id="456", status="pending")
        self.session.add(student_project)
        self.session.commit()
        student_project.status = "done"
        self.session.commit()
        self.assertEqual(student_project.status, "done")

    def test_delete_student_project(self):
        student_project = StudentProject(student_id="123", project_id="456", status="pending")
        self.session.add(student_project)
        self.session.commit()
        self.session.delete(student_project)
        self.session.commit()
        self.assertIsNone(self.session.query(StudentProject).filter_by(id=student_project.id).first())

if __name__ == '__main__':
    unittest.main()