from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class ExpSetup(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        layout = self.initUi()
        self.setGeometry(300, 300, 300, 150)
        self.setWindowTitle("Setup")
        self.setWindowModality(Qt.ApplicationModal)
        self.setLayout(layout)

    def initUi(self):

        # init layouts and widgets
        # selection method
        self.methods = self.combobox(["Highlight", "Bubble", "Rope"])
        hLayoutMethods = QHBoxLayout()
        hLayoutMethods.addWidget(QLabel("methods :"))
        hLayoutMethods.addWidget(self.methods)

        # user number
        hLayoutUserNb = QHBoxLayout()
        hLayoutUserNb.addWidget(QLabel("user number :"))
        self.userNb = self.spinbox("userNb")
        hLayoutUserNb.addWidget(self.userNb)

        # density
        hLayoutDensity = QHBoxLayout()
        hLayoutDensity.addWidget(QLabel("density :"))
        self.density = self.combobox(["30", "60", "90"])
        hLayoutDensity.addWidget(self.density)

        # nombre de tailles de cibles
        hLayoutTargetsSize = QHBoxLayout()
        hLayoutTargetsSize.addWidget(QLabel("nombre de tailles de cibles :"))
        self.targetSize = self.combobox(["6", "12", "18"])
        hLayoutTargetsSize.addWidget(self.targetSize)

        # repetitions
        hLayoutRepetitions = QHBoxLayout()
        hLayoutRepetitions.addWidget(QLabel("repetitions :"))
        self.repetitions = self.spinbox("repetitions")
        hLayoutRepetitions.addWidget(self.repetitions)

        #init next button
        nextButton = QPushButton("next",self)
        nextButton.clicked.connect(self.accept)

        mainLayout = QVBoxLayout()
        mainLayout.addLayout(hLayoutUserNb)
        mainLayout.addLayout(hLayoutDensity)
        mainLayout.addLayout(hLayoutMethods)
        mainLayout.addLayout(hLayoutTargetsSize)
        mainLayout.addLayout(hLayoutRepetitions)
        mainLayout.addWidget(nextButton)
        return mainLayout

    def launchBubble(self):
        self.accept()
        return "true"

    def launchSetup(self):
        dlg = ExpSetup()
        r = dlg.exec_()
        if r:
            return dlg.getValues()
        return None

    def getValues(self):
        return self.userNb.value(), self.methods.currentText(), self.density.currentText(), self.targetSize.currentText(), self.repetitions.value()

    # generate selection method combobox
    def combobox(self, values):
        combo = QComboBox()
        combo.addItems(values)
        return combo;
        
    # generator of spinbox
    def spinbox(self, value):
        sb = QSpinBox()
        #init spinbox values
        if(value=="userNb"):
            sb.setValue(1)
        elif(value=="repetitions"):
            sb.setValue(1)
        return sb
        

