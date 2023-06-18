
import rom_picker
import buttons
import labels
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QImage, QPalette, QBrush
from PyQt5.QtCore import Qt
import sys
import os 
import pprint


src_path = os.path.dirname(os.path.realpath(__file__))

def list_non_empty_directories(directory):
    non_empty_dirs = []
    for root, dirs, files in os.walk(directory):
        if files:
            non_empty_dirs.append(root)
    return non_empty_dirs


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Python")
        self.resize(1600, 900)
 

        thumbanils_path = f'{src_path}/../thumbnails'  # Replace with the actual directory path
        non_empty_dirs = list_non_empty_directories(thumbanils_path)
        self.image_container = rom_picker.ImageContainerWidget(non_empty_dirs)
        self.setCentralWidget(self.image_container)

        # Set background_image
        bg_image_path = f'{src_path}/../bg_2.jpg'  # Replace with the actual image path
        self.set_background_image(bg_image_path)


        # Add labels 
        self.image_container.layout.addLayout(labels.set_label(self, "GameCube", 500, 80), 0, 0, Qt.AlignBottom)


        # Add buttons
        # buttons.set_button(self, "A", 100, 100)

        buttons.set_button(self.image_container)

        # pprint.pprint(self.image_container.__dict__)

        # main_layout = self.image_container.layout
        # main_layout.addLayout(layout, 0, 0, Qt.AlignBottom)



    def set_background_image(self, image_path):
        background_image = QImage(image_path)
        palette = QPalette()
        palette.setBrush(QPalette.Background, QBrush(background_image))
        self.setPalette(palette)

    def keyPressEvent(self, event):
        self.image_container.keyPressEvent(event)



def main(): 
    # app = QApplication(sys.argv)
    # window = rom_picker.MainWindow()


    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())




    # buttons.set_button(window)

    # labels.set_label(window, "GameCube", 10, 10)



    # window.show()
    # sys.exit(app.exec_())



main()
