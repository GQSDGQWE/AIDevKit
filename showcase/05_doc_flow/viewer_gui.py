"""
Showcase 05: DocFlow Previewer GUI

PLAN:
1. 列表展示文件。
2. 预览基本元数据。

EXECUTE:
"""

import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QListWidget, QVBoxLayout, QWidget, QLabel
try:
    from engine.sdk import DocEngine
except:
    from sdk import DocEngine

class DocPreviewer(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("📑 DocFlow Previewer")
        self.resize(400, 400)
        
        container = QWidget()
        layout = QVBoxLayout(container)
        
        self.list = QListWidget()
        self.engine = DocEngine(".")
        
        for item in self.engine.scan()[:10]:
            self.list.addItem(f"{item['file']} ({item['size']} bytes)")
            
        layout.addWidget(QLabel("Scanned Source Files:"))
        layout.addWidget(self.list)
        self.setCentralWidget(central_widget := container)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = DocPreviewer()
    win.show()
    sys.exit(app.exec())
