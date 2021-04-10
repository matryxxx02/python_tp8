import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from BubbleWidget import *
from NormalWidget import *
from ExpSetup import *

def main(args):
	app = QApplication(sys.argv)
	mainWindow = MainWindow()
	mainWindow.show()
	sys.exit(app.exec_())

class MainWindow(QMainWindow):
	def __init__(self):
		QMainWindow.__init__(self)
		self.setWindowTitle("Bubble cursor")
		self.resize(1024, 800)
		self.dialog = ExpSetup()
		userNb,	method, density, targetSize, repetitions = self.dialog.launchSetup()
		print(userNb,
		method,
		density,
		targetSize,
		repetitions)

		if(method=="Highlight"):
			self.widget = NormalWidget()
		elif (method=="Rope") :
			self.widget = BubbleWidget("Rope")
		else :
			self.widget = BubbleWidget("Bubble")
		self.setCentralWidget(self.widget)

if __name__ == "__main__":
	main(sys.argv)