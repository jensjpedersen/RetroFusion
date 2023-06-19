from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
from PyQt5.QtGui import QPainter, QPainterPath, QColor
from PyQt5.QtCore import Qt
import sys


class TriangularButtonUp(QPushButton):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFixedSize(100, 100)  # Set the size of the button

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        path = QPainterPath()
        path.moveTo(0, self.height())  # Move to the bottom-left corner
        path.lineTo(self.width() / 2, 0)  # Draw a line to the top-middle point
        path.lineTo(self.width(), self.height())  # Draw a line to the bottom-right corner
        path.lineTo(0, self.height())  # Draw a line back to the bottom-left corner

        # Set the button's color and border
        if self.isDown():
            painter.setBrush(Qt.darkGray)
        elif self.isChecked():
            painter.setBrush(Qt.gray)
        else:
            # painter.setBrush(Qt.black)
            painter.setBrush(QColor(76, 25, 40))


        # self.setStyleSheet("background-color: rgba(76,25,40,0);")
        painter.setPen(Qt.black)
        painter.drawPath(path)

    def sizeHint(self):
        return self.minimumSizeHint()

class TriangularButtonRight(QPushButton):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFixedSize(100, 100)  # Set the size of the button

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        path = QPainterPath()
        path.moveTo(0, 0)  # Move to the top-left corner
        path.lineTo(self.width(), self.height() / 2)  # Draw a line to the middle-right point
        path.lineTo(0, self.height())  # Draw a line to the bottom-left corner
        path.lineTo(0, 0)  # Draw a line back to the top-left corner

        # Set the button's color and border
        if self.isDown():
            painter.setBrush(Qt.darkGray)
        elif self.isChecked():
            painter.setBrush(Qt.gray)
        else:
            # painter.setBrush(Qt.black)
            painter.setBrush(QColor(76, 25, 40))
        painter.setPen(Qt.black)
        painter.drawPath(path)

    def sizeHint(self):
        return self.minimumSizeHint()


class TriangularButtonDown(QPushButton):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFixedSize(100, 100)  # Set the size of the button

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        path = QPainterPath()
        path.moveTo(0, 0)  # Move to the top-left corner
        path.lineTo(self.width() / 2, self.height())  # Draw a line to the bottom-center point
        path.lineTo(self.width(), 0)  # Draw a line to the top-right corner
        path.lineTo(0, 0)  # Draw a line back to the top-left corner

        # Set the button's color and border
        if self.isDown():
            painter.setBrush(Qt.darkGray)
        elif self.isChecked():
            painter.setBrush(Qt.gray)
        else:
            # painter.setBrush(Qt.black)
            painter.setBrush(QColor(76, 25, 40))


        painter.setPen(Qt.black)
        painter.drawPath(path)

    def sizeHint(self):
        return self.minimumSizeHint()

class TriangularButtonLeft(QPushButton):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFixedSize(100, 100)  # Set the size of the button

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        path = QPainterPath()

        path.moveTo(self.width(), 0)  # Move to the top-right corner
        path.lineTo(0, self.height() / 2)  # Draw a line to the middle-left point
        path.lineTo(self.width(), self.height())  # Draw a line to the bottom-right corner
        path.lineTo(self.width(), 0)  # Draw a line back to the top-right corner

        # Set the button's color and border
        if self.isDown():
            painter.setBrush(Qt.darkGray)
        elif self.isChecked():
            painter.setBrush(Qt.gray)
        else:
            # painter.setBrush(Qt.black)
            painter.setBrush(QColor(76, 25, 40))

        painter.setPen(Qt.black)
        painter.drawPath(path)

    def sizeHint(self):
        return self.minimumSizeHint()


def set_button(window: QWidget) -> None:
    button_up = TriangularButtonUp(window)
    button_right = TriangularButtonRight(window)
    button_down = TriangularButtonDown(window)
    button_left = TriangularButtonLeft(window)

    button_left.move(15, 320)
    button_up.move(900, 10)
    button_right.move(1700, 320)
    button_down.move(900, 600)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QWidget()

    set_button(window)
    
    # button_up.clicked.connect(lambda: print("Button clicked!"))
    window.show()
    sys.exit(app.exec_())
