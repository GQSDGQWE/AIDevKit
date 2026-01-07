"""
Showcase 04: Container Monitor GUI
由于容器通常运行在 headless 环境，GUI 通过外部 API 监控状态。

EXECUTE:
"""

import sys
import requests
from PySide6.QtWidgets import QApplication, QLabel, QMainWindow
from PySide6.QtCore import QTimer

class ContainerMonitor(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("🐳 Container Monitor")
        self.label = QLabel("Status: Unknown")
        self.setCentralWidget(self.label)
        self.timer = QTimer()
        self.timer.timeout.connect(self.check)
        self.timer.start(3000)

    def check(self):
        try:
            r = requests.get("http://127.0.0.1:8004/health")
            self.label.setText(f"Status: {r.json()['status']}")
            self.label.setStyleSheet("color: green;")
        except:
            self.label.setText("Status: Offline")
            self.label.setStyleSheet("color: red;")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = ContainerMonitor()
    win.show()
    sys.exit(app.exec())
