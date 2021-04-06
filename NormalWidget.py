from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from MainBubble import Target
from NormalCursor import NormalCursor
import csv

class NormalWidget(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.targets = []
        # chargé le fichier targets.csv
        with open('src_tp_bubble.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                self.targets.append(Target(int(row[0]), int(row[1]), int(row[2])))
        self.cursor = NormalCursor(self.targets)

    def paintEvent(self, event):
        painter = QPainter(self)
        for target in self.targets:
            target.paint(painter)
        # self.cursor.paint(painter)

    def mouseMoveEvent(self, event):
        self.cursor.select(event.x(), event.y())
        self.update()

        
