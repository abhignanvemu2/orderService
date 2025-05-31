from sqlalchemy import Column, Integer, Float, ForeignKey, DateTime
from sqlalchemy.sql import func
from Config.db import Base

class Rating(Base):
    __tablename__ = 'ratings'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    order_id = Column(Integer, ForeignKey('orders.id'))
    delivery_agent_id = Column(Integer, ForeignKey('delivery_agents.id'), nullable=True)
    restaurant_id = Column(Integer, ForeignKey('restaurants.id'))
    order_rating= Column(Float, nullable=True )
    restaurent_rating = Column(Float, nullable=True)
    created_at = Column(DateTime, default=func.now())
