from src.api.deps import DatabaseSession
from fastapi import APIRouter, Depends, HTTPException, status
from src.schemas import user_schema 
from src.db.models import user,classes
from src.core.logger import logger
router = APIRouter(
    prefix="/auth",
   tags=["auth"]
)

@router.post("/user_registeration", status_code=status.HTTP_201_CREATED)
async def user_creation(data: user_schema.UserCreate, db: DatabaseSession):
    
    """
    {
  "user_name": "Boby",
  "email": "boby@gmail.com",
  "role": "teacher",
  "password": "boby123",
  "register_number": "string",
  "employee_id": "EMP1007"
  }
    """
    logger.debug(f"Received data {data.dict()}")
    new_user = user.User(
        user_name=data.user_name,
        email = data.email,
        password_hash=data.password,
        role=data.role
    )
    db.add(new_user)
    #db.commit()
    #db.refresh(new_user)
    logger.info("Successfully added basic user details")
    if data.role=="student":
        reg_number = data.register_number
        #logger.info(f"register number entered: {reg_number}")
        if not reg_number:
            raise HTTPException(status_code=400, detail="Student Register Number required")
        
        
        student = db.query(user.Student).filter(user.Student.register_number==reg_number).first()
        #logger.info(f"the student id: {student.student_id}")
        if not student:
            raise HTTPException(status_code=400, detail="No record of that student")
        
        if student.user_id is not None:
            raise HTTPException(status_code=400, detail="User already linked to this register number")

        student.user_id = new_user.user_id
        #db.commit()
        
    elif data.role=="teacher":
        emp_id = data.employee_id
        logger.info(f"employee id entered {emp_id}")
        if not emp_id:
            return HTTPException(status_code=400, detail="Teacher Employee ID is required")
        
        teacher = db.query(user.Teacher).filter(user.Teacher.employee_id==emp_id).first()
        #logger.info(f"teacher {teacher.teacher_id}")
        
        if not teacher:
            raise HTTPException(status_code=400, detail="No record of this teacher")
        
        if teacher.user_id is not None:
            raise HTTPException(status_code=400, detail="User Id already exist")
        
        teacher.user_id = new_user.user_id
        #db.commit()
    
    else:
        return HTTPException(status_code=400, detail="Invalid role type")
    
    db.commit()
    
    return {"message": f"{data.role.capitalize()} data created succesfully"}
        


#TODO : Teacher and student login
@router.post("/login")
async def login(data: user_schema.UserLoginBase, db: DatabaseSession):
    username = data.user_name
    password = data.password
    
    user_info = db.query(user.User).filter(
        (user.User.user_name == username)&
        (user.User.password_hash==password)
    ).first()
    if user_info is None:
        raise HTTPException(status_code=400, detail="User not found")
    
    return {
        "message": f"User {user_info.user_name} has successfully logged in"
    }

