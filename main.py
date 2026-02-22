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
        dock = QDockWidget(self)
        dock.setWidget(self.sidebar)
        self.central_widget.image_clicked.connect(self.sidebar.select_image)
        dock.setFeatures(
            dock.features() | QDockWidget.DockWidgetFeature.DockWidgetClosable | QDockWidget.DockWidgetFeature.DockWidgetMovable)
        dock.setMinimumWidth(150)
        dock.setMaximumWidth(600)
        self.addDockWidget(Qt.DockWidgetArea.RightDockWidgetArea, dock)

        self.central_widget.image_added.connect(self.sidebar.add_image)

        self.sidebar.image_selected.connect(lambda path: print("Selected:", path))

        # ------ ADDING PAGES TO THE STACK ------


if __name__ == "__main__":
    from PyQt6.QtWidgets import QApplication
    import sys
    app = QApplication(sys.argv)
    with open("themes/maintheme.qss", "r") as f:
        app.setStyleSheet(f.read())
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
