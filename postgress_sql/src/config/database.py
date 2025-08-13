import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv 

load_dotenv()

db_uri = os.getenv("DATABASE_URI")



engine = create_engine(db_uri)

SessionLocal = sessionmaker(autocommit = False , autoflush= False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()