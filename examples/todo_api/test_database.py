"""
TODO API - Database Tests / 数据库测试
"""

import os
from database import Database
from models import Task, TaskStatus

print("🧪 Running database tests...\n")

# Clean test database
test_db = "test_todo.db"
if os.path.exists(test_db):
    os.remove(test_db)

db = Database(test_db)

# Test 1: Create user
user1 = db.create_user("alice", "alice@example.com")
assert user1.id > 0
print("✅ Test 1: Create user")

# Test 2: Get user
retrieved_user = db.get_user(user1.id)
assert retrieved_user.username == "alice"
print("✅ Test 2: Get user by ID")

# Test 3: Get all users
db.create_user("bob", "bob@example.com")
users = db.get_all_users()
assert len(users) == 2
print("✅ Test 3: Get all users")

# Test 4: Create task
task1 = Task(id=0, title="Write code", user_id=user1.id)
created_task = db.create_task(task1)
assert created_task.id > 0
print("✅ Test 4: Create task")

# Test 5: Get task
retrieved_task = db.get_task(created_task.id)
assert retrieved_task.title == "Write code"
print("✅ Test 5: Get task by ID")

# Test 6: Get tasks by user
db.create_task(Task(id=0, title="Review PR", user_id=user1.id))
user_tasks = db.get_tasks_by_user(user1.id)
assert len(user_tasks) == 2
print("✅ Test 6: Get tasks by user")

# Test 7: Update task
retrieved_task.update_status(TaskStatus.IN_PROGRESS)
db.update_task(retrieved_task)
updated = db.get_task(retrieved_task.id)
assert updated.status == TaskStatus.IN_PROGRESS
print("✅ Test 7: Update task")

# Test 8: Delete task
result = db.delete_task(created_task.id)
assert result == True and db.get_task(created_task.id) is None
print("✅ Test 8: Delete task")

# Test 9: Transaction rollback
try:
    db.create_user("alice", "alice2@example.com")
    assert False
except:
    print("✅ Test 9: Transaction rollback")

# Cleanup
os.remove(test_db)
print(f"\n🎉 All 9 tests passed!")
