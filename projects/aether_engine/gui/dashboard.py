import sys
import os
import time
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                             QHBoxLayout, QPushButton, QLabel, QTableWidget, 
                             QTableWidgetItem, QComboBox, QMessageBox)
from PySide6.QtCore import Qt, QTimer

# Robust import logic for SDK interop
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.join(current_dir, "..", "..", ".."))
if root_dir not in sys.path:
    sys.path.insert(0, root_dir)

from projects.cognis_vault.sdk.cognis_sdk import CognisSDK

class AetherDashboard(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Aether DevOps Engine - Powered by Cognis")
        self.resize(900, 600)
        self.vault = CognisSDK("http://127.0.0.1:8888")
        self.setup_ui()

    def setup_ui(self):
        self.central = QWidget()
        self.setCentralWidget(self.central)
        layout = QVBoxLayout(self.central)
        
        # Header
        header = QLabel("AETHER ENGINE")
        header.setStyleSheet("font-size: 28px; color: #ff79c6; font-weight: bold;")
        layout.addWidget(header)

        # Interop Section
        interop_box = QHBoxLayout()
        self.vault_status = QLabel("Vault Status: Not Connected")
        self.connect_btn = QPushButton("Connect to Cognis Vault")
        self.connect_btn.clicked.connect(self.connect_vault)
        interop_box.addWidget(self.vault_status)
        interop_box.addWidget(self.connect_btn)
        layout.addLayout(interop_box)

        # Deploy Controls
        ctrl_layout = QHBoxLayout()
        self.secret_selector = QComboBox()
        self.secret_selector.setPlaceholderText("Select Credential from Vault")
        self.deploy_btn = QPushButton("RUN SECURE DEPLOY")
        self.deploy_btn.setEnabled(False)
        self.deploy_btn.clicked.connect(self.run_deploy)
        ctrl_layout.addWidget(self.secret_selector)
        ctrl_layout.addWidget(self.deploy_btn)
        layout.addLayout(ctrl_layout)

        # Status Table
        self.table = QTableWidget(0, 3)
        self.table.setHorizontalHeaderLabels(["Service", "Status", "Vault Record ID"])
        self.table.horizontalHeader().setStretchLastSection(True)
        layout.addWidget(self.table)

    def connect_vault(self):
        # 首先检查网络连接
        if not self.vault.check_connection():
            QMessageBox.critical(
                self, 
                "网络连接错误", 
                "无法连接到 Cognis Vault API (http://127.0.0.1:8888)\n\n"
                "请确保:\n"
                "1. API 服务器正在运行\n"
                "2. 端口 8888 没有被占用\n"
                "3. 防火墙没有阻止连接"
            )
            return
        
        # 尝试登录
        if self.vault.login("automated_user", "Aa123456"):
            self.vault_status.setText("Vault Status: SECURE CONNECTION ESTABLISHED")
            self.vault_status.setStyleSheet("color: #50fa7b;")
            self.deploy_btn.setEnabled(True)
            self.refresh_secrets()
        else:
            QMessageBox.warning(
                self, 
                "认证失败", 
                "登录 Cognis Vault 失败\n\n"
                "请检查用户名和密码是否正确"
            )

    def refresh_secrets(self):
        self.secret_selector.clear()
        try:
            secrets = self.vault.list_secrets()
            if not secrets:
                self.secret_selector.addItem("没有可用的凭证", None)
                return
            for s in secrets:
                self.secret_selector.addItem(f"{s['title']} ({s['service_type']})", s['id'])
        except Exception as e:
            QMessageBox.warning(self, "错误", f"获取凭证列表失败: {str(e)}")

    def run_deploy(self):
        secret_id = self.secret_selector.currentData()
        if secret_id is None:
            QMessageBox.warning(self, "错误", "请先选择一个有效的凭证")
            return
        
        title = self.secret_selector.currentText()
        row = self.table.rowCount()
        self.table.insertRow(row)
        self.table.setItem(row, 0, QTableWidgetItem(f"App_{title}"))
        self.table.setItem(row, 1, QTableWidgetItem("In Progress..."))
        self.table.setItem(row, 2, QTableWidgetItem(str(secret_id)))
        
        # Simulate background task
        QTimer.singleShot(2000, lambda: self.table.setItem(row, 1, QTableWidgetItem("SUCCESS (Keys Pulled)")))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    # Apply a quick Dark Theme
    app.setStyleSheet("QWidget { background-color: #282a36; color: #f8f8f2; } QPushButton { background-color: #6272a4; padding: 5px; }")
    window = AetherDashboard()
    window.show()
    sys.exit(app.exec())
