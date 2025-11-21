from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .db.base import Base, get_engine    
from .api.v1.routers import api_router

#lifespan event handler
@asynccontextmanager
async def lifespan(app: FastAPI):
    #Startup code
    Base.metadata.create_all(bind= get_engine())
    yield
    #Shutdown code
    get_engine().dispose()

app=FastAPI(
    title="Attendance Reg",
    description="Backend service for attendance register full stack web app",
    lifespan=lifespan,
    version="1.0.0"
)
origins = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
    "http://localhost:8000",
    "http://127.0.0.1:8000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



@app.get("/")
def message():
    return {"message": "Go to docs endpoint"}

app.include_router(api_router, prefix="/api/v1")



#TODO API versioning

