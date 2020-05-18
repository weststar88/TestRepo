import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QLCDNumber, QPushButton, QHBoxLayout, QVBoxLayout, QAction, qApp, QLineEdit
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSignal
from enum import Enum

class CalculatorOperator(Enum):
    Init = 0
    Plus = 1
    Minus = 2
    Multiply = 3
    Divide = 4

class calculatorWidget(QWidget):

    def __init__(self, plusSignal, minusSignal, multiplySignal, divideSignal, equalSignal, qleSignal):
        super().__init__()

        self.qle = QLineEdit(self)
        self.qle.textChanged[str].connect(qleSignal)

        self.plusBtn = QPushButton('+', self)
        self.plusBtn.resize(self.plusBtn.sizeHint())
        self.plusBtn.clicked.connect(plusSignal)

        self.minusBtn = QPushButton('-', self)
        self.minusBtn.resize(self.minusBtn.sizeHint())
        self.minusBtn.clicked.connect(minusSignal)

        self.multiplyBtn = QPushButton('*', self)
        self.multiplyBtn.resize(self.multiplyBtn.sizeHint())
        self.multiplyBtn.clicked.connect(multiplySignal)

        self.divideBtn = QPushButton('/', self)
        self.divideBtn.resize(self.divideBtn.sizeHint())
        self.divideBtn.clicked.connect(divideSignal)

        self.equalBtn = QPushButton('=', self)
        self.equalBtn.resize(self.equalBtn.sizeHint())
        self.equalBtn.clicked.connect(equalSignal)

        self.hbox = QHBoxLayout()
        self.hbox.addStretch(1)
        self.hbox.addWidget(self.plusBtn)
        self.hbox.addWidget(self.minusBtn)
        self.hbox.addWidget(self.multiplyBtn)
        self.hbox.addWidget(self.divideBtn)
        self.hbox.addStretch(1)

        self.vbox = QVBoxLayout()
        self.vbox.addStretch(1)
        self.vbox.addWidget(self.qle)
        self.vbox.addStretch(1)
        self.vbox.addLayout(self.hbox)
        self.vbox.addStretch(1)
        self.vbox.addWidget(self.equalBtn)
        self.vbox.addStretch(1)

        self.setLayout(self.vbox)

    def setQleText(self, text):
        self.qle.setText(text)

class MyApp(QMainWindow):
    currentValue = 0
    processValue = 0
    myOperator = CalculatorOperator.Init

    def __init__(self):
        super().__init__()
        self.MakeCalCulatorWidget()
        self.MakeExitMenu()

        self.statusBar()
        self.setWindowTitle('Calculator')
        self.setGeometry(300, 300, 300, 200)
        self.show()

    def MakeCalCulatorWidget(self):
        self.calculatorInstance = calculatorWidget(self.Plus, self.Minus, self.Multiply, self.Divide, self.Equal, self.onTextChanged)
        self.setCentralWidget(self.calculatorInstance)

    def MakeExitMenu(self):
        exitAction = QAction(QIcon('exit.png'), 'Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(qApp.quit)

        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)
        filemenu = menubar.addMenu('&File')
        filemenu.addAction(exitAction)

    def SetStatusBar(self, message):
        self.statusBar().showMessage(str(message))

    def Calculate(self):
        if self.myOperator is CalculatorOperator.Plus:
            self.processValue += self.currentValue
        elif self.myOperator is CalculatorOperator.Minus:
            self.processValue -= self.currentValue
        elif self.myOperator is CalculatorOperator.Multiply:
            self.processValue *= self.currentValue
        elif self.myOperator is CalculatorOperator.Divide:
            value = self.processValue / self.currentValue
            self.processValue = int(value)
        else:
            self.processValue = self.currentValue

    def Plus(self):
        self.Calculate()
        self.currentValue = 0
        self.calculatorInstance.setQleText(str(self.currentValue))
        self.myOperator = CalculatorOperator.Plus
        self.SetStatusBar('{} {}'.format(self.processValue, '+'))

    def Minus(self):
        self.Calculate()
        self.currentValue = 0
        self.calculatorInstance.setQleText(str(self.currentValue))
        self.myOperator = CalculatorOperator.Minus
        self.SetStatusBar('{} {}'.format(self.processValue, '-'))

    def Multiply(self):
        self.Calculate()
        self.currentValue = 0
        self.calculatorInstance.setQleText(str(self.currentValue))
        self.myOperator = CalculatorOperator.Multiply
        self.SetStatusBar('{} {}'.format(self.processValue, '*'))

    def Divide(self):
        self.Calculate()
        self.currentValue = 0
        self.calculatorInstance.setQleText(str(self.currentValue))
        self.myOperator = CalculatorOperator.Divide
        self.SetStatusBar('{} {}'.format(self.processValue, '/'))

    def Equal(self):
        self.Calculate()
        self.currentValue = self.processValue
        self.calculatorInstance.setQleText(str(self.currentValue))
        self.processValue = 0
        self.myOperator = CalculatorOperator.Init
        self.SetStatusBar('')

    def onTextChanged(self, text):
        self.currentValue = int(text)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())