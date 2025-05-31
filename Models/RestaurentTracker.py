from sqlalchemy import Column, Integer, ForeignKey, DateTime
from sqlalchemy.sql import func
from Config.db import Base

class Restaurent_tracker(Base):
    __tablename__ = 'restaurent_tracker'

    id = Column(Integer, primary_key=True, index=True)
    restaurant_id = Column(Integer, ForeignKey("restaurants.id"))
    is_online = Column(Integer)  # 1 -> Online, 0 -> Offline
    online_time = Column(DateTime, nullable=True)
    offline_time = Column(DateTime, nullable=True)
    created_at = Column(DateTime, default=func.now())
