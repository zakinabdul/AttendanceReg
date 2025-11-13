from pydantic import BaseModel

# -------------------- Class Schemas --------------------
class ClassBase(BaseModel):
    department: str
    semester: int
    section: str


class ClassCreate(ClassBase):
    pass


class ClassUpdate(ClassBase):
    pass


class ClassResponse(ClassBase):
    class_id: int

    class Config:
        orm_mode = True


# -------------------- Subject Schemas --------------------
class SubjectBase(BaseModel):
    subject_name: str
    subject_code: str
    employee_id: int
    class_id: int
    credits: int


class SubjectCreate(SubjectBase):
    pass


class SubjectUpdate(SubjectBase):
    pass


class SubjectResponse(SubjectBase):
    subject_id: int

    class Config:
        orm_mode = True
