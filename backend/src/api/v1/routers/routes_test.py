from src.api.deps import DatabaseSession
from fastapi import APIRouter, Depends, HTTPException, status
from src.schemas import user_schema 
from src.db.models import user,classes
from src.core.logger import logger
from sqlalchemy import select
router = APIRouter(
    prefix="/test",
   tags=["test"]
)

@router.get("/get_all_user")
async def get_all_users(db: DatabaseSession):
    query = select(user.User)
    result = await db.execute(query)
    users = result.scalars().all()
    return users

@router.get("/get_all_student")
async def get_all_students(db: DatabaseSession):
    query = select(user.Student)
    result = await db.execute(query)
    students = result.scalars().all()
    return students
