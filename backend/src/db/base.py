from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from src.core.config import settings
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

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=get_engine())
