from pydantic import BaseModel
from typing import Optional,List
from .class_schema import ClassCreate
#User schemas
class UserBase(BaseModel):
    user_name: str 
    email: str
    role: str  # e.g., 'student', 'teacher', 'admin'

class UserCreate(UserBase):
    password: str
    register_number:Optional[str]=None
    employee_id:Optional[str]=None
    #class_details: Optional["ClassCreate"] = None
    
class UserResponse(UserBase):
    user_id: str
    created_at: str  # ISO formatted datetime string
    
# Teacher schemas
class TeacherBase(BaseModel):
    employee_id: str
    department: str | None = None
    subject_id: int | None = None
class TeacherCreate(TeacherBase):
    pass
class TeacherResponse(TeacherBase):
    teacher_id: int
    user_id: int
    

# Student schemas
class StudentBase(BaseModel):
    register_number: str
    course: str
    semester: int

class StudentResponse(StudentBase):
    class_id: int
    user_id: Optional[int] = None
    student_id: int


class StudentOut(BaseModel):
    user_name: str
    register_number: str
    # Add other fields you want to show the frontend
    
    class Config:
        from_attributes = True # This tells Pydantic to read from SQLAlchemy models

# 2. Schema for the WHOLE response
class StudentListResponse(BaseModel):
    message: str
    students: List[StudentOut] # A list of the schema above
    session_id: int
    
    
#UserCreate.model_rebuild()

#TODO schemas for login

class UserLoginBase(BaseModel):
    user_name: str
    password: str
    
# schema for student attendance view
class StudentAttendanceBae(BaseModel):
    student_id: str