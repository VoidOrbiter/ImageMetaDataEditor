from PyQt6.QtWidgets import (
    QWidget, QLabel, QPushButton
)
from PyQt6.QtCore import pyqtSignal, Qt

class ImageItem(QWidget):
    remove_requested = pyqtSignal(object)
    clicked = pyqtSignal(str)

    def __init__(self, pixmap, file_path):
        super().__init__()
        self.file_path = file_path
        self.setFixedSize(160, 160)

        self.image_label = QLabel(self)
        self.image_label.setGeometry(5, 5, 150, 150)
        self.image_label.setPixmap(pixmap)
        self.image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.remove_button = QPushButton("X", self)
        self.remove_button.setGeometry(5, 5, 25, 25)
        self.remove_button.clicked.connect(self.request_removal)

        self.mousePressEvent = lambda event: self.clicked.emit(self.file_path)

        self.setStyleSheet("border: 1px solid lightgray;")

    def request_removal(self):
        self.remove_requested.emit(self)

    def on_click(self, event):
        self.clicked.emit(self.file_path)