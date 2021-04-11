import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from BubbleWidget import *
from NormalWidget import *
from ExpSetup import *
from XPManager import *

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

		manager = XPManager(userNb, method, density, targetSize, repetitions)
		self.setCentralWidget(manager.choiceCursor())

if __name__ == "__main__":
	main(sys.argv)