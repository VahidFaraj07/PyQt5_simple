import sys
from PyQt5.QtWidgets import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(150, 250, 500, 350)
        self.setWindowTitle('RadioButton Example')
        self.UI()
        self.show()

    def UI(self):
        self.name = QLineEdit(self)
        self.surname = QLineEdit(self)
        self.male = QRadioButton("Male", self)
        self.female = QRadioButton("Female", self)
        submitButton = QPushButton("Submit", self)

        self.name.setPlaceholderText("Enter your name")
        self.surname.setPlaceholderText("Enter your surname")

        self.name.move(10, 10)
        self.surname.move(10, 40)
        self.male.move(10, 70)
        self.female.move(70, 70)
        submitButton.move(30, 100)

        submitButton.clicked.connect(self.getValues)

    def getValues(self):
        name = self.name.text()
        surname = self.surname.text()
        if self.male.isChecked():
            gender = "Male"
        else:
            gender = "Female"
        print(f"name - {name}\nsurname - {surname}\ngender - {gender}")


def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())


if __name__ == '__main__':
    main()
