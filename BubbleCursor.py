from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from math import sqrt
import random
import time 
import datetime
from csv import writer

class BubbleCursor(QWidget):
    def __init__(self, targets, currentUserNb, method, density, currentTargetSize):
        QWidget.__init__(self)
        self.defaultColor = QColor(134, 245, 95)
        self.x = 0
        self.y = 0
        self.size = 10
        self.targets = targets
        self.closest = None
        self.currentUserNb = currentUserNb
        self.method = method
        self.density = density
        self.currentTargetSize = currentTargetSize
        self.selected = None #self.randomSelector()
        # self.selected.toSelect = True
        # self.timer = time.time()

    def paint(self, painter):
        painter.setPen(QPen(self.defaultColor, 1))
        painter.drawEllipse(QPoint(self.x, self.y), self.size, self.size)

    def move(self, x, y):
        self.x = x
        self.y = y
        closest = self.targets[0]
        if(self.closest!= None):
            self.closest.toSelect = False
        selectedTarget = "cible non selectionne"
        numTarget = None
        minDist = self.distance(x,y,closest)
        for idx, target in enumerate(self.targets):
            newDist = self.distance(x, y, target)
            if (newDist < minDist):
                minDist = newDist
                closest = target
                numTarget = idx
        if(closest.toSelect == True):
            selectedTarget = "cible selectionnee"
        if self.closest != None and not (closest.x == self.closest.x and closest.y == self.closest.y):
            result = str(self.currentUserNb)+","+self.method+","+str(self.density)+","+str(self.currentTargetSize)+","+str(numTarget)+","+str(datetime.datetime.now())+","+selectedTarget
            self.writeResultInCSV(result)
            print(result)
            
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
        return sqrt(x + y) - target.size / 2
        
    def writeResultInCSV(self, result):
        with open('result.csv', 'a') as file:
            file.write(result+"\n")
            file.close()