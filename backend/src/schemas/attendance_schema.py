from pydantic import BaseModel, field_validator
from typing import Optional, Literal
from datetime import date, datetime, time

# ==================================================
# Attendance Session Schemas
# ==================================================
class AttendanceSessionBase(BaseModel):
    class_id: int
    subject_id: int
    teacher_id: int
    period_id: int
    session_date: date
    status: bool = False  # True if session is completed


class AttendanceSessionCreate(AttendanceSessionBase):
    pass


class AttendanceSessionUpdate(BaseModel):
    status: bool


class AttendanceSessionResponse(AttendanceSessionBase):
    session_id: int

    class Config:
        orm_mode = True


# ==================================================
# Attendance Record Schemas
# ==================================================
class AttendanceRecordBase(BaseModel):
    student_id: int


class AttendanceRecordCreate(AttendanceRecordBase):
    session_id: int
    status: Literal["Present", "Absent"]


class AttendanceRecordUpdate(BaseModel):
    status: Literal["Present", "Absent"]


class AttendanceRecordResponse(AttendanceRecordBase):
    record_id: int
    timestamp: datetime

    class Config:
        orm_mode = True


# ==================================================
# Period Schemas
# ==================================================
class PeriodBase(BaseModel):
    period_number: int
    start_time: time
    end_time: time

    @field_validator("end_time")
    def validate_time(cls, end_time, values):
        """Ensure end_time is after start_time"""
        start_time = values.get("start_time")
        if start_time and end_time <= start_time:
            raise ValueError("end_time must be after start_time")
        return end_time


class PeriodCreate(PeriodBase):
    pass


class PeriodUpdate(BaseModel):
    start_time: time
    end_time: time


class PeriodResponse(PeriodBase):
    period_id: int

    class Config:
        orm_mode = True
