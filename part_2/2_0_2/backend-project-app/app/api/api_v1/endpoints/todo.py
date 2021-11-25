from fastapi import APIRouter
from app.db.todo_in_memory import fake_todo
from app.schemas.todo import Todo
router = APIRouter()

@router.get("/todos/")
async def get_todos():
    return fake_todo 

@router.post("/todos/")
async def create_todos(todo: Todo):
    fake_todo.append(todo)
    return todo

