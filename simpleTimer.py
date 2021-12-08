import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QTimer


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(150, 250, 500, 350)
        self.setWindowTitle('Timer Example')
        self.UI()
        self.show()

    def UI(self):
        self.emptyTextLabel = QLabel(self)
        self.emptyTextLabel.resize(200, 300)
        self.emptyTextLabel.setStyleSheet("background-color:red")
        self.emptyTextLabel.move(10, 10)

        startButton = QPushButton("Start", self)
        stopButton = QPushButton("Stop", self)
        startButton.move(250, 150)
        stopButton.move(350, 150)
        startButton.clicked.connect(self.start)
        startButton.clicked.connect(self.stop)


        self.time
        self.myTimer = QTimer()
        self.myTimer.setInterval(10)
        self.myTimer.timeout.connect(self.changeColor)
        self.value = 0
        

    def changeColor(self):
        if self.value == 0:
            self.emptyTextLabel.setStyleSheet("background-color:green")
            self.value = 1
        else:
            self.emptyTextLabel.setStyleSheet("background-color:yellow")
            self.value = 0

    def start(self):
        self.myTimer.start()

    def stop(self):
        self.myTimer.stop()


def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())


if __name__ == '__main__':
    main()
