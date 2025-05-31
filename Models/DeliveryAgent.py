from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from Config.db import Base

class DeliveryAgent(Base):
    __tablename__ = 'delivery_agents'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String, unique=True)
    phone = Column(String, unique=True, nullable=False)
    is_available = Column(Integer, default=1) # 1-> is_available 0 -> not_available
    created_at = Column(DateTime, default=func.now())
