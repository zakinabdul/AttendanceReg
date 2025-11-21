from sqlalchemy import Boolean, Column, Integer, String, TIMESTAMP, ForeignKey
from src.db.base import Base
from sqlalchemy.orm import relationship
class User(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True, index=True)
    user_name = Column(String, nullable=False, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    password_hash = Column(String, nullable=False)
    created_at = Column(TIMESTAMP, server_default='NOW()')
    role= Column(String, nullable=False, index=True)  # e.g., 'student', 'teacher', 'admin'
    
    teacher = relationship("Teacher", back_populates="user", uselist=False)
    student = relationship("Student", back_populates="user", uselist=False)

class Teacher(Base):
    __tablename__ = "teachers"

    teacher_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.user_id"), nullable=True)
    subject_id = Column(Integer, ForeignKey("subjects.subject_id"), nullable=True)
    employee_id = Column(String, unique=True, nullable=False, index=True)
    department = Column(String, nullable=True, index=True)
    
    user = relationship("User", back_populates="teacher")
    # There are two FK paths between Teacher and Subject in the schema:
    # - Subject.employee_id -> teachers.employee_id
    # - Teacher.subject_id -> subjects.subject_id
    # SQLAlchemy cannot disambiguate joins when multiple FK paths exist,
    # so specify which foreign key the relationship should use.
    subjects = relationship(
        "Subject",
        back_populates="teacher",
        foreign_keys="[Subject.employee_id]",
    )

    # Optional: relationship to the 'primary' subject (if subject_id is used
    # to point to a primary subject for the teacher)
    primary_subject = relationship(
        "Subject",
        foreign_keys="[Teacher.subject_id]",
        uselist=False,
    )
    
class Student(Base):
    __tablename__ = "students"

    student_id = Column(Integer, primary_key=True, index=True)
    register_number = Column(String, unique=True, nullable=False, index=True)
    course = Column(String, nullable=False, index=True)
    semester = Column(Integer, nullable=False, index=True)
    class_id = Column(Integer, ForeignKey("classes.class_id"), nullable=False)
    user_id = Column(Integer, ForeignKey("users.user_id"), nullable=True)
    
    user = relationship("User", back_populates="student")
