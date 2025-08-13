from fastapi import FastAPI
from pydantic import BaseModel , Field
from typing import Optional, List





app = FastAPI()

class Student(BaseModel):
    id: int
    name: str
    age: int
    email: str
    phone: Optional[str] = None
    courses: List[str] = Field(default_factory=list)
    address: Optional[str] = None
    is_active: bool = True

student_db = {}

@app.get("/")
def read_root():
    return {"massage": "connection success"}



@app.post("/student/signup")
def signup_student(student: Student):
    try:
        student_db[student.id]
        if student.id in student_db:
            return {"message": "Student already exists"}
        student_db[student.id] = student
        return {"message": "Student signed up successfully", "student": student}
    except Exception as e:
        return {"error": str(e)}