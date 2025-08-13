from fastapi import APIRouter, HTTPException
from hello_fastapi.db.todo_db import todo_db
from hello_fastapi.utilities.todo_utilities import todo_check, get_next_id
from pydantic import BaseModel

class TodoItem(BaseModel):
    id: int 
    title: str
    description: str
    completed: bool 

todo_router = APIRouter()

@todo_router.get("/todo")
def read_todo():
    if not todo_db:
        raise HTTPException(status_code=404, detail="Todo list is empty")
    return {"todo_list": todo_db}

@todo_router.get("/todo/{todo_id}")
def read_todo_item(todo_id: int):
    todo = todo_check(todo_id)
    if "error" in todo:
        raise HTTPException(status_code=404, detail=todo["error"])
    return {"todo": todo["todo"]}


@todo_router.post("/todo")
def create_todo(todo: TodoItem):
    try:
        if not todo.title or not todo.description:
            raise HTTPException(status_code=400, detail="Title and description are required")
        if todo.completed is None:
            todo.completed = False
        todo.id = get_next_id()
        todo_db.append(todo.dict())
        return {"message": "Todo item created successfully", "todo": todo}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@todo_router.put("/todo")
def update_todo( todo: TodoItem):
    try:
        existing_todo = todo_check(todo.id)
        if "error" in existing_todo:
            raise HTTPException(status_code=404, detail=existing_todo["error"])
        todo_db[todo.id] = todo.dict()
        return {"message": f"Todo item {todo.id} updated successfully", "todo": todo}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    

@todo_router.delete("/todo/{todo_id}")
def delete_todo(todo_id: int):
    try:
        todo = todo_check(todo_id)
        if "error" in todo:
            raise HTTPException(status_code=404, detail=todo["error"])
        todo_db.pop(todo_id)
        return {"message": f"Todo item {todo_id} deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))























# from fastapi import APIRouter

# from ..db.todo_db import todo_db
# from fastapi import HTTPException
# from ..utilities.todo_utilities import todo_check, get_next_id
# todo_router = APIRouter()


# todo_router.get("/todo")
# def read_todo():
#     try:
#         if not todo_db:
#             raise HTTPException(status_code=404, detail="Todo list is empty")
#         return {"todo_list": todo_db, "message": "Todo list retrieved successfully"}
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))



# todo_router.get("/todo/{todo_id}")
# def read_todo_item(todo_id: int):
#     try:
#         todo = todo_check(todo_id)
#         if "error" in todo:
#             raise HTTPException(status_code=404, detail=todo["error"])
#         return {"message": f"Todo item {todo_id} retrieved successfully", "todo": todo["todo"]}
#     except Exception as e:
#         return {"error": str(e)}



# todo_router.post("/todo")
# def create_todo(todo: dict):
#     return {"message": "Todo item created successfully", "todo": todo}


# todo_router.put("/todo/{todo_id}")
# def update_todo(todo_id: int, todo: dict):
#     return {"message": f"Todo item {todo_id} updated successfully", "todo": todo}


# todo_router.delete("/todo/{todo_id}")  
# def delete_todo(todo_id: int):
#     return {"message": f"Todo item {todo_id} deleted successfully"}



