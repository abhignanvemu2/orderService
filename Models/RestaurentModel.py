from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from Config.db import Base

class Restaurant(Base):
    __tablename__ = 'restaurants'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    description = Column(String)
    status = Column(Integer, default=1)  # 1 -> Online/ 0 -> offline
    created_at = Column(DateTime, default=func.now())
