"""
Local Password Vault - API Server
本地密码管理服务器主程序。

PLAN:
1. 实现用户注册与登录（JWT）。
2. 实现密码条目的增加与查询。
3. 重点：查询时使用用户的 encryption_key 实时解密。
4. 提供简单的自测逻辑验证全流程。

EXECUTE:
"""

from fastapi import FastAPI, HTTPException, Depends, Header
from pydantic import BaseModel
from typing import List, Optional
import uvicorn

# 内部模块导入
from vault.crypto import CryptoManager
from vault.models import VaultDB

app = FastAPI(title="Local Password Vault")
db = VaultDB()
crypto = CryptoManager()

# --- 架构模型 ---
class UserAuth(BaseModel):
    username: str
    password: str

class PasswordEntry(BaseModel):
    site_name: str
    site_username: str
    password: str

class EntryResponse(BaseModel):
    id: int
    site_name: str
    site_username: str
    password: str # 解密后的文明

# --- 辅助方法 ---
async def get_current_user(authorization: str = Header(...)):
    if not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Invalid token")
    token = authorization.split(" ")[1]
    try:
        # 简化版：直接从 JWT 提取 username 并查询数据库
        import jwt # 确保导入
        payload = jwt.decode(token, "local_vault_system_secret_key", algorithms=["HS256"])
        user = db.get_user(payload.get("sub"))
        if not user:
            raise HTTPException(status_code=401, detail="User not found")
        return user
    except Exception:
        raise HTTPException(status_code=401, detail="Could not validate credentials")

# --- 接口实现 ---

@app.post("/register")
def register(auth: UserAuth):
    hashed = crypto.hash_password(auth.password)
    enc_key = crypto.generate_encryption_key()
    uid = db.create_user(auth.username, hashed, enc_key)
    if not uid:
        raise HTTPException(status_code=400, detail="User already exists")
    return {"message": "User registered successfully", "user_id": uid}

@app.post("/login")
def login(auth: UserAuth):
    user = db.get_user(auth.username)
    if not user or not crypto.verify_password(auth.password, user["hashed_master_password"]):
        raise HTTPException(status_code=401, detail="Incorrect credentials")
    
    token = crypto.create_access_token({"sub": auth.username})
    return {"access_token": token, "token_type": "bearer"}

@app.post("/passwords")
def add_password(entry: PasswordEntry, user=Depends(get_current_user)):
    encrypted = crypto.encrypt_data(entry.password, user["encryption_key"])
    db.add_entry(user["id"], entry.site_name, entry.site_username, encrypted)
    return {"message": "Password saved safely"}

@app.get("/passwords", response_model=List[EntryResponse])
def list_passwords(user=Depends(get_current_user)):
    rows = db.get_entries(user["id"])
    results = []
    for r in rows:
        decrypted = crypto.decrypt_data(r["encrypted_password"], user["encryption_key"])
        results.append({
            "id": r["id"],
            "site_name": r["site_name"],
            "site_username": r["site_username"],
            "password": decrypted
        })
    return results

if __name__ == "__main__":
    print("🚀 Starting Local Password Vault on http://localhost:8000")
    uvicorn.run(app, host="127.0.0.1", port=8000)
