"""
Showcase 01: Todo Master Pro - API & Core
符合 API-First 规则。

PLAN:
1. 实现 FastAPI 后端。
2. 实现内存存储。
3. 提供 CRUD 接口。

EXECUTE:
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

class Todo(BaseModel):
    id: Optional[int] = None
    task: str
    completed: bool = False

todos = []
counter = 1

@app.post("/todos", response_model=Todo)
def create_todo(todo: Todo):
    global counter
    todo.id = counter
    todos.append(todo)
    counter += 1
    return todo

@app.get("/todos", response_model=List[Todo])
def get_todos():
    return todos

@app.put("/todos/{todo_id}")
def update_todo(todo_id: int, completed: bool):
    for t in todos:
        if t.id == todo_id:
            t.completed = completed
            return t
    raise HTTPException(status_code=404, detail="Todo not found")

@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int):
    global todos
    todos = [t for t in todos if t.id != todo_id]
    return {"message": "Deleted"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8001)
