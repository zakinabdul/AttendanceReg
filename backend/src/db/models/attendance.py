from sqlalchemy import Boolean, CheckConstraint, Column, Integer, String, ForeignKey
from src.db.base import Base
from sqlalchemy import Enum, DateTime, Time, Date
from sqlalchemy.sql import func

class attendance_session(Base):
    __tablename__ = "attendance_sessions"

    session_id = Column(Integer, primary_key=True, index=True)
    class_id = Column(Integer, ForeignKey("classes.class_id"), nullable=False, index=True)
    subject_id = Column(Integer, ForeignKey("subjects.subject_id"), nullable=False, index=True)
    teacher_id = Column(Integer, ForeignKey("teachers.teacher_id"), nullable=False, index=True)
    period_id = Column(Integer, nullable=False, index=True)
    session_date = Column(Date, nullable=False, index=True)
    status = Column(Boolean, default=False)  # True if session is completed
    
class attendance_record(Base):
    __tablename__ = "attendance_records"
    record_id = Column(Integer, primary_key=True, index=True)
    session_id = Column(Integer, ForeignKey("attendance_sessions.session_id"), nullable=False, index=True)
    student_id = Column(Integer, ForeignKey("students.student_id"), nullable=False, index=True)
    status = Column(Enum('Present', 'Absent', name='attendance_status'), nullable=False)
    timestamp = Column(DateTime, server_default=func.now(), nullable=False)
    
    
class period(Base):
    __tablename__ = "periods"
    
    period_id = Column(Integer, primary_key=True, index=True)
    period_number = Column(Integer, nullable=False)
    start_time = Column(Time, nullable=False)
    end_time = Column(Time, nullable=False)

    __table_args__ = (
        CheckConstraint('period_number >= 1 AND period_number <= 7', name='check_period_number'),
    )

