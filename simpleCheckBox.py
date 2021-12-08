import sys
from PyQt5.QtWidgets import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(150, 250, 500, 350)
        self.setWindowTitle('Empty window Example')
        self.UI()
        self.show()

    def UI(self):
        self.name = QLineEdit(self)
        self.surname = QLineEdit(self)

        self.name.move(10, 10)
        self.surname.move(10, 40)

        self.name.setPlaceholderText("Enter your name")
        self.surname.setPlaceholderText("Enter your surname")

        self.remember = QCheckBox("Remember me", self)
        self.remember.move(10, 70)

        submitButton = QPushButton("Submit", self)
        submitButton.move(10, 100)
        submitButton.clicked.connect(self.submit)

    def submit(self):
        if(self.remember.isChecked()):
            print(
                f"name: {self.name.text()}\nsurname: {self.surname.text()}\nRemember me is checked")
        else:
            print(
                f"name: {self.name.text()}\nsurname: {self.surname.text()}\nRemember me is not checked")


def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())


if __name__ == '__main__':
    main()
