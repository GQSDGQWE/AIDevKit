import os
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlmodel import Session, create_engine, select, SQLModel
from typing import List
from contextlib import asynccontextmanager
from .models import User, VaultRecord, AuditLog
from .security import verify_password, get_password_hash, create_access_token, SECRET_KEY, ALGORITHM
from jose import jwt, JWTError

# Database Setup
DATABASE_URL = "sqlite:///./cognis_vault.db"
engine = create_engine(DATABASE_URL)

@asynccontextmanager
async def lifespan(app: FastAPI):
    SQLModel.metadata.create_all(engine)
    yield

app = FastAPI(title="Cognis Vault Pro API", version="1.0.0", lifespan=lifespan)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def get_session():
    with Session(engine) as session:
        yield session

# Auth Endpoints
@app.post("/register")
async def register(user: User, session: Session = Depends(get_session)):
    user.hashed_password = get_password_hash(user.hashed_password)
    session.add(user)
    session.commit()
    session.refresh(user)
    return {"status": "success", "username": user.username}

@app.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends(), session: Session = Depends(get_session)):
    statement = select(User).where(User.username == form_data.username)
    user = session.exec(statement).first()
    if not user or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    
    access_token = create_access_token(data={"sub": user.username, "id": user.id})
    return {"access_token": access_token, "token_type": "bearer"}

async def get_current_user(token: str = Depends(oauth2_scheme), session: Session = Depends(get_session)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None: raise HTTPException(status_code=401)
    except JWTError: raise HTTPException(status_code=401)
    
    user = session.exec(select(User).where(User.username == username)).first()
    if user is None: raise HTTPException(status_code=401)
    return user

# Vault Endpoints
@app.post("/records", response_model=VaultRecord)
async def create_record(record: VaultRecord, current_user: User = Depends(get_current_user), session: Session = Depends(get_session)):
    record.owner_id = current_user.id
    session.add(record)
    
    # Audit logging
    log = AuditLog(user_id=current_user.id, action=f"CREATE_RECORD: {record.title}")
    session.add(log)
    
    session.commit()
    session.refresh(record)
    return record

@app.get("/records", response_model=List[VaultRecord])
async def list_records(current_user: User = Depends(get_current_user), session: Session = Depends(get_session)):
    return session.exec(select(VaultRecord).where(VaultRecord.owner_id == current_user.id)).all()

@app.get("/audit", response_model=List[AuditLog])
async def get_audit_logs(current_user: User = Depends(get_current_user), session: Session = Depends(get_session)):
    return session.exec(select(AuditLog).where(AuditLog.user_id == current_user.id)).all()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8888)
