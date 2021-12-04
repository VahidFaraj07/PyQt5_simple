import sys
from PyQt5.QtWidgets import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(150, 250, 500, 350)
        self.setWindowTitle('pyqt5 app')
        self.show()

App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())
