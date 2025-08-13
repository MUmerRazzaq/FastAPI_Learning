from fastapi import HTTPException
from hello_fastapi.db.todo_db import todo_db
def todo_check(todo_id:int):
    try:
        if todo_id >= len(todo_db) or todo_id < 0:
            raise HTTPException(status_code=404, detail="Todo item not found")
        # return {"todo_id": todo_id, "todo": todo_db[todo_id]}
        return {"todo_id": todo_id, "todo": todo_db[todo_id]}  # ✅ correct

    except Exception as e:
        return {"error": str(e)}



def get_next_id():
    if not todo_db:
        return 0
    return max(todo["id"] for todo in todo_db) + 1
