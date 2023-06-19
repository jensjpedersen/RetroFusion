
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


    def __create_button(self): 

        # button = QPushButton("CLICK", self)
        # button = QPushButton("", self)

        self.setGeometry(100, 100, 100, 100)

        self.clicked.connect(self.clickme)

        self.setIcon(QIcon("../resources/play_station_2_logo.png"))
        self.setIconSize(QSize(100, 100))
        self.setStyleSheet("background-color: rgba(0,0,0,0);")
        self.move(10, 10)
        # button.show()

    def clickme(self):
        # printing pressed
        print("pressed")

 
 

if __name__ == '__main__':
    pass
    app = QApplication(sys.argv)
    window = QWidget()
    button = StartButton(window)
    window.show()
    sys.exit(app.exec_())
