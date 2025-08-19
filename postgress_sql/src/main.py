from fastapi import FastAPI 
from routes import todo_routes , users_routes



app = FastAPI()

app.include_router(todo_routes.todo_router, prefix="/todo", tags= ['Todos'])
app.include_router(users_routes.user_route,prefix='/user', tags= ['Users'])