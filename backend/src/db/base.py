from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.orm import sessionmaker, declarative_base
from src.core.config import settings
from sqlalchemy.pool import NullPool
Base = declarative_base()

class DatabaseSettings:
    def __init__(self):
        self.SQLALCHEMY_DATABASE_URL = settings.DATABASE_URL

        # You can load this from environment variables
        
    def get_db_url(self):
        return self.SQLALCHEMY_DATABASE_URL

def get_engine():
    settings = DatabaseSettings()
    return create_engine(settings.get_db_url())

def get_async_engine():
    settings = DatabaseSettings()
    return create_async_engine(
        settings.get_db_url(),
        poolclass=NullPool
    )
    
#SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=get_async_engine())
AsyncSessionLocal = async_sessionmaker(
    bind=get_async_engine(),
    autoflush=False,
    autocommit=False,
    expire_on_commit=False,
    class_=AsyncSession
)