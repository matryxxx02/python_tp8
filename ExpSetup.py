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

        # init widgets
        self.comboboxMethod()

        # init layouts
        # selection method
        hLayoutMethods = QHBoxLayout()
        hLayoutMethods.addWidget(QLabel("methods :"))
        hLayoutMethods.addWidget(self.methods)

        # user number
        hLayoutUserNb = QHBoxLayout()
        hLayoutUserNb.addWidget(QLabel("user number :"))
        self.userNb = self.spinbox("userNb")
        hLayoutUserNb.addWidget(self.userNb)

        # density
        hLayoutUserNb = QHBoxLayout()
        hLayoutUserNb.addWidget(QLabel("density :"))
        self.density = self.spinbox("density")
        hLayoutUserNb.addWidget(self.density)

        # nombre de tailles de cibles
        hLayoutTargetsSize = QHBoxLayout()
        hLayoutTargetsSize.addWidget(QLabel("nombre de tailles de cibles :"))
        self.targetSize = self.spinbox("targets")
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
        return self.userNb.value(), self.methods.currentText(), self.density.value(), self.targetSize.value(), self.repetitions.value()

    # generate selection method combobox
    def comboboxMethod(self):
        self.methods = QComboBox()
        # init combobox values
        self.methods.addItems(["Highlight", "Bubble", "Rope"])
        
    # generator of spinbox
    def spinbox(self, value):
        sb = QSpinBox()
        #init spinbox values
        if(value=="userNb"):
            sb.setValue(1)
        elif(value=="density"):
            sb.setValue(60)
        elif(value=="targets"):
            sb.setValue(12)
        elif(value=="repetitions"):
            sb.setValue(1)
        return sb
        

