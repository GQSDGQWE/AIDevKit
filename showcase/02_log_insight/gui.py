"""
Showcase 02: Log Insight - Dashboard GUI

PLAN:
1. 实现带有色彩标记的日志查看器。
2. 实时请求 API 获取更新。

EXECUTE:
"""

import sys
import requests
from PySide6.QtWidgets import (QApplication, QMainWindow, QTextEdit, QVBoxLayout, 
                             QWidget, QPushButton)
from PySide6.QtCore import QTimer

class LogDashboard(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("📊 Log Insight Dashboard")
        self.resize(600, 400)
        
        container = QWidget()
        layout = QVBoxLayout(container)
        
        self.browser = QTextEdit()
        self.browser.setReadOnly(True)
        self.browser.setStyleSheet("background-color: #1e1e1e; color: #d4d4d4; font-family: Consolas;")
        
        self.btn = QPushButton("Start/Stop Real-time Monitor")
        self.btn.clicked.connect(self.toggle_timer)
        
        layout.addWidget(self.browser)
        layout.addWidget(self.btn)
        self.setCentralWidget(container)
        
        self.timer = QTimer()
        self.timer.timeout.connect(self.fetch_logs)
        self.active = False

    def toggle_timer(self):
        self.active = not self.active
        if self.active: self.timer.start(2000)
        else: self.timer.stop()

    def fetch_logs(self):
        try:
            r = requests.get("http://127.0.0.1:8002/stream?lines=3")
            for log in r.json()['logs']:
                color = "white"
                if "ERROR" in log: color = "red"
                elif "WARN" in log: color = "orange"
                self.browser.append(f'<span style="color:{color};">{log}</span>')
        except:
            self.browser.append('<span style="color:gray;">Waiting for server on 8002...</span>')

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = LogDashboard()
    win.show()
    sys.exit(app.exec())
