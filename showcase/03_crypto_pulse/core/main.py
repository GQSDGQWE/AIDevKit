"""
Showcase 03: Crypto Pulse - Async API
高并发异步价格模拟。

PLAN:
1. 使用 asyncio 模拟交易所数据。
2. 实现高性能 API。

EXECUTE:
"""

import asyncio
from fastapi import FastAPI
import random

app = FastAPI()

async def fetch_fake_price(symbol: str):
    await asyncio.sleep(random.uniform(0.01, 0.1)) # 模拟网络延迟
    return {"symbol": symbol, "price": 50000 + random.uniform(-100, 100)}

@app.get("/ticker/{symbol}")
async def get_ticker(symbol: str):
    return await fetch_fake_price(symbol.upper())

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8003)
