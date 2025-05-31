from sqlalchemy import Column, Integer, String, Float, ForeignKey
from Config.db import Base

class MenuItem(Base):
    __tablename__ = 'menu_items'

    id = Column(Integer, primary_key=True, index=True)
    restaurant_id = Column(Integer, ForeignKey('restaurants.id'))
    name = Column(String)
    description = Column(String)
    price = Column(Float)
    available = Column(Integer, default=1) # 1-> True 0 -> False
    