# app/main.py
from fastapi import FastAPI, HTTPException
from app.models import TaskCreate, TaskUpdate
from app.database import create_task, get_tasks, update_task, delete_task

app = FastAPI(title="Task API")

@app.post("/tasks")
def create(task: TaskCreate):
    return create_task(task.title, task.description)

@app.get("/tasks")
def read_tasks():
    return get_tasks()

@app.put("/tasks/{task_id}")
def update(task_id: str, task: TaskUpdate):
    updated = update_task(task_id, task.title, task.description, task.completed)
    if not updated:
        raise HTTPException(status_code=404, detail="Task not found")
    return updated

@app.delete("/tasks/{task_id}")
def delete(task_id: str):
    deleted = delete_task(task_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Task not found")
    return {"message": "Task deleted successfully"}
