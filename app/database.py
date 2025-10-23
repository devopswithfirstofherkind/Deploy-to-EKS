# app/database.py
from typing import Dict
from uuid import uuid4

# In-memory database
tasks: Dict[str, dict] = {}

def create_task(title: str, description: str):
    task_id = str(uuid4())
    tasks[task_id] = {
        "id": task_id,
        "title": title,
        "description": description,
        "completed": False
    }
    return tasks[task_id]

def get_tasks():
    return list(tasks.values())

def update_task(task_id: str, title: str = None, description: str = None, completed: bool = None):
    if task_id not in tasks:
        return None
    if title is not None:
        tasks[task_id]["title"] = title
    if description is not None:
        tasks[task_id]["description"] = description
    if completed is not None:
        tasks[task_id]["completed"] = completed
    return tasks[task_id]

def delete_task(task_id: str):
    return tasks.pop(task_id, None)
