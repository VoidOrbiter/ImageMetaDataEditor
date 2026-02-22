from PyQt6.QtWidgets import (
    QWidget, QLabel, QVBoxLayout,
    QListWidget
)

class SideBar(QWidget):
    def __init__(self, parent=None):
        super().__init__()
        layout = QVBoxLayout()
        self.setLayout(layout)

        self.image_name_label = QLabel("No image Loaded")
        layout.addWidget(self.image_name_label)

        self.metadata_list = QListWidget()
        layout.addWidget(self.metadata_list)
