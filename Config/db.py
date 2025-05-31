import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative  import declarative_base

load_dotenv()

DB_URL= os.getenv("DATABASE_URL").replace("+asyncpg", "")

engine = create_engine(DB_URL, echo=True)

SessionLocal = sessionmaker(bind= engine)

Base = declarative_base()


