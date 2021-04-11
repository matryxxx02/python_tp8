from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from math import sqrt
import datetime

class NormalCursor(QWidget):
    def __init__(self, targets, currentUserNb, method, density, currentTargetSize):
        QWidget.__init__(self)
        self.targets = targets
        self.selected = None
        self.currentUserNb = currentUserNb
        self.method = method
        self.density = density
        self.currentTargetSize = currentTargetSize

    def select(self, x, y):
        selectedTarget = "cible non selectionnee"
        numTarget = None
        if (self.selected != None):
            self.selected.toSelect = False
        for idx, target in enumerate(self.targets):
            distance = self.distance(x, y, target)
            if (distance <= 0):
                if (target.toSelect == True and self.selected != None and not (target.x == self.selected.x and target.y == self.selected.y)):
                    selectedTarget = "cible selectionnee"
                    numTarget = idx
                target.toSelect = True
                self.selected = target
        result = str(self.currentUserNb)+","+self.method+","+str(self.density)+","+str(self.currentTargetSize)+","+str(numTarget)+","+str(datetime.datetime.now())+","+selectedTarget
        self.writeResultInCSV(result)
        print(result)


    def distance(self, cursorx, cursory, target):
        x = (target.x - cursorx) ** 2
        y = (target.y - cursory) ** 2
        return sqrt(x + y) - target.size
        
    def writeResultInCSV(self, result):
        with open('result.csv', 'a') as file:
            file.write(result+"\n")
            file.close()