#TODO Sudent attendance percentage view or current present count
from fastapi import APIRouter, HTTPException, status
from src.api.deps import DatabaseSession
from src.schemas import user_schema 
from src.db.models import attendance
from sqlalchemy import func
router = APIRouter(
    prefix="/student",
   tags=["student"]
)
@router.post("/student_attendance", status_code=status.HTTP_201_CREATED)
async def attendance_view(data: user_schema.StudentAttendanceBae, db: DatabaseSession):
    student_id = data.student_id
    
    present_count  = db.query(func.count(attendance.attendance_record.record_id)).filter(
        attendance.attendance_record.student_id==student_id
    ).scalar()

    return {
        "student_id": student_id,
        "present_days": present_count
    }
