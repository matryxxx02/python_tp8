from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from Target import Target
from BubbleCursor import BubbleCursor
from RopeCursor import RopeCursor
import csv

class BubbleWidget(QWidget):
    def __init__(self, type):
        QWidget.__init__(self)
        self.targets = []
        # chargé le fichier targets.csv
        with open('src_tp_bubble.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                self.targets.append(Target(int(row[0]), int(row[1]), int(row[2])))
        if(type=="Rope"):
            self.cursor = RopeCursor(self.targets)
        else :
            self.cursor = BubbleCursor(self.targets)


    def paintEvent(self, event):
        painter = QPainter(self)
        self.cursor.paint(painter)
        for target in self.targets:
            target.paint(painter)

    def mouseMoveEvent(self, event):
        self.cursor.move(event.x(), event.y())
        self.update()

        
