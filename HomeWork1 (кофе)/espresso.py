from PyQt6.QtCore import QPointF
from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
import sys
from PyQt6 import uic
import sqlite3


class Widget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('espresso_main.ui', self)
        self.setGeometry(250, 250, 1040, 340)

    def initTable(self):
        con = sqlite3.connect('coffe.db')
        cur = con.cursor()
        end_res = []
        avg_l = []
        f = '5'

        for x in a:
            result = cur.execute(f"""SELECT DISTINCT name, strength FROM Trolls 
                        WHERE strength > 5 AND place = '{x}'""").fetchall()

            for y in result:
                end_res.append(y[0])
                avg_l.append(y[1])


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Widget()
    ex.show()
    sys.exit(app.exec())
