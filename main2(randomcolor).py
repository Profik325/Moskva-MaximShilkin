from random import randint

from PyQt6.QtCore import QPointF
from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
import sys


def RColorandSize():
    return randint(0, 255), randint(0, 255), randint(0, 255), randint(20, 100)


class Widget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.button_one = QPushButton(parent=self, text='create a circle')
        self.setGeometry(500, 500, 300, 300)
        self.paint = False
        self.button_one.clicked.connect(self.Button_one)

        self.qp = QPainter()

    def paintEvent(self, a0):
        if self.paint:
            self.qp.begin(self)
            r, g, b, size = RColorandSize()
            self.qp.setBrush(QColor(r, g, b))
            pos = QPointF(150.0, 150.0)
            self.qp.drawEllipse(pos, size, size)
            self.paint = False
            self.qp.end()

    def Button_one(self):
        self.paint = True
        self.repaint()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Widget()
    ex.show()
    sys.exit(app.exec())