"""
Showcase 03: Crypto Pulse - Pulse GUI
实时波动监控。

PLAN:
1. 实现异步获取的 SDK 类。
2. 绘制简易波形或大号字体行情。

EXECUTE:
"""

import sys
import requests
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget
from PySide6.QtCore import QTimer, Qt
from PySide6.QtGui import QFont

class CryptoPulse(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("📈 Crypto Pulse")
        self.setFixedSize(300, 200)
        
        container = QWidget()
        layout = QVBoxLayout(container)
        
        self.label = QLabel("BTC: $0.00")
        self.label.setFont(QFont("Arial", 24, QFont.Bold))
        self.label.setAlignment(Qt.AlignCenter)
        
        layout.addWidget(self.label)
        self.setCentralWidget(container)
        
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_price)
        self.timer.start(1000)

    def update_price(self):
        try:
            r = requests.get("http://127.0.0.1:8003/ticker/BTC")
            price = r.json()['price']
            self.label.setText(f"BTC: ${price:,.2f}")
            self.label.setStyleSheet("color: green;" if random.getrandbits(1) else "color: red;")
        except:
            self.label.setText("Link Lost")
            self.label.setStyleSheet("color: gray;")

if __name__ == "__main__":
    import random # 为演示颜色随机
    app = QApplication(sys.argv)
    win = CryptoPulse()
    win.show()
    sys.exit(app.exec())
