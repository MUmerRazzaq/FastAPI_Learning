from fastapi import APIRouter , Depends , HTTPException
from models.todo_models import Todos
from config.database import  get_db
from sqlalchemy.orm import Session
from validations.validation import TodoCreate



todo_router = APIRouter()

@todo_router.post("/create/{user_id}")
def create_todo( user_id : int ,todo : TodoCreate , db: Session = Depends(get_db)):
    try:
        todo_data = Todos(title = todo.title , description = todo.description , user_id = user_id )
        db.add(todo_data)
        db.commit()
        db.refresh(todo_data)
    except Exception as e:
        db.rollback()
        return {
            'error' : str(e),
            'massage' : 'Error',
            'status': 'failed'
        }
    return {
            "data": todo,
            "massage": "todo Created",
            "status": "success"
        }

@todo_router.get("/{todo_id}")
def get_todo(todo_id : int , db : Session = Depends(get_db)):
    try:
        todo = db.query(Todos).filter(Todos.id==todo_id).first()
        if not todo:
            raise HTTPException (status_code=404, detail="todo not found")
        return {
            "data": todo,
            "massage": "todo fetched",
            "status": "success"
        }
    except Exception as e:
        return {
            'error' : e,
            'massage' : 'Error',
            'status' : 'failed'
        }