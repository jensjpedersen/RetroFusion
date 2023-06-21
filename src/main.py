
import rom_picker
import buttons
import console_menu 
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QStackedLayout, QLabel
from PyQt5.QtGui import QImage, QPalette, QBrush
from PyQt5.QtCore import Qt
import sys
import os 


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

        self.setWindowTitle("Retro Fusion")
        self.resize(1600, 900)
 

        thumbanils_path = f'{src_path}/../thumbnails'  # Replace with the actual directory path
        non_empty_dirs = list_non_empty_directories(thumbanils_path)
        self.image_container = rom_picker.ImageContainerWidget(non_empty_dirs)
        self.setCentralWidget(self.image_container)

        # Set background_image
        bg_image_path = f'{src_path}/../bg_2.jpg'  # Replace with the actual image path
        # bg_image_path = f'{src_path}/../sep09.jpg'
        self.set_background_image(bg_image_path)



        # Add buttons 
        # buttons.set_button(self)

        self.buttons = buttons.ButtonContainer(self)


        # Start button 
        # self.start_button = start_button.StartButton(self)

        # Init console menu
        self.console_menu = console_menu.ConsoleMenuContainer(self)


    def set_background_image(self, image_path):
        background_image = QImage(image_path)
        palette = QPalette()
        palette.setBrush(QPalette.Background, QBrush(background_image))
        self.setPalette(palette)

    def keyPressEvent(self, event):

        if event.key() == Qt.Key_Left or event.key() == Qt.Key_H:
            self.image_container.current_widget.scroll_images(-1)

        elif event.key() == Qt.Key_Right or event.key() == Qt.Key_L:
            self.image_container.current_widget.scroll_images(1)

        elif event.key() == Qt.Key_Up or event.key() == Qt.Key_K:
            if self.image_container.current_index == 0: self.image_container.current_index = len(self.image_container.widgets)
            self.image_container.change_layout(-1)
            # self.start_button.update_icon()
            self.console_menu.update()
            self.buttons.update()

        elif event.key() == Qt.Key_Down or event.key() == Qt.Key_J:
            if self.image_container.current_index == len(self.image_container.widgets)-1: self.image_container.current_index = -1 
            self.image_container.change_layout(+1)
            # self.start_button.update_icon()
            self.console_menu.update()
            self.buttons.update()

        elif event.key() == Qt.Key_Return:
            print(f'choice:{self.image_container.current_widget.images[self.image_container.current_widget.current_index]}')
            sys.exit()



def main(): 
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

main()
