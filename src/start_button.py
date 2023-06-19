
# importing libraries
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
import pprint

class StartButton(QPushButton):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.__create_button()
        self.__print_parent()

    def __print_parent(self):
        pprint.pprint(self.parent().__dict__)


    def update_icon(self):
        self.console = self.parent().image_container.current_console
        self.setIcon(QIcon(f"../resources/{self.console}_logo.png"))
        # self.setIcon(QIcon(f"../resources/gamecube_logo.png"))


    def __create_button(self): 

        # button = QPushButton("CLICK", self)
        # button = QPushButton("", self)

        self.setGeometry(150, 150, 150, 150)

        self.clicked.connect(self.clickme)

        # self.setIcon(QIcon("../resources/play_station_2_logo.png"))
        self.update_icon()
        self.setIconSize(QSize(150, 150))
        self.setStyleSheet("background-color: rgba(76,25,40,0);")
        self.move(1500, 30)

    def clickme(self):
        print("pressed")

 
 

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QWidget()
    button = StartButton(window)
    window.show()
    sys.exit(app.exec_())
