import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont


myFont1 = QFont("Boardway", 16)

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(150, 250, 500, 350)
        self.setWindowTitle('SpinBox Example')
        self.UI()
        self.show()

    def UI(self):
        self.ball1 = QLabel("O", self)
        self.spin_box1 = QSpinBox(self)
        self.spin_box2 = QSpinBox(self)

        self.spin_box1.move(420, 270)
        self.spin_box2.move(420, 310)

        self.ball1.setFont(myFont1)
        self.spin_box1.setFont(myFont1)
        self.spin_box2.setFont(myFont1)

        self.spin_box1.valueChanged.connect(self.ballPosition)
        self.spin_box2.valueChanged.connect(self.ballPosition)

        self.spin_box1.setSingleStep(25)
        self.spin_box2.setSingleStep(25)

        self.spin_box1.setMaximum(350)
        self.spin_box2.setMaximum(300)

        self.spin_box1.setPrefix("X: ")
        self.spin_box2.setPrefix("Y: ")

    def ballPosition(self):
        self.ball1.move(self.spin_box1.value(), self.spin_box2.value())

App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())
