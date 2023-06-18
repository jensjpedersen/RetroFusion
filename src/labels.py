from PyQt5.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget
from PyQt5.QtGui import QFont
from PyQt5.QtCore import QRect

import sys


# return layout
def set_label(window: QWidget, text: str, x: int, y: int): 
    label = QLabel(text)
    font = QFont()
    font.setFamily(u"Inconsolata Extra Condensed ExtraBold")
    font.setPointSize(40)
    font.setBold(True)
    font.setWeight(75)
    label.setFont(font)
    layout = QVBoxLayout()


    layout.addWidget(label)
    layout.setContentsMargins(x, y, 0, 0)
    window.setLayout(layout)

    return layout





if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QWidget()
    set_label(window, "GameCube", 500, 80)
    window.show()
    sys.exit(app.exec_())


