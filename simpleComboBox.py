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
        self.text1 = QLabel('Where do you live?', self)
        self.combo1 = QComboBox(self)
        saveButton = QPushButton("Save",self)

        self.text1.move(130,130)
        self.combo1.move(270,128)
        saveButton.move(170,170)


        # add items to comboBox
        countries = ["Germany","Italy","Czech", "Norway","Russia","Finland","Ireland","Latvia"]
        self.combo1.addItems(countries)

        saveButton.clicked.connect(self.getValue)

    def getValue(self):
        print(f"You live in {self.combo1.currentText()}") 

def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())

if __name__ == '__main__':
    main()
