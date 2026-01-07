# Modern Professional Stylesheet
STYLESHEET = """
QMainWindow { background-color: #1e1e2e; }
QWidget { color: #cdd6f4; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; }
QLineEdit { 
    background-color: #313244; 
    border: 1px solid #45475a; 
    padding: 8px; 
    border-radius: 4px;
    selection-background-color: #89b4fa;
}
QPushButton {
    background-color: #89b4fa;
    color: #1e1e2e;
    font-weight: bold;
    padding: 10px;
    border-radius: 4px;
}
QPushButton:hover { background-color: #b4befe; }
QTableWidget {
    background-color: #181825;
    border: none;
    gridline-color: #313244;
}
QHeaderView::section {
    background-color: #313244;
    padding: 5px;
    border: none;
}
QTabWidget::pane { border: 1px solid #45475a; }
QTabBar::tab {
    background: #313244;
    padding: 10px;
    margin-right: 2px;
}
QTabBar::tab:selected { background: #45475a; border-bottom: 2px solid #89b4fa; }
"""
