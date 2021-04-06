from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class ExpSetup(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        b1 = QPushButton("ok",self)
        self.setWindowTitle("Dialog")
        self.setWindowModality(Qt.ApplicationModal)
