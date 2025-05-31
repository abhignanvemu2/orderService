from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from Config.db import Base

class Order(Base):
    __tablename__ = 'orders'  

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    restaurant_id = Column(Integer, ForeignKey('restaurants.id'))
    item_id = Column(Integer, ForeignKey('menu_items.id'))
    delivery_agent_id = Column(Integer, ForeignKey('delivery_agents.id'), nullable=True)
    status = Column(Integer, default=1)  #1-> accepted, 2-> rejected, 0-> pending, 4-> delivered
    delivery_status = Column(Integer, default=0)  #0-> not_assigned, 1-> assigned,2-> picked_up, 3-> delivered
    created_at = Column(DateTime, default=func.now())
