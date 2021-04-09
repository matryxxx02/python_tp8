from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from math import sqrt
import random
import time 

class BubbleCursor(QWidget):
    def __init__(self, targets):
        QWidget.__init__(self)
        self.defaultColor = QColor(134, 245, 95)
        self.x = 0
        self.y = 0
        self.size = 10
        self.targets = targets
        self.closest = None
        self.selected = None #self.randomSelector()
        # self.selected.toSelect = True
        self.timer = time.time()

    def paint(self, painter):
        painter.setPen(QPen(self.defaultColor, 1))
        painter.drawEllipse(QPoint(self.x, self.y), self.size, self.size)

    def move(self, x, y):
        self.x = x
        self.y = y
        closest = self.targets[0]
        if (self.closest != None):
            self.closest.toSelect = False

        minDist = self.distance(x,y,closest)
        for target in self.targets:
            newDist = self.distance(x, y, target)
            if (newDist < minDist):
                minDist = newDist
                closest = target
                # self.closest.toSelect = True
        self.size = minDist
        self.closest = closest
        self.closest.toSelect = True

    def select(self, x, y):
        distance = self.distance(x, y, self.selected)
        if (distance <= 0):
            newTime = time.time()
            print("temps de selection :", newTime - self.timer)
            self.timer = newTime
            self.selected.toSelect = False
            self.selected = self.randomSelector()
            self.selected.toSelect = True
        
    def randomSelector(self):
        return self.targets[random.randint(0,len(self.targets))]


    def distance(self, cursorx, cursory, target):
        x = (target.x - cursorx) ** 2
        y = (target.y - cursory) ** 2
        return sqrt(x+y) - target.size/2