from sqlalchemy import Column , Integer , String , Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class Todo(Base):
    __tablename__ = "todos"
    id = Column(Integer, primary_key=True , index=True)
    title = Column(String , index=True)
    description = Column (String , nullable=True)
    status = Column (Boolean , default= False)
    created_at = Column (DateTime , default= datetime.now)
    