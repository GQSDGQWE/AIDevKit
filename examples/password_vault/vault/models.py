"""
Local Password Vault - Database Models
使用 SQLite 存储用户和加密的凭据。

PLAN:
1. 初始化 SQLite 数据库。
2. 创建用户表（存储哈希后的主密码和加密密钥）。
3. 创建记录表（存储加密后的账号密码）。
4. 提供基础的增删改查方法。

EXECUTE:
"""

import sqlite3
from pathlib import Path
from typing import List, Dict, Optional

DB_PATH = Path("vault_data.db")

class VaultDB:
    def __init__(self, db_path: str = str(DB_PATH)):
        self.conn = sqlite3.connect(db_path, check_same_thread=False)
        self.conn.row_factory = sqlite3.Row
        self._init_db()

    def _init_db(self):
        cursor = self.conn.cursor()
        # 用户表: id, username, hashed_master_password, encryption_key
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE,
            hashed_master_password TEXT,
            encryption_key TEXT
        )''')
        # 记录表: id, user_id, site_name, site_username, encrypted_password
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS entries (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            site_name TEXT,
            site_username TEXT,
            encrypted_password TEXT,
            FOREIGN KEY (user_id) REFERENCES users (id)
        )''')
        self.conn.commit()

    def create_user(self, username, hashed_pwd, enc_key):
        try:
            cursor = self.conn.cursor()
            cursor.execute("INSERT INTO users (username, hashed_master_password, encryption_key) VALUES (?, ?, ?)",
                         (username, hashed_pwd, enc_key))
            self.conn.commit()
            return cursor.lastrowid
        except sqlite3.IntegrityError:
            return None

    def get_user(self, username):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
        return cursor.fetchone()

    def add_entry(self, user_id, site, username, encrypted_pwd):
        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO entries (user_id, site_name, site_username, encrypted_password) VALUES (?, ?, ?, ?)",
                     (user_id, site, username, encrypted_pwd))
        self.conn.commit()
        return cursor.lastrowid

    def get_entries(self, user_id):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM entries WHERE user_id = ?", (user_id,))
        return cursor.fetchall()

    def close(self):
        self.conn.close()

# 单元测试
if __name__ == "__main__":
    print("🧪 测试数据库模型...")
    test_db = "test_vault.db"
    if Path(test_db).exists(): Path(test_db).unlink()
    
    db = VaultDB(test_db)
    uid = db.create_user("alice", "hash123", "key123")
    assert uid == 1
    
    user = db.get_user("alice")
    assert user["username"] == "alice"
    
    eid = db.add_entry(uid, "google.com", "alice@gmail.com", "enc_pwd_abc")
    assert eid == 1
    
    entries = db.get_entries(uid)
    assert len(entries) == 1
    assert entries[0]["site_name"] == "google.com"
    
    print("✅ 数据库增删改查测试通过")
    Path(test_db).unlink()
