
import rom_picker
import buttons
import lables
from PyQt5.QtWidgets import QApplication
import sys

def main(): 
    app = QApplication(sys.argv)
    window = rom_picker.MainWindow()

    buttons.set_button(window)


    window.show()
    sys.exit(app.exec_())



main()
