import os
import sys
from fastapi import FastAPI, Depends
from sqlmodel import SQLModel, Field, create_engine, Session, select
from typing import List, Optional
from contextlib import asynccontextmanager

# Aether Engine depends on Cognis Vault for its secrets
# This demonstrates real-world software supply chain and API-First interop

DATABASE_URL = "sqlite:///./aether_engine.db"
engine = create_engine(DATABASE_URL)

class Deployment(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    service_name: str
    status: str = "Idle"
    last_run: str = ""
    vault_record_id: int  # Link to Cognis Vault record ID

@asynccontextmanager
async def lifespan(app: FastAPI):
    SQLModel.metadata.create_all(engine)
    yield

app = FastAPI(title="Aether DevOps Engine API", lifespan=lifespan)

def get_session():
    with Session(engine) as session:
        yield session

@app.post("/deploy")
def trigger_deploy(service: str, vault_id: int, session: Session = Depends(get_session)):
    # In a real app, this would use the Cognis SDK to pull keys
    new_deploy = Deployment(service_name=service, status="Deploying", vault_record_id=vault_id)
    session.add(new_deploy)
    session.commit()
    return {"status": "triggered", "deployment_id": new_deploy.id}

@app.get("/status", response_model=List[Deployment])
def get_all_status(session: Session = Depends(get_session)):
    return session.exec(select(Deployment)).all()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=9000)
