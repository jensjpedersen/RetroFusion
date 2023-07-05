
import rom_picker
import buttons
import console_menu 
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QStackedLayout, QLabel
from PyQt5.QtGui import QImage, QPalette, QBrush
from PyQt5.QtCore import Qt
import sys
import os 

# TODO: handle empty dirs

src_path = os.path.dirname(os.path.realpath(__file__))

def list_non_empty_directories(directory):
    non_empty_dirs = []
    for root, dirs, files in os.walk(directory):
        if files:
            non_empty_dirs.append(root)

    if not non_empty_dirs: 
        print("Error: The roms directory is either empty or the titiles are not correctly formated.")
        sys.exit(1)

    return non_empty_dirs


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFocusPolicy(Qt.StrongFocus)

        self.setWindowTitle("Retro Fusion")
        self.resize(1600, 900)
 

        thumbanils_path = f'{src_path}/../thumbnails'  # Replace with the actual directory path
        non_empty_dirs = list_non_empty_directories(thumbanils_path)
        self.image_container = rom_picker.ImageContainerWidget(non_empty_dirs)
        self.setCentralWidget(self.image_container)

        # Set background_image
        bg_image_path = f'{src_path}/../resources/bg_2.jpg'  # Replace with the actual image path
        # bg_image_path = f'{src_path}/../sep09.jpg'
        self.set_background_image(bg_image_path)



        # Add buttons 
        # buttons.set_button(self)

        self.buttons = buttons.ButtonContainer(self)
        self.handleButtonClicked()


        # Start button 
        # self.start_button = start_button.StartButton(self)

        # Init console menu
        self.console_menu = console_menu.ConsoleMenuContainer(self)


    def set_background_image(self, image_path):
        background_image = QImage(image_path)
        palette = QPalette()
        palette.setBrush(QPalette.Background, QBrush(background_image))
        self.setPalette(palette)


    def handleButtonClicked(self):
        self.buttons.button_left.clicked.connect(lambda: self.left())
        self.buttons.button_right.clicked.connect(lambda: self.right())
        self.buttons.button_up.clicked.connect(lambda: self.up())
        self.buttons.button_down.clicked.connect(lambda: self.down())
        # Start and settings buttons in handled in respective classes


    def up(self): 
        if self.image_container.current_index == 0: self.image_container.current_index = len(self.image_container.widgets)
        self.image_container.change_layout(-1)
        self.console_menu.update()

    def down(self): 
        if self.image_container.current_index == len(self.image_container.widgets)-1: self.image_container.current_index = -1 
        self.image_container.change_layout(+1)
        self.console_menu.update()

    def left(self):
        self.image_container.current_widget.scroll_images(-1)

    def right(self):
        self.image_container.current_widget.scroll_images(1)

    def settings(self):
        print(f'console:{self.image_container.current_console}')
        sys.exit()

    def start(self):
        print(f'choice:{self.image_container.current_widget.images[self.image_container.current_widget.current_index]}')
        sys.exit()


    def keyPressEvent(self, event):

        if event.key() == Qt.Key_Left or event.key() == Qt.Key_H:
            self.left()

        elif event.key() == Qt.Key_Right or event.key() == Qt.Key_L:
            self.right()

        elif event.key() == Qt.Key_Up or event.key() == Qt.Key_K:
            self.up()

        elif event.key() == Qt.Key_Down or event.key() == Qt.Key_J:
            self.down()

        elif event.key() == Qt.Key_Return:
            self.start()



def main(): 
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

main()
