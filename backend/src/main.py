from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .db.base import Base, get_async_engine    
from .api.v1.routers import api_router
@asynccontextmanager
async def lifespan(app: FastAPI):
    # --- STARTUP ---
    # We use a context manager to get a connection
    async with get_async_engine().begin() as conn:
        # run_sync allows the sync 'create_all' to work in the async world
        await conn.run_sync(Base.metadata.create_all)
    
    print("✅ Database tables created (if they didn't exist)")
    
    yield # The application runs here
    
    # --- SHUTDOWN ---
    # Properly close the connection pool
    await get_async_engine().dispose()
    print("🛑 Database connection pool disposed")
    
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
@app.get("/trieal")
def message():
    return {"message": "Go to docs endpoint"}



app.include_router(api_router, prefix="/api/v1")



#TODO API versioning

