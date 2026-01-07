import sys
import os
import threading
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, 
                             QLineEdit, QPushButton, QLabel, QTableWidget, QTableWidgetItem,
                             QTabWidget, QMessageBox, QDialog, QFormLayout)
from PySide6.QtCore import Qt, Signal, Slot

# Robust import logic
current_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(current_dir, ".."))
if project_dir not in sys.path:
    sys.path.insert(0, project_dir)

from sdk.cognis_sdk import CognisSDK
from gui.styles import STYLESHEET

class CognitoApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.sdk = CognisSDK()
        self.setWindowTitle("Cognis Vault Professional v1.0")
        self.resize(1000, 700)
        self.setStyleSheet(STYLESHEET)
        
        self.init_login()

    def init_login(self):
        self.central = QWidget()
        self.setCentralWidget(self.central)
        layout = QVBoxLayout(self.central)
        layout.setAlignment(Qt.AlignCenter)

        self.title = QLabel("COGNIS VAULT PRO")
        self.title.setStyleSheet("font-size: 24px; font-weight: bold; color: #89b4fa; margin-bottom: 20px;")
        layout.addWidget(self.title)

        self.user_input = QLineEdit()
        self.user_input.setPlaceholderText("Username")
        self.user_input.setFixedWidth(300)
        layout.addWidget(self.user_input)

        self.pass_input = QLineEdit()
        self.pass_input.setPlaceholderText("Password")
        self.pass_input.setEchoMode(QLineEdit.Password)
        self.pass_input.setFixedWidth(300)
        layout.addWidget(self.pass_input)

        btn_layout = QHBoxLayout()
        self.login_btn = QPushButton("LOGIN")
        self.login_btn.clicked.connect(self.handle_login)
        self.reg_btn = QPushButton("REGISTER")
        self.reg_btn.clicked.connect(self.handle_register)
        self.reg_btn.setStyleSheet("background-color: #585b70; color: white;")
        
        btn_layout.addWidget(self.login_btn)
        btn_layout.addWidget(self.reg_btn)
        layout.addLayout(btn_layout)

    def handle_login(self):
        u, p = self.user_input.text(), self.pass_input.text()
        if self.sdk.login(u, p):
            self.init_dashboard()
        else:
            QMessageBox.critical(self, "Error", "Authentication Failed")

    def handle_register(self):
        u, p = self.user_input.text(), self.pass_input.text()
        if not u or not p: return
        res = self.sdk.register(u, p)
        QMessageBox.information(self, "Success", f"User {u} registered. Please login.")

    def init_dashboard(self):
        self.tabs = QTabWidget()
        self.setCentralWidget(self.tabs)

        # Tab 1: Secrets
        self.vault_tab = QWidget()
        v_layout = QVBoxLayout(self.vault_tab)
        
        self.record_table = QTableWidget(0, 4)
        self.record_table.setHorizontalHeaderLabels(["Title", "Type", "Payload", "Created At"])
        self.record_table.horizontalHeader().setStretchLastSection(True)
        v_layout.addWidget(self.record_table)

        btn_ctrl = QHBoxLayout()
        self.add_btn = QPushButton("+ New Secret")
        self.add_btn.clicked.connect(self.show_add_dialog)
        self.refresh_btn = QPushButton("Refresh")
        self.refresh_btn.clicked.connect(self.load_data)
        btn_ctrl.addWidget(self.add_btn)
        btn_ctrl.addWidget(self.refresh_btn)
        v_layout.addLayout(btn_ctrl)

        self.tabs.addTab(self.vault_tab, "Vault Records")

        # Tab 2: Audit Logs
        self.audit_tab = QWidget()
        a_layout = QVBoxLayout(self.audit_tab)
        self.audit_table = QTableWidget(0, 2)
        self.audit_table.setHorizontalHeaderLabels(["Action", "Timestamp"])
        self.audit_table.horizontalHeader().setStretchLastSection(True)
        a_layout.addWidget(self.audit_table)
        self.tabs.addTab(self.audit_tab, "Security Audit")

        self.load_data()

    def load_data(self):
        # Load Records
        records = self.sdk.list_secrets()
        self.record_table.setRowCount(len(records))
        for i, r in enumerate(records):
            self.record_table.setItem(i, 0, QTableWidgetItem(r['title']))
            self.record_table.setItem(i, 1, QTableWidgetItem(r['service_type']))
            self.record_table.setItem(i, 2, QTableWidgetItem(r['payload']))
            self.record_table.setItem(i, 3, QTableWidgetItem(r['created_at']))

        # Load Audits
        logs = self.sdk.get_audit_logs()
        self.audit_table.setRowCount(len(logs))
        for i, l in enumerate(logs):
            self.audit_table.setItem(i, 0, QTableWidgetItem(l['action']))
            self.audit_table.setItem(i, 1, QTableWidgetItem(l['timestamp']))

    def show_add_dialog(self):
        dialog = QDialog(self)
        dialog.setWindowTitle("Add Secret")
        form = QFormLayout(dialog)
        
        title_in = QLineEdit()
        type_in = QLineEdit()
        type_in.setPlaceholderText("e.g. Password, SSH Key")
        content_in = QLineEdit()
        
        form.addRow("Title:", title_in)
        form.addRow("Type:", type_in)
        form.addRow("Content:", content_in)
        
        save_btn = QPushButton("SAVE SECURELY")
        save_btn.clicked.connect(lambda: [
            self.sdk.add_secret(title_in.text(), type_in.text(), content_in.text()),
            dialog.accept(),
            self.load_data()
        ])
        form.addRow(save_btn)
        dialog.exec()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CognitoApp()
    window.show()
    sys.exit(app.exec())
