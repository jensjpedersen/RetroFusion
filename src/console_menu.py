import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QLabel, QWidget
from PyQt5.QtGui import QFont


class ConsoleMenuContainer(QWidget):
    def __init__(self, window):
        super().__init__(window)

        self.window = window
        self.labels = self.__create_labels()

    
    def __create_labels(self): 
        current_index = self.window.image_container.current_index
        widgets = self.window.image_container.widgets.keys()

        labels = []
    
        dy = 50
        y0 = 550
        x0 = 50

        for i, console in enumerate(widgets):

            label = Labels(console, x0, y0+i*dy, self.window)

            if current_index == i:
                label.highlight()

            labels.append(label)

        return labels



    def update(self): 

        current_index = self.window.image_container.current_index

        for i, label in enumerate(self.labels):
            label.remove_highlight()

            if current_index == i:
                label.highlight()



class Labels(QLabel):
    def __init__(self, text: str, x: int, y: int, window):
        super().__init__(window)
        self.window = window

        self.__create_label(x, y)
        self.__set_text(text)

    def __format_text(self, text: str) -> str:
        text = text.replace("_", " ")
        text = text.title()
        text = text.replace(" ", "")

        return text

    def __create_label(self, x: int, y: int):
        font = QFont()
        font.setFamily(u"Classic Console")
        font.setPointSize(45)
        font.setBold(False)
        # font.setWeight(75)
        # font.setWeight(0)
        self.setFont(font)
        self.move(x, y)
        self.setStyleSheet("QLabel { color: #141c27 }")
        self.resize(800, 120)


    def highlight(self) -> None:
        self.setStyleSheet("QLabel { color: #FFFFFF }")

    def remove_highlight(self) -> None:
        self.setStyleSheet("QLabel { color: #141c27 }")

    def __set_text(self, text: str) -> None:
        text = self.__format_text(text)
        self.setText(text)





if __name__ == '__main__':
    app = QApplication(sys.argv)
    
    window = CustomWidget()
    window.setGeometry(500, 500, 400, 200)
    window.show()
    
    sys.exit(app.exec_())
