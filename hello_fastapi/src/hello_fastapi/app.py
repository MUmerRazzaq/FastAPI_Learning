from fastapi import FastAPI
from hello_fastapi.routes.todo_routes import todo_router

app = FastAPI()

# This connects your router to the app

# Optional root endpoint just for testing
@app.get("/")
def read_root():
    return {"message": "Hello from FastAPI"}

app.include_router(todo_router, prefix="/api", tags=["todo"])