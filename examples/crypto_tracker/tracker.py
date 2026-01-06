"""
Crypto Price Tracker - Core logic / 核心逻辑
使用异步编程获取加密货币实时价格

PLAN:
1. Define CryptoClient class for API interaction
2. Implement async fetch for multiple coins (BTC, ETH, etc.)
3. Add caching mechanism locally
4. Implement self-tests/benchmarks
5. Maintain line count < 500

EXECUTE:
"""

import asyncio
import json
import time
from datetime import datetime
from typing import List, Dict, Any, Optional

# Mocking external API for environment independence
# In real scenario, use: import httpx

class CryptoTracker:
    """Track cryptocurrency prices using async logic"""
    
    def __init__(self, currency: str = "usd"):
        self.currency = currency
        self._cache: Dict[str, Dict[str, Any]] = {}

    async def fetch_price(self, coin_id: str) -> Dict[str, Any]:
        """
        Simulate fetching price from and API (e.g. CoinGecko)
        In production: response = await client.get(url)
        """
        # Simulation of network latency
        await asyncio.sleep(0.1)
        
        # Mocking data
        mock_prices = {
            "bitcoin": 45000.5 + (time.time() % 100),
            "ethereum": 2500.2 + (time.time() % 50),
            "solana": 100.8 + (time.time() % 10)
        }
        
        price = mock_prices.get(coin_id, 0.0)
        data = {
            "id": coin_id,
            "price": price,
            "currency": self.currency,
            "timestamp": datetime.now().isoformat()
        }
        self._cache[coin_id] = data
        return data

    async def track_multiple(self, coin_ids: List[str]) -> List[Dict[str, Any]]:
        """Fetch multiple coin prices concurrently"""
        tasks = [self.fetch_price(cid) for cid in coin_ids]
        return await asyncio.gather(*tasks)

    def get_cached_result(self, coin_id: str) -> Optional[Dict[str, Any]]:
        """Retrieve result from local cache"""
        return self._cache.get(coin_id)


# Self-tests and Performance Benchmark
async def run_tests():
    print("🧪 Running tracker.py self-tests...")
    tracker = CryptoTracker()
    
    # Test 1: Fetch single coin
    print("Test 1: Fetching BTC...")
    btc = await tracker.fetch_price("bitcoin")
    assert btc["id"] == "bitcoin"
    assert btc["price"] > 0
    print("✅ Test 1 passed")
    
    # Test 2: Fetch multiple concurrently
    print("Test 2: Concurrency check...")
    coins = ["bitcoin", "ethereum", "solana"]
    start = time.time()
    results = await tracker.track_multiple(coins)
    duration = time.time() - start
    
    assert len(results) == 3
    # Duration should be close to 0.1s due to concurrency, not 0.3s
    assert duration < 0.2
    print(f"✅ Test 2 passed (Duration: {duration:.3f}s)")
    
    # Test 3: Cache verification
    print("Test 3: Cache check...")
    cached = tracker.get_cached_result("ethereum")
    assert cached["id"] == "ethereum"
    print("✅ Test 3 passed")

    # Line count check
    with open(__file__, 'r', encoding='utf-8') as f:
        line_count = len(f.readlines())
    assert line_count < 500
    print(f"✅ Test 4 passed: Line count ({line_count} < 500)")
    
    print("\n🎉 All tracker.py tests passed!")

if __name__ == "__main__":
    asyncio.run(run_tests())
