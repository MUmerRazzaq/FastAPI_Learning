from email import message
from pydantic import BaseModel,Field
from typing_extensions import Annotated


class TodoCreate(BaseModel):
    title : str
    description : str
    completed : bool = False


class UserCreate(BaseModel):
    name: Annotated[str, Field(min_length=3,max_length=50)]
    mail: Annotated[str, Field(pattern=r'^\S+@\S+$')]
    password: Annotated[str, Field(min_length=6)]


class UserLogin(BaseModel):
    mail: Annotated[str, Field(pattern=r'^\S+@\S+$')]
    password: Annotated[str, Field(min_length=6)]
