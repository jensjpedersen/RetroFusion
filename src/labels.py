from PyQt5.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
import pprint
import rom_picker 

import sys


class Labels(QWidget):
    def __init__(self, window: rom_picker.ImageContainerWidget):

        super().__init__()
        self.window = window
        self.prev_label, self.next_label = self.__create_labels()

    def __create_labels(self) -> tuple[QLabel, QLabel]:

        prev_console, next_console = self.__get_consoles()
        next_label = self.__create_label(next_console, 500, 600)
        prev_label = self.__create_label(prev_console, 500, 50)

        return prev_label, next_label

    def __get_consoles(self) -> tuple[str, str]:

        current_index = self.window.current_index

        if self.window.current_index == len(self.window.widgets)-1:
            next_console = list(self.window.widgets.keys())[0]
            prev_console = list(self.window.widgets.keys())[current_index - 1]
        else:
            next_console = list(self.window.widgets.keys())[current_index + 1]
            prev_console = list(self.window.widgets.keys())[current_index - 1]


        return prev_console, next_console

    def update_label(self) -> None:

        prev_console, next_console = self.__get_consoles()
        self.next_label.setText(next_console)
        self.prev_label.setText(prev_console)

    def __create_label(self, text: str, x: int, y: int) -> QLabel: 

        label = QLabel(text, self.window)
        font = QFont()
        font.setFamily(u"Inconsolata Extra Condensed ExtraBold")
        font.setPointSize(70)
        font.setBold(True)
        font.setWeight(75)
        label.setFont(font)
        label.move(x, y)
        label.adjustSize()

        return label


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QWidget()

    label = Labels(window)

    window.show()
    sys.exit(app.exec_())
