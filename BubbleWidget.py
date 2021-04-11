from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from Target import Target
from BubbleCursor import BubbleCursor
from RopeCursor import RopeCursor
import csv

class BubbleWidget(QWidget):
    def __init__(self, type, fileBubble,fileSelectedTarget, currentUserNb, method, density, currentTargetSize):
        QWidget.__init__(self)
        self.targets = []
        # chargé les fichier csv
        self.createTargets(fileBubble)
        self.createSelectedTargets(fileSelectedTarget)

        if(type=="Rope"):
            self.cursor = RopeCursor(self.targets, currentUserNb, method, density, currentTargetSize)
        else :
            self.cursor = BubbleCursor(self.targets, currentUserNb, method, density, currentTargetSize)


    def paintEvent(self, event):
        painter = QPainter(self)
        self.cursor.paint(painter)
        for target in self.targets:
            target.paint(painter)

    def mouseMoveEvent(self, event):
        self.cursor.move(event.x(), event.y())
        self.update()
    
    def createTargets(self, filename):
        with open(filename, 'r') as bubbles:
            reader = csv.reader(bubbles)
            for row in reader:
                self.targets.append(Target(int(row[0]), int(row[1]), int(row[2])))

    def createSelectedTargets(self, filename):
        with open(filename, 'r') as selected:
            reader = csv.reader(selected)
            for row in reader:
                self.targets[int(row[0])].toSelect = True

        
