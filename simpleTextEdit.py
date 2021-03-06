import sys
from PyQt5.QtWidgets import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(150, 250, 500, 350)
        self.setWindowTitle('Text Edit Example')
        self.UI()
        self.show()

    def UI(self):
        self.editor = QTextEdit(self)
        self.editor.move(5, 150)
        self.editor.setAcceptRichText(False)  # disable different text fonts
        self.editor.resize(480, 100)

        button = QPushButton("Save", self)
        button.clicked.connect(self.handling)
        button.move(220, 300)

    def handling(self):
        textEditData = str(self.editor.toPlainText())
        message = QMessageBox.information(self, "Your input", textEditData)


def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())


if __name__ == '__main__':
    main()
