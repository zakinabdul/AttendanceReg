from src.api.v1.routers.routes_auth import router as auth_router
from src.api.v1.routers.routes_teacher import router as teacher_router
from src.api.v1.routers.routes_students import router as student_router
from src.api.v1.routers.routes_test import router as test_router
from fastapi import APIRouter


api_router = APIRouter()
api_router.include_router(auth_router)
api_router.include_router(teacher_router)
api_router.include_router(student_router)
api_router.include_router(test_router)



