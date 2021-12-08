import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont

myFont1 = QFont("Boardway")
myFont2 = QFont("Candara")


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(150, 250, 500, 350)
        self.setWindowTitle('MessageBox Example')
        self.UI()
        self.show()

    def UI(self):
        infoButton = QPushButton("Info", self)
        exitButton = QPushButton("Click me", self)

        infoButton.setFont(myFont1)
        exitButton.setFont(myFont2)

        infoButton.move(50, 50)
        exitButton.move(150, 50)

        infoButton.clicked.connect(self.myInfoMessage)
        exitButton.clicked.connect(self.myExitMessage)

    def myInfoMessage(self):
        message = QMessageBox.information(self, "Info", "Life has no Ctrl + Z")

    def myExitMessage(self):
        message = QMessageBox.question(
            self, "Warning", "Are you sure you want to exit?", QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel)
        if message == QMessageBox.Yes:
            sys.exit()


def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())


if __name__ == '__main__':
    main()
