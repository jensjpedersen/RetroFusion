from PyQt5.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
import pprint
import rom_picker 

import sys


class Labels(QWidget):
    def __init__(self, window: rom_picker.ImageContainerWidget):
        super().__init__(window)
        self.window = window


        self.create_label_next(self.window)# -> self.next_label
        self.create_label_prev(self.window)# -> self.prev_label
        # self.set_labels(se)
        # self.__print()

    # def __print(self) -> None:
    #     pprint.pprint(self.__dict__)
    #     pprint.pprint(self.window.__dict__)

    def create_label_next(self, window) -> QLabel: 
        self.window = window
        current_index = self.window.current_index
        next_console = list(self.window.widgets.keys())[current_index + 1]
        self.next_label = self.__create_label(next_console, 500, 600)


    def create_label_prev(self, window) -> QLabel:
        self.window = window
        current_index = self.window.current_index
        prev_console = list(self.window.widgets.keys())[current_index - 1]
        self.prev_label = self.__create_label(prev_console, 500, 50)


    def update_label(self, window) -> None:
        self.window = window
        current_index = self.window.current_index
        next_console = list(self.window.widgets.keys())[current_index + 1]
        prev_console = list(self.window.widgets.keys())[current_index - 1]

        # Continue
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

    def __remove_label(self) -> None:
        # self.prev_label.deleteLater()
        pass
        # self.next_label.deleteLater()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QWidget()

    label = Labels(window)

    window.show()
    sys.exit(app.exec_())
