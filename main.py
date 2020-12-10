import sys, random
from UI import Ui_MainWindow
from PyQt5.QtGui import QPainter, QColor, QFont
from PyQt5.QtWidgets import *


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.rb1.clicked.connect(self.col1)
        self.cirk = []

    def col1(self):
        a = random.randint(0, 100)
        b = random.randint(0, 240)
        c = random.randint(0, 250)
        self.cirk.append((b, c, a, a))
        self.repaint()

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.draw(qp)
        qp.end()

    def draw(self, qp):
        col = QColor()
        col.setNamedColor('yellow')
        for i in range(len(self.cirk)):
            qp.setBrush(col)
            qp.drawEllipse(self.cirk[i][0], self.cirk[i][1], self.cirk[i][2], self.cirk[i][2])
            print(self.cirk[i][0], self.cirk[i][1], self.cirk[i][2], self.cirk[i][2])

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())