from src.api.deps import DatabaseSession
from fastapi import APIRouter, Depends, HTTPException, status
from src.schemas import class_schema, user_schema, attendance_schema
from src.db.models import user,classes, attendance
from typing import List
from datetime import date, datetime
from sqlalchemy import update

router = APIRouter(
    prefix="/teacher",
   tags=["teacher"]
)

@router.post("/student_list", status_code=status.HTTP_201_CREATED, response_model=user_schema.StudentListResponse)
async def students_list(data: class_schema.ClassCreate, db: DatabaseSession):
    """
    {
     "department": "Computer Science and Engineering",
     "semester": 1,
     "section": "B"
    }
    """
    department = data.department
    semester = data.semester
    section = data.section
    
    query = select(classes.Class).where(
        (classes.Class.department == department)& 
        (classes.Class.semester == semester) &
        (classes.Class.section == section)
    )
    result = await db.execute(query)
    class_info = result.scalars().first()

    if not class_info:
        raise HTTPException(status_code=400, detail="No class for that info is available")
    
    class_id = class_info.class_id
    
    
    query= select(user.Student).where(
        user.Student.class_id ==class_id
    )
    result = await db.execute(query)
    students = result.scalars().all()
    # current date
    # to find the current period number
    current_timedate = datetime.now().time()
    
    query = select(attendance.period).filter(
        (attendance.period.start_time <=current_timedate)&
        (attendance.period.end_time>=current_timedate)
    )
    result = await db.execute(query)
    period_number = result.scalars().first()
    if period_number is None:
        raise HTTPException(status_code=400, detail="NO such period is found in the record")
    today = date.today()
    
    query = select(attendance.attendance_session).where(
        (attendance.attendance_session.session_date == today) &
        (attendance.attendance_session.period_id ==period_number.period_id)
    )
    result = await db.execute(query)
    session = result.scalars().first()
    if session is None:
        raise HTTPException(status_code=400, detail="The current session is not in reocrd")
    
    session_id_current = session.session_id
    
    return {
    "message": "Successfully loaded the list of students",
    "students": students,
    "session_id": session_id_current  }


@router.post("/attendance_record")
async def attendance_marking(data: List[attendance_schema.AttendanceRecordCreate], db: DatabaseSession):
    
    # 1. Safety Check: Handle empty data
    if not data:
        raise HTTPException(status_code=400, detail="No attendance records provided")

    # 2. Bulk Create Logic
    # We convert the incoming Pydantic data into Database Models
    records = [
        attendance.attendance_record(
            session_id=record.session_id,
            student_id=record.student_id,
            status="Present"
        )
        for record in data
    ]
    
    # 'add_all' is the standard way to queue multiple objects in AsyncSession
    db.add_all(records)

    # 3. Update the Session Status
    session_id = data[0].session_id    

    # CORRECT WAY TO UPDATE:
    # Use the 'update()' statement, not 'select().update()'
    stmt = (
        update(attendance.attendance_session)
        .where(attendance.attendance_session.session_id == session_id)
        .values(status=True) # or "Completed", depending on your DB column type
    )
    
    await db.execute(stmt)

    # 4. Final Commit
    # This saves the new records AND the update query all at once.
    await db.commit()

    return {"message": "All records for today added successfully"}
       
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