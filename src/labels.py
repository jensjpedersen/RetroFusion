from PyQt5.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
import pprint
import rom_picker 

import sys


class Labels(QLabel):
    def __init__(self, window):

        super().__init__(window)
        self.window = window

        self.items = ['item1', 'item2', 'item3', 'item4', 'item5']

        self.__create_label('this is a text', 10, 10)

    # def __create_labels(self) -> tuple[QLabel, QLabel]:

    #     prev_console, next_console = self.__get_consoles()
    #     next_label = self.__create_label(next_console, 800, 480)
    #     prev_label = self.__create_label(prev_console, 800, 100)

    #     return prev_label, next_label

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

        # prev_console, next_console = self.__get_consoles()

        prev_console = self.__format_text(prev_console)
        next_console = self.__format_text(next_console)
        self.next_label.setText(next_console)
        self.prev_label.setText(prev_console)

    def __format_text(self, text: str) -> str:
        text = text.replace("_", " ")
        text = text.title()
        text = text.replace(" ", "")

        return text


     

    def __create_label(self, text: str, x: int, y: int) -> QLabel: 

        text = self.__format_text(text)
        label = QLabel(text, self.window)
        font = QFont()
        # font.setFamily(u"Inconsolata Extra Condensed ExtraBold")
        # font.setFamily(u"Roboto")
        # font.setFamily(u"Roboto Mono")
        font.setFamily(u"Classic Console")
        font.setPointSize(50)
        font.setBold(True)
        font.setWeight(75)
        label.setFont(font)
        label.move(x, y)
        # Set custom size
        label.resize(800, 120)
        # label.adjustSize()

        return label


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QWidget()

    label = Labels(window)

    window.show()
    sys.exit(app.exec_())
