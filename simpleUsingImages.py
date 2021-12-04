import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(150, 250, 700, 700)
        self.setWindowTitle('Empty window Example')
        self.UI()
        self.show()

    def UI(self):
        self.image = QLabel(self)
        self.image.setPixmap(QPixmap('D:/Images/xxx.jpg'))
        self.image.move(30, 30)

        removeButton = QPushButton("Remove", self)
        removeButton.move(5, 5)
        removeButton.clicked.connect(self.removeImage)

        showButton = QPushButton("Show", self)
        showButton.move(105, 5)
        showButton.clicked.connect(self.showImage)

    def removeImage(self):
        self.image.close()

    def showImage(self):
        self.image.show()


App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())


# image direcotory D:/23/Images/xy/
