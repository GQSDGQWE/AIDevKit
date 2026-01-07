"""
Showcase 01: Todo Master Pro - SDK & GUI
集成 SDK 控制与 PySide6 界面。

PLAN:
1. 实现 TodoSDK。
2. 实现 GUI 主窗口。
3. 提供打包入口。

EXECUTE:
"""

import requests
import sys
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                             QLineEdit, QPushButton, QListWidget, QListWidgetItem)

class TodoSDK:
    def __init__(self, url="http://127.0.0.1:8001"):
        self.url = url

    def add(self, task):
        return requests.post(f"{self.url}/todos", json={"task": task}).json()

    def list(self):
        return requests.get(f"{self.url}/todos").json()

class TodoGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.sdk = TodoSDK()
        self.setWindowTitle("✅ Todo Master Pro")
        self.setFixedSize(400, 500)
        
        central = QWidget()
        layout = QVBoxLayout(central)
        
        self.input = QLineEdit(placeholderText="Enter new task...")
        self.add_btn = QPushButton("Add Task")
        self.list_view = QListWidget()
        self.refresh_btn = QPushButton("Refresh List")
        
        self.add_btn.clicked.connect(self.add_task)
        self.refresh_btn.clicked.connect(self.load_tasks)
        
        for w in [self.input, self.add_btn, self.list_view, self.refresh_btn]:
            layout.addWidget(w)
        
        self.setCentralWidget(central)

    def add_task(self):
        if self.input.text():
            self.sdk.add(self.input.text())
            self.input.clear()
            self.load_tasks()

    def load_tasks(self):
        self.list_view.clear()
        try:
            tasks = self.sdk.list()
            for t in tasks:
                status = "✔" if t['completed'] else "⏳"
                self.list_view.addItem(f"[{status}] {t['task']}")
        except:
            self.list_view.addItem("Err: Server not running on 8001")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = TodoGUI()
    win.show()
    sys.exit(app.exec())
