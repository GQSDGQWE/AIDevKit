"""
Showcase 04: Container Auth - API
容器化网关与健康检测。

PLAN:
1. 实现带有 /health 接口的 FastAPI。
2. 配置 Dockerfile (PLAN-EXECUTE 风格)。

EXECUTE:
"""

from fastapi import FastAPI
import os

app = FastAPI()

@app.get("/")
def home():
    return {"status": "Container Running", "env": os.getenv("STAGE", "dev")}

@app.get("/health")
def health():
    return {"status": "healthy"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8004)
