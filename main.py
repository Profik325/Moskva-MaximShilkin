from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
import sys


class Widget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.button_one = QPushButton(self, 'create a circle')

    def Button_one(self):



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Widget()
    ex.show()
    sys.exit(app.exec())