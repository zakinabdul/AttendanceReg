from src.api.deps import DatabaseSession
from fastapi import APIRouter, Depends, HTTPException, status
from src.schemas import user_schema 
from src.db.models import user,classes
from src.core.logger import logger
router = APIRouter(
    prefix="/test",
   tags=["test"]
)

@router.get("/get_all_user")
async def get_users(db: DatabaseSession):
    users = db.query(user.User).all()
    return users

@router.get("/get_all_student")
async def get_users(db: DatabaseSession):
    users = db.query(user.Student).all()
    return users