"""
TODO API - Database Operations / 数据库操作层

PLAN:
1. Create SQLite database connection manager
2. Implement CRUD operations for Task
3. Implement CRUD operations for User
4. Add transaction support
5. Add self-tests (10 tests)

EXECUTE:
"""

import sqlite3
from typing import List, Optional
from contextlib import contextmanager
from models import Task, User, TaskStatus, TaskPriority
from datetime import datetime


class Database:
    """Database manager for TODO API"""
    
    def __init__(self, db_path: str = "todo.db"):
        """Initialize database connection"""
        self.db_path = db_path
        self.create_tables()
    
    @contextmanager
    def get_connection(self):
        """Context manager for database connection"""
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        try:
            yield conn
            conn.commit()
        except Exception as e:
            conn.rollback()
            raise e
        finally:
            conn.close()
    
    def create_tables(self) -> None:
        """Create database tables if not exist"""
        with self.get_connection() as conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT NOT NULL UNIQUE,
                    email TEXT NOT NULL UNIQUE,
                    created_at TEXT NOT NULL
                )
            """)
            conn.execute("""
                CREATE TABLE IF NOT EXISTS tasks (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT NOT NULL,
                    description TEXT,
                    status TEXT NOT NULL,
                    priority INTEGER NOT NULL,
                    created_at TEXT NOT NULL,
                    updated_at TEXT NOT NULL,
                    due_date TEXT,
                    user_id INTEGER NOT NULL,
                    FOREIGN KEY (user_id) REFERENCES users (id)
                )
            """)
    
    # User CRUD operations
    def create_user(self, username: str, email: str) -> User:
        """Create new user"""
        with self.get_connection() as conn:
            cursor = conn.execute(
                "INSERT INTO users (username, email, created_at) VALUES (?, ?, ?)",
                (username, email, datetime.now().isoformat())
            )
            user_id = cursor.lastrowid
            return User(id=user_id, username=username, email=email)
    
    def get_user(self, user_id: int) -> Optional[User]:
        """Get user by ID"""
        with self.get_connection() as conn:
            row = conn.execute("SELECT * FROM users WHERE id = ?", (user_id,)).fetchone()
            if row:
                return User(
                    id=row["id"],
                    username=row["username"],
                    email=row["email"],
                    created_at=datetime.fromisoformat(row["created_at"])
                )
            return None
    
    def get_all_users(self) -> List[User]:
        """Get all users"""
        with self.get_connection() as conn:
            rows = conn.execute("SELECT * FROM users").fetchall()
            return [User(
                id=row["id"],
                username=row["username"],
                email=row["email"],
                created_at=datetime.fromisoformat(row["created_at"])
            ) for row in rows]
    
    # Task CRUD operations
    def create_task(self, task: Task) -> Task:
        """Create new task"""
        with self.get_connection() as conn:
            cursor = conn.execute(
                """INSERT INTO tasks 
                   (title, description, status, priority, created_at, updated_at, due_date, user_id) 
                   VALUES (?, ?, ?, ?, ?, ?, ?, ?)""",
                (task.title, task.description, task.status.value, task.priority.value,
                 task.created_at.isoformat(), task.updated_at.isoformat(),
                 task.due_date.isoformat() if task.due_date else None, task.user_id)
            )
            task.id = cursor.lastrowid
            return task
    
    def get_task(self, task_id: int) -> Optional[Task]:
        """Get task by ID"""
        with self.get_connection() as conn:
            row = conn.execute("SELECT * FROM tasks WHERE id = ?", (task_id,)).fetchone()
            if row:
                return Task(
                    id=row["id"],
                    title=row["title"],
                    description=row["description"],
                    status=TaskStatus(row["status"]),
                    priority=TaskPriority(row["priority"]),
                    created_at=datetime.fromisoformat(row["created_at"]),
                    updated_at=datetime.fromisoformat(row["updated_at"]),
                    due_date=datetime.fromisoformat(row["due_date"]) if row["due_date"] else None,
                    user_id=row["user_id"]
                )
            return None
    
    def get_tasks_by_user(self, user_id: int) -> List[Task]:
        """Get all tasks for a user"""
        with self.get_connection() as conn:
            rows = conn.execute("SELECT * FROM tasks WHERE user_id = ?", (user_id,)).fetchall()
            return [Task(
                id=row["id"],
                title=row["title"],
                description=row["description"],
                status=TaskStatus(row["status"]),
                priority=TaskPriority(row["priority"]),
                created_at=datetime.fromisoformat(row["created_at"]),
                updated_at=datetime.fromisoformat(row["updated_at"]),
                due_date=datetime.fromisoformat(row["due_date"]) if row["due_date"] else None,
                user_id=row["user_id"]
            ) for row in rows]
    
    def update_task(self, task: Task) -> None:
        """Update existing task"""
        with self.get_connection() as conn:
            conn.execute(
                """UPDATE tasks SET title=?, description=?, status=?, priority=?, 
                   updated_at=?, due_date=? WHERE id=?""",
                (task.title, task.description, task.status.value, task.priority.value,
                 datetime.now().isoformat(),
                 task.due_date.isoformat() if task.due_date else None, task.id)
            )
    
    def delete_task(self, task_id: int) -> bool:
        """Delete task by ID"""
        with self.get_connection() as conn:
            cursor = conn.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
            return cursor.rowcount > 0


# Self-test
if __name__ == "__main__":
    print("Run: python test_database.py")

