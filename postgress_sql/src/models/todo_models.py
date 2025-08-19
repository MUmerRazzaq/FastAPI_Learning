from sqlalchemy import Column , Integer , String , Boolean, DateTime , ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from sqlalchemy.orm import relationship

Base = declarative_base()


class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key= True , index= True)
    name = Column (String , index=True , nullable=False)
    mail = Column(String, nullable= False, unique=True)
    password = Column (String , nullable= False)
    todos = relationship("Todos", back_populates="user", cascade="all, delete-orphan")

class Todos(Base):
    __tablename__ = "todos"
    id = Column(Integer, primary_key=True , index=True)
    title = Column(String , index=True , nullable= False)
    description = Column (String , nullable=True)
    status = Column (Boolean , default= False)
    created_at = Column (DateTime , default= datetime.now)
    user_id = Column(Integer , ForeignKey("users.id", ondelete="CASCADE"), nullable= False)
   
    user = relationship("Users", back_populates="todos")
