from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from Config.db import Base

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True)
    email = Column(String, unique=True)
    password_hash = Column(String)
    created_at = Column(DateTime, default=func.now())
