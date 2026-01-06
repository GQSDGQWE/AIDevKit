"""
Log Analyzer - Parser Module / 日志解析器模块

PLAN:
1. Read log files with UTF-8 encoding
2. Parse common log formats (Apache/Nginx/Custom)
3. Extract timestamp, IP, method, URL, status, response_time
4. Handle malformed lines gracefully
5. Performance: >10,000 lines/sec

EXECUTE:
"""

import re
from typing import List, Dict, Optional
from datetime import datetime
from dataclasses import dataclass


@dataclass
class LogEntry:
    """Represents a single log entry"""
    timestamp: datetime
    level: str
    ip: str
    method: str
    url: str
    status: int
    response_time: int  # milliseconds
    raw_line: str
    
    def to_dict(self) -> dict:
        """Convert to dictionary"""
        return {
            "timestamp": self.timestamp.isoformat(),
            "level": self.level,
            "ip": self.ip,
            "method": self.method,
            "url": self.url,
            "status": self.status,
            "response_time": self.response_time
        }


class LogParser:
    """Parse log files and extract structured data"""
    
    # Pattern: 2026-01-07 10:23:45 - INFO - 192.168.1.100 - GET /api/users - 200 - 45ms
    PATTERN = re.compile(
        r'(\d{4}-\d{2}-\d{2}\s+\d{2}:\d{2}:\d{2})\s+-\s+(\w+)\s+-\s+'
        r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+-\s+'
        r'(GET|POST|PUT|DELETE|PATCH)\s+([^\s]+)\s+-\s+'
        r'(\d{3})\s+-\s+(\d+)ms'
    )
    
    def __init__(self):
        """Initialize parser"""
        self.parsed_count = 0
        self.error_count = 0
    
    def parse_line(self, line: str) -> Optional[LogEntry]:
        """
        Parse single log line
        
        Args:
            line: Raw log line
        
        Returns:
            LogEntry if successful, None if malformed
        """
        match = self.PATTERN.match(line.strip())
        if not match:
            self.error_count += 1
            return None
        
        try:
            timestamp = datetime.strptime(match.group(1), '%Y-%m-%d %H:%M:%S')
            level = match.group(2)
            ip = match.group(3)
            method = match.group(4)
            url = match.group(5)
            status = int(match.group(6))
            response_time = int(match.group(7))
            
            self.parsed_count += 1
            return LogEntry(timestamp, level, ip, method, url, status, response_time, line)
        except (ValueError, IndexError):
            self.error_count += 1
            return None
    
    def parse_file(self, file_path: str) -> List[LogEntry]:
        """
        Parse entire log file
        
        Args:
            file_path: Path to log file
        
        Returns:
            List of parsed log entries
        """
        entries = []
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                entry = self.parse_line(line)
                if entry:
                    entries.append(entry)
        return entries
    
    def get_stats(self) -> Dict[str, int]:
        """Get parsing statistics"""
        return {
            "parsed": self.parsed_count,
            "errors": self.error_count,
            "total": self.parsed_count + self.error_count,
            "success_rate": round(self.parsed_count / (self.parsed_count + self.error_count) * 100, 2) if self.parsed_count + self.error_count > 0 else 0
        }


# Self-tests
if __name__ == "__main__":
    import os, time
    
    print("🧪 Running parser.py self-tests...\n")
    
    # Create sample log
    sample_log = "test_sample.log"
    with open(sample_log, 'w', encoding='utf-8') as f:
        f.write("2026-01-07 10:23:45 - INFO - 192.168.1.100 - GET /api/users - 200 - 45ms\n")
        f.write("2026-01-07 10:24:12 - ERROR - 192.168.1.101 - POST /api/login - 401 - 12ms\n")
        f.write("Invalid log line\n")
        f.write("2026-01-07 10:26:00 - INFO - 192.168.1.100 - PUT /api/users/1 - 200 - 30ms\n")
    print("✅ Test 1: Sample log created")
    
    # Parse single line
    parser = LogParser()
    entry = parser.parse_line("2026-01-07 10:23:45 - INFO - 192.168.1.100 - GET /api/users - 200 - 45ms")
    assert entry and entry.status == 200
    print("✅ Test 2: Parse valid line")
    
    # Handle malformed line
    assert parser.parse_line("Invalid") is None
    print("✅ Test 3: Handle malformed")
    
    # Parse file
    parser2 = LogParser()
    entries = parser2.parse_file(sample_log)
    assert len(entries) == 3
    print(f"✅ Test 4: Parse file ({len(entries)} entries)")
    
    # Statistics
    stats = parser2.get_stats()
    assert stats["parsed"] == 3 and stats["errors"] == 1
    print(f"✅ Test 5: Stats ({stats['success_rate']}%)")
    
    # Extract fields
    assert entries[0].timestamp.year == 2026 and entries[0].ip == "192.168.1.100"
    print("✅ Test 6: Extract fields")
    
    # to_dict
    entry_dict = entries[0].to_dict()
    assert "timestamp" in entry_dict and "status" in entry_dict
    print("✅ Test 7: to_dict conversion")
    
    # Performance test
    perf_log = "test_perf.log"
    with open(perf_log, 'w', encoding='utf-8') as f:
        line = "2026-01-07 10:23:45 - INFO - 192.168.1.100 - GET /api/test - 200 - 10ms\n"
        for _ in range(10000):
            f.write(line)
    
    start = time.time()
    parser3 = LogParser()
    parser3.parse_file(perf_log)
    lines_per_sec = 10000 / (time.time() - start)
    assert lines_per_sec > 10000
    print(f"✅ Test 8: Performance ({int(lines_per_sec):,} lines/sec)")
    
    # Line count
    with open(__file__, 'r', encoding='utf-8') as f:
        line_count = len(f.readlines())
    assert line_count < 500
    print(f"✅ Test 9: Line count ({line_count} < 500)")
    
    # Cleanup
    os.remove(sample_log)
    os.remove(perf_log)
    print(f"\n🎉 All 9 tests passed! parser.py compliant.")

