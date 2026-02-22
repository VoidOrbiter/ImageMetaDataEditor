from PyQt6.QtWidgets import (
    QMainWindow, QStackedWidget, QVBoxLayout,
    QDockWidget
)
from PyQt6.QtCore import Qt
from gui.SideBar import SideBar
from gui.MainMenu import MainMenu

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # ------ WINDOW SETTING ------
        self.setWindowTitle("MetaDataEditor")
        self.resize(800, 600)

        # ------ Layout ------
        layout = QVBoxLayout()
        self.setLayout(layout)

        # ------ QSTACKEDWIDGET ------
        self.stack = QStackedWidget()

        # ------ CENTRAL WIDGET ------
        self.central_widget = MainMenu()
        self.setCentralWidget(self.central_widget)
        # ------ SIDE PANEL ------
        self.sidebar = SideBar(self)
        dock = QDockWidget("Test", self)
        dock.setWidget(self.sidebar)
        self.addDockWidget(Qt.DockWidgetArea.RightDockWidgetArea, dock)


        # ------ ADDING PAGES TO THE STACK ------


if __name__ == "__main__":
    from PyQt6.QtWidgets import QApplication
    import sys

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
