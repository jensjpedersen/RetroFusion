import sys
import os
import pprint
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QImage, QPalette, QBrush
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QGridLayout, QWidget, QVBoxLayout


src_path = os.path.dirname(os.path.realpath(__file__))

class ImageDisplayWidget(QWidget):
    def __init__(self, image_directory):
        super().__init__()
        self.image_directory = image_directory
        self.images = []
        self.current_index = 0
        self.num_images_per_row = 9
        # self.center_image_index = self.num_images_per_row // 2  # Index of the center image
        self.center_image_index = 0  # Index of the center image
        self.center_image_size = 300  # Size of the center image

        self.layout = QGridLayout()
        self.setLayout(self.layout)

        self.load_images()
        self.display_images()

    def load_images(self):
        for filename in sorted(os.listdir(self.image_directory)):
            if filename.endswith(".jpg") or filename.endswith(".png"):
                self.images.append(os.path.join(self.image_directory, filename))

    def display_images(self):
        row = 0
        col = 0
        for i in range(self.current_index, min(self.current_index + self.num_images_per_row, len(self.images))):
            image_label = QLabel()
            pixmap = QPixmap(self.images[i])

            # Adjust the size based on whether it's the center image or not
            if i == self.current_index + self.center_image_index:
                pixmap = pixmap.scaledToWidth(self.center_image_size)
            else:
                pixmap = pixmap.scaledToWidth(200)

            image_label.setPixmap(pixmap)

            # Center veritcally
            self.layout.addWidget(image_label, row, col)
            col += 1
            if col >= self.num_images_per_row:
                row += 1
                col = 0

        # Set column and row stretch factors to ensure consistent spacing
        self.layout.setColumnStretch(self.num_images_per_row, 1)
        self.layout.setRowStretch(row + 1, 1)
        self.layout.setContentsMargins(50, 0, 0, 450)

    def clear_images(self):
        while self.layout.count():
            child = self.layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()

    def scroll_images(self, step):
        self.current_index += step

        if self.current_index < 0:
            self.current_index = len(self.images) - 1
        elif self.current_index >= len(self.images):
            self.current_index = 0

        self.clear_images()
        self.display_images()


class ImageContainerWidget(QWidget):
    def __init__(self, thumbanils_dirs: list):
        super().__init__()

        self.current_index: int = 0
        self.widgets = self.__create_image_widgets(thumbanils_dirs)
        self.layout = QGridLayout()
        self.setLayout(self.layout)
        self.current_console = list(self.widgets.keys())[self.current_index]
        self.current_widget = self.widgets[self.current_console]
        self.layout.addWidget(self.current_widget, 0, 0, Qt.AlignVCenter)




    def __create_image_widgets(self, thumbnils_dirs: list) -> None: 
        widgets = {}
        for d in thumbnils_dirs: 
            console = os.path.basename(d)
            widgets[console] = ImageDisplayWidget(d)

        return widgets


    def change_layout(self, step: int) -> None:
            self.current_widget.hide()
            self.layout.removeWidget(self.current_widget)

            # Change widget
            self.current_index = self.current_index + step
            self.current_console = list(self.widgets)[self.current_index]
            self.current_widget = self.widgets[self.current_console]
            self.layout.addWidget(self.current_widget, 0, 0, Qt.AlignVCenter)
            self.setCurrentWidget()


    def setCurrentWidget(self):
        self.current_widget.setFocus()
        self.current_widget.show()





