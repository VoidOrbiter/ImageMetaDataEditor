from PyQt6.QtWidgets import (
    QWidget, QLabel, QPushButton
)
from PyQt6.QtCore import pyqtSignal, Qt

class ImageItem(QWidget):
    remove_requested = pyqtSignal(object)

    def __init__(self, pixmap):
        super().__init__()
        self.setFixedSize(160, 160)

        self.image_label = QLabel(self)
        self.image_label.setGeometry(5, 5, 150, 150)
        self.image_label.setPixmap(pixmap)
        self.image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.remove_button = QPushButton("X", self)
        self.remove_button.setGeometry(5, 5, 25, 25)
        self.remove_button.clicked.connect(self.request_removal)

        self.setStyleSheet("border: 1px solid lightgray;")

    def request_removal(self):
        self.remove_requested.emit(self)