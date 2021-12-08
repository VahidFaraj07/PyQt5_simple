from PyQt5.QtWidgets import *
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(200, 300, 500, 400)
        self.setWindowTitle('Button Example')
        self.UI()
        self.show()

    def UI(self):
        self.text = QLabel('Choose your way', self)
        self.text.move(200, 100)
        enterButton = QPushButton("Enter", self)
        exitButton = QPushButton("Exit", self)

        enterButton.move(150, 150)
        exitButton.move(250, 150)

        enterButton.clicked.connect(self.enterFunc)
        exitButton.clicked.connect(self.exitFunc)
        
    def enterFunc(self):
        self.text.setText("You clicked Enter")
        self.text.resize(250,300)

    def exitFunc(self):
        self.text.setText("You clicked Exit")
        self.text.resize(250,300)     

def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())

if __name__ == '__main__':
    main()
