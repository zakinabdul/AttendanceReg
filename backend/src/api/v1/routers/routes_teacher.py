from src.api.deps import DatabaseSession
from fastapi import APIRouter, Depends, HTTPException, status
from src.schemas import class_schema, user_schema, attendance_schema
from src.db.models import user,classes, attendance
from typing import List
from datetime import date, datetime
router = APIRouter(
    prefix="/teacher",
   tags=["teacher"]
)

@router.post("/student_list", status_code=status.HTTP_201_CREATED)
async def students_list(data: class_schema.ClassCreate, db: DatabaseSession):
    department = data.department
    semester = data.semester
    section = data.section
    
    class_info = db.query(classes.Class).filter(
        (classes.Class.department == department)& 
        (classes.Class.semester == semester) &
        (classes.Class.section == section)
    ).first()

    if not class_info:
        raise HTTPException(status_code=400, detail="No class for that info is available")
    
    class_id = class_info.class_id
    students = db.query(user.Student).filter(
        user.Student.class_id ==class_id
    ).all()
    
    # current date
    # to find the current period number
    current_timedate = datetime.now().time()
    period_number = db.query(attendance.period).filter(
        (attendance.period.start_time <=current_timedate)&
        (attendance.period.end_time>=current_timedate)
    ).first()
    
    if period_number is None:
        raise HTTPException(status_code=400, detail="NO such period is found in the record")
    today = date.today()
    session = db.query(attendance.attendance_session).filter(
        (attendance.attendance_session.session_date == today) &
        (attendance.attendance_session.period_id ==period_number.period_id)
    ).first()
    
    if session is None:
        raise HTTPException(status_code=400, detail="The current session is not in reocrd")
    
    session_id_current = session.session_id
    
    return {
    "message": "Successfully loaded the list of students",
    "students": students,
    "session_id": session_id_current  }

@router.post("/attendance_record")
async def attendance_marking(data: List[attendance_schema.AttendanceRecordCreate], db: DatabaseSession):

    records = [
        attendance.attendance_record(
            session_id = record.session_id,
            student_id = record.student_id,
            status = "Present"
        )
        for record in data
    ]
    db.bulk_save_objects(records)

    session_id = data[0].session_id    

    db.query(attendance.attendance_session).filter(
        attendance.attendance_session.session_id == session_id
    ).update({"status": True}, synchronize_session=False)

    db.commit()

    return {"message": "All record of today is added succefully"}

       
"""
@router.put("/session_complete/{session_id}")
async def complete_session(session_id: int, db: DatabaseSession):
    updated_rows = db.query(attendance.AttendanceSession).filter(
        attendance.AttendanceSession.session_id == session_id
    ).update(
        {"status": True},
        synchronize_session=False
    )
    db.commit()

    if updated_rows == 0:
        raise HTTPException(404, "Session not found")

    return {"message": "Session marked as completed"}

"""        
#TODO: In V2 change into async version
#TODO: Need to find a way to add absenties to the record [optional]