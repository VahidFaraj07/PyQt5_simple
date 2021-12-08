from PyQt5.QtWidgets import *
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(200, 300, 500, 400)
        self.setWindowTitle('Label Example')
        self.UI()
        self.show()

    def UI(self):
        self.text1 = QLabel('- hello bro', self)
        self.text2 = QLabel('- hi man', self)
        self.text1.move(10, 100)
        self.text2.move(10, 120)


def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())


if __name__ == '__main__':
    main()
