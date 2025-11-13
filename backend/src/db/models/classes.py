from sqlalchemy import Boolean, Column, Integer, String, ForeignKey
from src.db.base import Base
from sqlalchemy.orm import relationship

class Class(Base):
    __tablename__ = "classes"

    class_id = Column(Integer, primary_key=True, index=True)
    department = Column(String, nullable=False, index=True)
    semester = Column(Integer, nullable=False, index=True)
    section = Column(String, nullable=False, index=True)
    
    subjects = relationship("Subject", back_populates="class_")

class Subject(Base):
    __tablename__ = "subjects"

    subject_id = Column(Integer, primary_key=True, index=True)
    subject_name = Column(String, nullable=False, index=True)
    subject_code = Column(String, unique=True, nullable=False, index=True)
    employee_id = Column(String, ForeignKey("teachers.employee_id"), nullable=False, index=True)
    class_id = Column(Integer, ForeignKey("classes.class_id"), nullable=False, index=True)
    credits = Column(Integer, nullable=False)
    
    class_ = relationship("Class", back_populates="subjects")
    teacher = relationship("Teacher", back_populates="subjects", foreign_keys=[employee_id])
