from fastapi import FastAPI , Depends , HTTPException
from models.todo_models import Todo
from config.database import SessionLocal ,engine
from sqlalchemy.orm import Session
from pydantic import BaseModel

# Todo.metadata.create_all(bind=engine)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

app = FastAPI()

class TodoCreate(BaseModel):
    title : str
    description : str

class TodoResponse(BaseModel):
    id : int 
    class Config:
        from_attributes = True

@app.post("/create_todo/")
def create_todo( todo : TodoCreate , db: Session = Depends(get_db) ):
    try:
        todo_data = Todo(title = todo.title , description = todo.description)
        db.add(todo_data)
        db.commit()
        db.refresh(todo_data)
    except Exception as e:
        return f"An error {e} "
    return todo_data

@app.get("/{todo_id}")
def get_todo(todo_id : int , db : Session = Depends(get_db)):
    try:
        todo = db.query(Todo).filter(Todo.id==todo_id).first()
        if not todo:
            raise HTTPException (status_code=404, detail="todo not found")
        return {
            "data": todo,
            "massage": "todo fetched",
            "status": "success"
        }
    except Exception as e:
        return {
            "massage" : f"error == {e}"
        }

    
    


