"""
Markdown Doc Generator - Generator / 文档生成器
将扫描得到的元数据转换为 Markdown 表格和列表

PLAN:
1. Receive metadata from scanner
2. Render Markdown Template
3. Support local file export
4. Integrate with scanner for full-flow test
5. Maintain line count < 500

EXECUTE:
"""

import os
from pathlib import Path
from typing import List, Dict

class MarkdownRenderer:
    """Renders scanned metadata into markdown formats"""
    
    def __init__(self, metadata: List[Dict[str, str]]):
        self.metadata = metadata

    def to_table(self) -> str:
        """Generates a summary table"""
        rows = ["| File | Description |", "| :--- | :--- |"]
        for item in self.metadata:
            rows.append(f"| `{item['name']}` | {item['doc'].splitlines()[0]} |")
        return "\n".join(rows)

    def to_detail_list(self) -> str:
        """Generates a detailed list with paths"""
        lines = ["## Project Structure Details"]
        for item in self.metadata:
            lines.append(f"### {item['name']}")
            lines.append(f"- **Path**: `{item['path']}`")
            lines.append(f"- **Doc**:\n> {item['doc']}")
        return "\n".join(lines)

    def write_to_file(self, output_path: str):
        content = f"# Project Documentation\n\n{self.to_table()}\n\n{self.to_detail_list()}"
        Path(output_path).write_text(content, encoding='utf-8')
        return content

# Integration test
def run_integration_test():
    print("🧪 Running generator.py integration tests...")
    
    dummy_meta = [
        {"name": "auth.py", "path": "src/auth.py", "doc": "Handles user login and JWT."},
        {"name": "utils.py", "path": "src/utils.py", "doc": "Generic helpers."}
    ]
    
    renderer = MarkdownRenderer(dummy_meta)
    
    # Test 1: Table formatting
    table = renderer.to_table()
    assert "auth.py" in table
    assert "| :---" in table
    print("✅ Test 1: Table formatting")

    # Test 2: File export
    output_f = "test_doc.md"
    content = renderer.write_to_file(output_f)
    assert os.path.exists(output_f)
    assert "# Project Documentation" in content
    print("✅ Test 2: File export success")
    
    # Cleanup
    os.remove(output_f)

    # Line count check
    with open(__file__, 'r', encoding='utf-8') as f:
        line_count = len(f.readlines())
    assert line_count < 500
    print(f"✅ Test 3: Line count ({line_count} < 500)")

if __name__ == "__main__":
    run_integration_test()
    print("\n🎉 All generator.py tests passed!")
