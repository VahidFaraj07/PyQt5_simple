import sys
from PyQt5.QtWidgets import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(150, 250, 500, 350)
        self.setWindowTitle('List Widget Example')
        self.UI()
        self.show()

    def UI(self):
        self.newRecord = QLineEdit(self)
        self.listWidget = QListWidget(self)
        self.newRecord.move(10, 10)
        self.listWidget.move(10, 50)
        self.listWidget.resize(300, 250)

        self.planets = ['Merkuri', 'Venera', 'Yer', 'Mars',
                        'Yupiter', 'Saturn', 'Uran', 'Neptun', 'Pluton']
        self.listWidget.addItems(self.planets)

        addButton = QPushButton('Add', self)
        delButton = QPushButton('Delete', self)

        addButton.move(350, 50)
        delButton.move(350, 80)

        addButton.clicked.connect(self.addUnit)
        delButton.clicked.connect(self.delUnit)

    def addUnit(self):
        self.listWidget.addItem(self.newRecord.text())
        self.newRecord.setText('')
        self.planets.clear()
        for index in range(self.listWidget.count()):
            self.planets.append(self.listWidget.item(index).text())

    def delUnit(self):
        rowID = self.listWidget.currentRow()
        self.listWidget.takeItem(rowID)
        self.planets.clear()
        for index in range(self.listWidget.count()):
            self.planets.append(self.listWidget.item(index).text())


def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())


if __name__ == '__main__':
    main()
