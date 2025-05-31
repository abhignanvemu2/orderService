from sqlalchemy import Column, String, Integer
from Config.db import Base

class Student(Base):
    __tablename__ = "student"
    
    id   = Column(Integer, primary_key=True)
    name = Column(String)
    age  = Column(Integer)



