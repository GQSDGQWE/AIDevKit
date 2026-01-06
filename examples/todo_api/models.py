"""
TODO API - Data Models / 数据模型定义

PLAN:
1. Define Task and User models with dataclasses
2. Add validation in __post_init__
3. Implement helper methods (to_dict, update_status)
4. Add self-tests (10 tests total)

EXECUTE:
"""

from datetime import datetime
from enum import Enum
from typing import Optional
from dataclasses import dataclass, field


class TaskStatus(Enum):
    """Task status enumeration"""
    TODO = "todo"
    IN_PROGRESS = "in_progress"
    DONE = "done"
    ARCHIVED = "archived"


class TaskPriority(Enum):
    """Task priority enumeration"""
    LOW = 1
    MEDIUM = 2
    HIGH = 3
    URGENT = 4


@dataclass
class Task:
    """
    Task model for TODO items
    
    Example:
        >>> task = Task(id=1, title="Learn Python", user_id=1)
        >>> task.status
        <TaskStatus.TODO: 'todo'>
    """
    id: int
    title: str
    user_id: int
    description: Optional[str] = None
    status: TaskStatus = TaskStatus.TODO
    priority: TaskPriority = TaskPriority.MEDIUM
    created_at: datetime = field(default_factory=datetime.now)
    updated_at: datetime = field(default_factory=datetime.now)
    due_date: Optional[datetime] = None
    
    def __post_init__(self):
        """Validate task data"""
        if not self.title or len(self.title.strip()) == 0:
            raise ValueError("Task title cannot be empty")
        if self.id < 0:
            raise ValueError("Task ID must be positive")
        if self.user_id < 0:
            raise ValueError("User ID must be positive")
    
    def update_status(self, new_status: TaskStatus) -> None:
        """Update task status and timestamp"""
        self.status = new_status
        self.updated_at = datetime.now()
    
    def is_overdue(self) -> bool:
        """Check if task is overdue"""
        if self.due_date is None:
            return False
        return datetime.now() > self.due_date
    
    def to_dict(self) -> dict:
        """Convert task to dictionary"""
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "status": self.status.value,
            "priority": self.priority.value,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
            "due_date": self.due_date.isoformat() if self.due_date else None,
            "user_id": self.user_id,
            "is_overdue": self.is_overdue()
        }
    
    def __repr__(self) -> str:
        return f"Task(id={self.id}, title='{self.title}', status={self.status.value})"


@dataclass
class User:
    """
    User model for task ownership
    
    Example:
        >>> user = User(id=1, username="alice", email="alice@example.com")
        >>> user.username
        'alice'
    """
    id: int
    username: str
    email: str
    created_at: datetime = field(default_factory=datetime.now)
    
    def __post_init__(self):
        """Validate user data"""
        if not self.username or len(self.username.strip()) == 0:
            raise ValueError("Username cannot be empty")
        if "@" not in self.email:
            raise ValueError("Invalid email format")
        if self.id < 0:
            raise ValueError("User ID must be positive")
    
    def to_dict(self) -> dict:
        """Convert user to dictionary"""
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
            "created_at": self.created_at.isoformat()
        }
    
    def __repr__(self) -> str:
        return f"User(id={self.id}, username='{self.username}')"


# Self-tests
if __name__ == "__main__":
    print("🧪 Running models.py self-tests...\n")
    
    # Test 1: Task creation with defaults
    task1 = Task(id=1, title="Write documentation", user_id=1)
    assert task1.status == TaskStatus.TODO and task1.priority == TaskPriority.MEDIUM
    print("✅ Test 1 passed: Task creation with defaults")
    
    # Test 2: Task with custom priority
    task2 = Task(id=2, title="Fix critical bug", user_id=1, priority=TaskPriority.URGENT)
    assert task2.priority == TaskPriority.URGENT
    print("✅ Test 2 passed: Task with custom priority")
    
    # Test 3: Task status update
    task2.update_status(TaskStatus.IN_PROGRESS)
    assert task2.status == TaskStatus.IN_PROGRESS
    print("✅ Test 3 passed: Task status update")
    
    # Test 4: Overdue detection
    past_date = datetime(2025, 1, 1)
    task3 = Task(id=3, title="Old task", user_id=1, due_date=past_date)
    assert task3.is_overdue() == True
    print("✅ Test 4 passed: Overdue detection")
    
    # Test 5: Task to dict conversion
    task_dict = task1.to_dict()
    assert "id" in task_dict and "title" in task_dict and task_dict["status"] == "todo"
    print("✅ Test 5 passed: Task to dict conversion")
    
    # Test 6: Empty title validation
    try:
        Task(id=4, title="", user_id=1)
        assert False, "Should raise ValueError"
    except ValueError:
        print("✅ Test 6 passed: Empty title validation")
    
    # Test 7: User creation
    user1 = User(id=1, username="alice", email="alice@example.com")
    assert user1.username == "alice"
    print("✅ Test 7 passed: User creation")
    
    # Test 8: Email validation
    try:
        User(id=2, username="bob", email="invalid-email")
        assert False, "Should raise ValueError"
    except ValueError:
        print("✅ Test 8 passed: Email validation")
    
    # Test 9: User to dict conversion
    user_dict = user1.to_dict()
    assert "username" in user_dict and user_dict["email"] == "alice@example.com"
    print("✅ Test 9 passed: User to dict conversion")
    
    # Test 10: Line count check
    with open(__file__, 'r', encoding='utf-8') as f:
        line_count = len(f.readlines())
    assert line_count < 500, f"File has {line_count} lines, must be < 500"
    print(f"✅ Test 10 passed: Line count ({line_count} lines < 500)")
    
    print(f"\n🎉 All 10 tests passed! models.py compliant with framework.")

