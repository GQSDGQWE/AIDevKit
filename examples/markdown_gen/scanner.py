"""
Markdown Doc Generator - Code Scanner / 代码扫描器
递归扫描代码库并提取文档信息

PLAN:
1. Implement Recursive scanner using pathlib
2. Use regex/ast to extract docstrings
3. Structure data for the generator
4. Implement self-tests on dummy files
5. Maintain line count < 500

EXECUTE:
"""

import os
import re
from pathlib import Path
from typing import List, Dict, Any

class CodeScanner:
    """Scans python files and extracts documentation"""
    
    def __init__(self, root_dir: str):
        self.root_dir = Path(root_dir)

    def scan_files(self, extension: str = ".py") -> List[Path]:
        """Recursively find files with given extension"""
        return list(self.root_dir.rglob(f"*{extension}"))

    def extract_docstring(self, file_path: Path) -> str:
        """Simple extraction of top-level docstring"""
        content = file_path.read_text(encoding='utf-8')
        # Matches content between triple quotes at start of file
        match = re.search(r'"""(.*?)"""', content, re.DOTALL)
        if match:
            return match.group(1).strip()
        return "No documentation found."

    def generate_metadata(self) -> List[Dict[str, str]]:
        """Scan project and return structured metadata"""
        files = self.scan_files()
        metadata = []
        for f in files:
            metadata.append({
                "name": f.name,
                "path": str(f.relative_to(self.root_dir)),
                "doc": self.extract_docstring(f)
            })
        return metadata

# Self-tests
def run_tests():
    print("🧪 Running scanner.py self-tests...")
    
    # Setup dummy environment
    test_dir = Path("test_repo_simulation")
    test_dir.mkdir(exist_ok=True)
    temp_file = test_dir / "sample.py"
    temp_file.write_text('"""\nSample Doc\n"""\nprint("hello")', encoding='utf-8')
    
    scanner = CodeScanner(str(test_dir))
    
    # Test 1: File discovery
    files = scanner.scan_files()
    assert len(files) >= 1
    assert any(f.name == "sample.py" for f in files)
    print("✅ Test 1: File discovery")
    
    # Test 2: Docstring extraction
    doc = scanner.extract_docstring(temp_file)
    assert doc == "Sample Doc"
    print("✅ Test 2: Docstring extraction")
    
    # Test 3: Metadata generation
    meta = scanner.generate_metadata()
    assert meta[0]["name"] == "sample.py"
    print("✅ Test 3: Metadata generation success")

    # Cleanup
    temp_file.unlink()
    test_dir.rmdir()

    # Line count check
    with open(__file__, 'r', encoding='utf-8') as f:
        line_count = len(f.readlines())
    assert line_count < 500
    print(f"✅ Test 4: Line count ({line_count} < 500)")

if __name__ == "__main__":
    run_tests()
    print("\n🎉 All scanner.py tests passed!")
