from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout, QListWidget, QListWidgetItem, QSizePolicy
from PyQt6.QtCore import pyqtSignal
from PIL import Image
from PIL.ExifTags import TAGS

class SideBar(QWidget):
    image_selected = pyqtSignal(str)

    def __init__(self, parent=None):
        super().__init__(parent)
        layout = QVBoxLayout()
        self.setLayout(layout)

        self.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)

        self.image_name_label = QLabel("No Image Loaded")
        layout.addWidget(self.image_name_label)
        self.image_name_label.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)

        self.metadata_list = QListWidget()
        layout.addWidget(self.metadata_list)
        self.metadata_list.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)

        self.image_list = QListWidget()
        layout.addWidget(self.image_list)
        self.image_list.currentItemChanged.connect(self.on_image_selected)
        self.image_list.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)

        self.image_paths = []

    def add_image(self, file_path):
        file_name = file_path.split("\\")[-1]
        item = QListWidgetItem(file_name)
        self.image_list.addItem(item)
        self.image_paths.append(file_path)

        if len(self.image_paths) == 1:
            self.image_list.setCurrentRow(0)

    def select_image(self, file_path):
        if file_path not in self.image_paths:
            return

        index = self.image_paths.index(file_path)
        self.image_list.setCurrentRow(index)
        self.update_metadata(file_path)

    def update_metadata(self, file_path):
        self.image_name_label.setText(file_path.split("\\")[-1])
        self.metadata_list.clear()

        try:
            image = Image.open(file_path)
            ext = file_path.lower().split(".")[-1]
            if ext not in ["jpg", "jpeg", "tiff"]:
                self.metadata_list.addItem("No metadata available for this format")
            else:
                exif_data = image.getexif()
                if exif_data:
                    for tag_id, value in exif_data.items():
                        tag = TAGS.get(tag_id, tag_id)
                        self.metadata_list.addItem(f"{tag}: {value}")
                else:
                    self.metadata_list.addItem("No metadata found")
        except Exception as e:
            self.metadata_list.addItem(f"Error reading metadata: {e}")

        self.image_selected.emit(file_path)

    def on_image_selected(self, current, previous):
        if current is None:
            self.image_name_label.setText("No Image Loaded")
            self.metadata_list.clear()
            return

        index = self.image_list.row(current)
        file_path = self.image_paths[index]
        self.update_metadata(file_path)

    def remove_image(self, file_path):
        if file_path not in self.image_paths:
            return

        index = self.image_paths.index(file_path)
        self.image_paths.pop(index)

        if 0 <= index < self.image_list.count():
            item = self.image_list.takeItem(index)
            del item

        # update selection safely
        if self.image_list.count() > 0:
            new_index = min(index, self.image_list.count() - 1)
            self.image_list.setCurrentRow(new_index)
        else:
            self.image_name_label.setText("No Image Loaded")
            self.metadata_list.clear()