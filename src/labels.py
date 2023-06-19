from PyQt5.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget
from PyQt5.QtGui import QFont
from PyQt5.QtCore import QRect

import sys


# return layout
def set_label(window: QWidget, text: str, x: int, y: int) -> None: 
    label = QLabel(text, window)
    font = QFont()
    font.setFamily(u"Inconsolata Extra Condensed ExtraBold")
    font.setPointSize(70)
    font.setBold(True)
    font.setWeight(75)
    label.setFont(font)
    label.move(x, y)
    label.adjustSize()





if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QWidget()
    set_label(window, "GameCube", 500, 80)
    window.show()
    sys.exit(app.exec_())


