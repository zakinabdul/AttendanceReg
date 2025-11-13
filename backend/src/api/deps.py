from typing import Generator, Annotated
from fastapi import Depends
from sqlalchemy.orm import Session
from src.db.base import SessionLocal

def get_db() -> Generator:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

DatabaseSession = Annotated[Session, Depends(get_db)]