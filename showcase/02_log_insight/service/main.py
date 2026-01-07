"""
Showcase 02: Log Insight - API
提供日志流接口。

PLAN:
1. 模拟日志生成。
2. 实现 API 端点导出日志。

EXECUTE:
"""

from fastapi import FastAPI
import random
import datetime

app = FastAPI()

LOG_TYPES = ["INFO", "WARN", "ERROR", "DEBUG"]

@app.get("/stream")
def get_log_stream(lines: int = 10):
    logs = []
    for _ in range(lines):
        ts = datetime.datetime.now().isoformat()
        lvl = random.choice(LOG_TYPES)
        msg = f"Event_{random.randint(100, 999)} triggered."
        logs.append(f"[{ts}] {lvl}: {msg}")
    return {"logs": logs}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8002)
