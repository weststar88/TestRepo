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
    def __init__(self):
        super().__init__()

    def initUI(self, plusSignal, minusSignal, multiplySignal, divideSignal, equalSignal, qleSignal):
        qle = QLineEdit(self)
        qle.textChanged[str].connect(qleSignal)

        plusBtn = QPushButton('+', self)
        plusBtn.resize(plusBtn.sizeHint())
        plusBtn.clicked.connect(plusSignal)

        minusBtn = QPushButton('-', self)
        minusBtn.resize(minusBtn.sizeHint())
        minusBtn.clicked.connect(minusSignal)

        multiplyBtn = QPushButton('*', self)
        multiplyBtn.resize(multiplyBtn.sizeHint())
        multiplyBtn.clicked.connect(multiplySignal)

        divideBtn = QPushButton('/', self)
        divideBtn.resize(divideBtn.sizeHint())
        divideBtn.clicked.connect(divideSignal)

        equalBtn = QPushButton('=', self)
        equalBtn.resize(equalBtn.sizeHint())
        equalBtn.clicked.connect(equalSignal)

        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(plusBtn)
        hbox.addWidget(minusBtn)
        hbox.addWidget(multiplyBtn)
        hbox.addWidget(divideBtn)
        hbox.addStretch(1)

        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addWidget(qle)
        vbox.addStretch(1)
        vbox.addLayout(hbox)
        vbox.addStretch(1)
        vbox.addWidget(equalBtn)
        vbox.addStretch(1)

        self.setLayout(vbox)


class MyApp(QMainWindow):
    currentValue = 0
    processValue = 0
    myOperator = CalculatorOperator.Init

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.MakeCalCulatorWidget()
        self.MakeExitMenu()

        self.statusBar()
        self.setWindowTitle('Calculator')
        self.setGeometry(300, 300, 300, 200)
        self.show()

    def MakeCalCulatorWidget(self):
        calculatorInstance = calculatorWidget()
        calculatorInstance.initUI(self.Plus, self.Minus, self.Multiply, self.Divide, self.Equal, self.onTextChanged)
        self.setCentralWidget(calculatorInstance)

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
            self.processValue /= self.currentValue
        else:
            self.processValue = self.currentValue

    def Plus(self):
        self.Calculate()
        self.SetStatusBar(self.processValue)
        self.myOperator = CalculatorOperator.Plus

    def Minus(self):
        self.Calculate()
        self.SetStatusBar(self.processValue)
        self.myOperator = CalculatorOperator.Minus

    def Multiply(self):
        self.Calculate()
        self.SetStatusBar(self.processValue)
        self.myOperator = CalculatorOperator.Multiply

    def Divide(self):
        self.Calculate()
        self.SetStatusBar(self.processValue)
        self.myOperator = CalculatorOperator.Divide

    def Equal(self):
        self.Calculate()
        self.SetStatusBar()
        # lineEdit에 입력해야됨
        self.myOperator = CalculatorOperator.Init
        self.processValue = 0

    def onTextChanged(self, text):
        self.currentValue = int(text)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())