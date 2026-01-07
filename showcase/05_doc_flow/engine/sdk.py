"""
Showcase 05: DocFlow Scanner - Engine SDK
文件扫描与 Markdown 提取。

PLAN:
1. 实现 Scanner 类。
2. 支持导出 JSON API 格式。

EXECUTE:
"""

import os
from pathlib import Path

class DocEngine:
    def __init__(self, target_dir):
        self.target_dir = Path(target_dir)

    def scan(self):
        results = []
        for p in self.target_dir.rglob("*.py"):
            results.append({
                "file": p.name,
                "size": p.stat().st_size,
                "path": str(p)
            })
        return results

if __name__ == "__main__":
    eng = DocEngine(".")
    print(eng.scan())
