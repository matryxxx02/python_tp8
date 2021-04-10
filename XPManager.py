from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from BubbleWidget import *
from NormalWidget import *

class XPManager():
    def __init__(self, userNb,	method, density, targetSize, repetitions):
        self.targetSize = []
        self.density = []
        self.method = method
        self.currentDensity = density
        self.currentTargetSize = targetSize
        self.currentRepetitions = repetitions

    def choiceCursor(self):
        fileBubble = "bubble"+self.currentDensity+"x"+self.currentTargetSize+".csv"
        fileSelectedTarget = "selected"+self.currentDensity+"x"+self.currentTargetSize+".csv"
        if(self.method=="Highlight"):
			return NormalWidget(fileBubble,fileSelectedTarget)
		elif (self.method=="Rope") :
			return BubbleWidget("Rope",fileBubble,fileSelectedTarget)
		else :
			return BubbleWidget("Bubble",fileBubble,fileSelectedTarget)