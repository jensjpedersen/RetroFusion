from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
from PyQt5.QtGui import QPainter, QPainterPath, QColor, QIcon, QFont
from PyQt5.QtCore import Qt, QSize

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
        self.focusPolicy = Qt.NoFocus

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

class TriangularButtonUp(QPushButton):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFixedSize(100, 100)  # Set the size of the button
        self.focusPolicy = Qt.NoFocus

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
        self.focusPolicy = Qt.NoFocus

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
        self.focusPolicy = Qt.NoFocus

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
        self.focusPolicy = Qt.NoFocus

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



# class StartButton(QPushButton):

#     def __init__(self, parent=None):
#         super().__init__(parent)
#         self.__create_button()


#     def update_icon(self):
#         self.console = self.parent().image_container.current_console
#         self.setIcon(QIcon(f"{src_path}/../resources/{self.console}_logo.png"))
#         # self.setIcon(QIcon(f"../resources/gamecube_logo.png"))


#     def __create_button(self): 

#         # button = QPushButton("CLICK", self)
#         # button = QPushButton("", self)

#         # self.setGeometry(200, 200, 200, 200)
#         self.setGeometry(150, 150, 150, 150)

#         self.clicked.connect(self.clickme)

#         # self.setIcon(QIcon("../resources/play_station_2_logo.png"))
#         self.update_icon()
#         # self.setIconSize(QSize(150, 150))
#         self.setIconSize(QSize(150, 150))
#         self.setStyleSheet("background-color: rgba(76,25,40,0);")
#         # self.move(1500, 30)
#         self.move(10, 10)

#     def clickme(self):
#         print("pressed")



class ButtonContainer(QWidget):

    def __init__(self, window):
        super().__init__(window)
        # Fcus

        self.window = window
        self.__create_buttons()



    def __create_buttons(self):

        button_up = TriangularButtonUp(self.window)
        button_right = TriangularButtonRight(self.window)
        button_down = TriangularButtonDown(self.window)
        button_left = TriangularButtonLeft(self.window)
        start_button = StartButton(self.window)
        

        delta = 125
        button_up.move(800+delta, 700-delta)
        button_right.move(800+delta*2, 700)
        button_down.move(800+delta, 700+delta)
        button_left.move(800, 700)
        start_button.move(925, 700)


    # def update(self): 
    #     # self.start_button.update_icon()



    
# def set_button(window: QWidget) -> None:
#     button_up = TriangularButtonUp(window)
#     button_right = TriangularButtonRight(window)
#     button_down = TriangularButtonDown(window)
#     button_left = TriangularButtonLeft(window)

#     delta = 150
#     button_left.move(800, 700)
#     button_up.move(800+delta, 700-delta)
#     button_right.move(800+delta*2, 700)
#     button_down.move(800+delta, 700+delta)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QWidget()

    set_button(window)
    
    # button_up.clicked.connect(lambda: print("Button clicked!"))
    window.show()
    sys.exit(app.exec_())
