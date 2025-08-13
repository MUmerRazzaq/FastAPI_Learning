from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class User(BaseModel):
    username: str
    password: str
    email: Optional[str] = None
    full_name: Optional[str] = None

user_info = {  "admin": "password" }


@app.get("/")
def read_root():
    return {"massage": "Connected to FastAPI",
            "status": "ok"}  




@app.get("/login/{username}/{password}")
def login(username: str, password: str):
    try :
        # Simulate a login process
        if username != "admin" or password != "password":
            raise ValueError("Invalid credentials")
        return {"message": "Login successful", "username": username , "Status": "ok"}
    except Exception as e:
        return {"error": str(e)}
    

@app.get("/search")
def search(query: str):
    try:
        # Simulate a search process
        if not query:
            raise ValueError("Query cannot be empty")
        return {"message": "Search successful", "query": query, "status": "ok"}
    except Exception as e:
        return {"error": str(e)}
    

@app.post("/signup")
def signup(user: User):
    try:
        # Simulate a signup process
        if not user.username or not user.password:
            raise ValueError("Username and password are required")
        return {"message": "Signup successful", "user": user, "status": "ok"}
    except Exception as e:
        return {"error": str(e)}


@app.post("/user/{username}")
def user(username: str, user: User, query:str):
    try:
        if not username:
            raise ValueError("Username cannot be empty")
        elif username not in user_info:
            raise ValueError("User not found")
        elif user.password != user_info[username]:
            raise ValueError("Invalid password")
        elif not query:
            raise ValueError("Query cannot be empty")
        return {"message": "User found", "username": username, "query": query, "status": "ok"}
    except Exception as e:
        return {"error": str(e)}