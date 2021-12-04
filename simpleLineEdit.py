from PyQt5.QtWidgets import *
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(200, 300, 500, 400)
        self.setWindowTitle('LineEdit Example')
        self.UI()
        self.show()

    def UI(self):
        self.usernameTextBox = QLineEdit(self)
        self.passTextBox = QLineEdit(self)

        self.usernameTextBox.move(50,50)
        self.passTextBox.move(50,100)

        self.usernameTextBox.setPlaceholderText("Enter username")
        self.passTextBox.setPlaceholderText("Enter password")

        # for hide password 
        self.passTextBox.setEchoMode(QLineEdit.Password)

        saveButton = QPushButton("Save",self)
        saveButton.move(230,100)
        saveButton.clicked.connect(self.getValues)


    def getValues(self):
        username = self.usernameTextBox.text()
        password = self.passTextBox.text()

        print(f"username: {username} and password: {password}")



def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())


if __name__ == '__main__':
    main()
