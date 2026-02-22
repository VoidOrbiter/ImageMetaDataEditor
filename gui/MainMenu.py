from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout,
    QScrollArea, QGridLayout
)
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt, pyqtSignal

from utils.dragndrop import DragNDrop
from utils.imageitem import ImageItem

class MainMenu(QWidget):
    image_added     = pyqtSignal(str)
    image_clicked   = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.resize(800, 600)

        self.image_items =[]

        layout = QVBoxLayout()
        self.setLayout(layout)

        self.dragndrop = DragNDrop(self)
        layout.addWidget(self.dragndrop)

        self.dragndrop.file_dropped.connect(self.add_image)

        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)

        self.gallery_widget = QWidget()
        self.grid_layout = QGridLayout(self.gallery_widget)
        self.grid_layout.setSpacing(10)

        self.scroll_area.setWidget(self.gallery_widget)
        layout.addWidget(self.scroll_area)

    def add_image(self, file_path):
        pixmap = QPixmap(file_path)
        if pixmap.isNull():
            return

        thumbnail = pixmap.scaled(
            150, 150,
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        )

        image_item = ImageItem(thumbnail, file_path)
        image_item.remove_requested.connect(self.remove_image)

        image_item.clicked.connect(lambda path=file_path: self.image_clicked.emit(path))

        self.image_items.append(image_item)
        self.rearrange_grid()

        self.image_added.emit(file_path)

    def remove_image(self, widget):
        self.grid_layout.removeWidget(widget)
        self.image_items.remove(widget)
        widget.deleteLater()
        self.rearrange_grid()

    def rearrange_grid(self):
        for index, widget in enumerate(self.image_items):
            row = index // 3
            col = index % 3
            self.grid_layout.addWidget(widget, row, col)

if __name__ == "__main__":
    import sys
    from PyQt6.QtWidgets import QApplication

    app = QApplication(sys.argv)
    window = MainMenu()
    window.show()
    sys.exit(app.exec())