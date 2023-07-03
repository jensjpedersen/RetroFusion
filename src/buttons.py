from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
from PyQt5.QtGui import QPainter, QPainterPath, QColor, QIcon, QFont, QKeyEvent
from PyQt5.QtCore import Qt

import sys
import os

# TODO: handle C-C

src_path = os.path.dirname(os.path.realpath(__file__))

class StartButton(QPushButton):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFixedSize(100, 100)  # Set the size of the button
        self.setText("Start")  # Set the text on the button
        self.setFont(QFont("Arial", 12, QFont.Bold))  # Set the font for the text
        self.setFocusPolicy(Qt.NoFocus)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        path = QPainterPath()
        path.addRoundedRect(0, 0, self.width(), self.height(), 5, 5)

        # Set the button's color and border
        if self.isDown():
            painter.setBrush(Qt.darkGray)
        elif self.isChecked():
            painter.setBrush(Qt.gray)
        else:
            painter.setBrush(QColor(76, 25, 40))

        painter.setPen(Qt.black)
        painter.drawPath(path)

        # Render the text on the button
        painter.setPen(Qt.white)  # Set the color of the text
        painter.drawText(self.rect(), Qt.AlignCenter, self.text())

    def keyPressEvent(self, event: QKeyEvent):
        if event.key() in (Qt.Key_Up, Qt.Key_Down, Qt.Key_Left, Qt.Key_Right):
            event.ignore()
        else:
            super().keyPressEvent(event)


class TriangularButtonUp(QPushButton):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFixedSize(100, 100)  # Set the size of the button
        self.setFocusPolicy(Qt.NoFocus)

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
            painter.setBrush(QColor(76, 25, 40))

        painter.setPen(Qt.black)
        painter.drawPath(path)

    def sizeHint(self):
        return self.minimumSizeHint()


class TriangularButtonRight(QPushButton):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFixedSize(100, 100)  # Set the size of the button
        self.setFocusPolicy(Qt.NoFocus)

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
            painter.setBrush(QColor(76, 25, 40))

        painter.setPen(Qt.black)
        painter.drawPath(path)

    def sizeHint(self):
        return self.minimumSizeHint()


class TriangularButtonDown(QPushButton):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFixedSize(100, 100)  # Set the size of the button
        self.setFocusPolicy(Qt.NoFocus)

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
            painter.setBrush(QColor(76, 25, 40))

        painter.setPen(Qt.black)
        painter.drawPath(path)

    def sizeHint(self):
        return self.minimumSizeHint()


class TriangularButtonLeft(QPushButton):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFixedSize(100, 100)  # Set the size of the button
        self.setFocusPolicy(Qt.NoFocus)

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
            painter.setBrush(QColor(76, 25, 40))

        painter.setPen(Qt.black)
        painter.drawPath(path)

    def sizeHint(self):
        return self.minimumSizeHint()


class ButtonContainer(QWidget):
    def __init__(self, window):
        super().__init__(window)
        self.window = window
        self.__create_buttons()

    def __create_buttons(self):
        button_up = TriangularButtonUp(self.window)
        button_right = TriangularButtonRight(self.window)
        button_down = TriangularButtonDown(self.window)
        button_left = TriangularButtonLeft(self.window)
        start_button = StartButton(self.window)

        delta = 125
        button_up.move(800 + delta, 700 - delta)
        button_right.move(800 + delta * 2, 700)
        button_down.move(800 + delta, 700 + delta)
        button_left.move(800, 700)
        start_button.move(925, 700)

    def keyPressEvent(self, event: QKeyEvent):
        if event.key() in (Qt.Key_Up, Qt.Key_Down, Qt.Key_Left, Qt.Key_Right):
            event.ignore()
        else:
            super().keyPressEvent(event)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QWidget()

    container = ButtonContainer(window)

    window.show()
    sys.exit(app.exec_())
