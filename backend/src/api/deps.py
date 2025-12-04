from typing import AsyncGenerator, Annotated
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from src.db.base import AsyncSessionLocal

async def get_db() -> AsyncGenerator:
    async with AsyncSessionLocal() as session:
        yield session
            
DatabaseSession = Annotated[AsyncSession, Depends(get_db)]


"""def get_db() -> Generator:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()"""