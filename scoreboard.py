import sys
from PyQt4 import QtGui, QtCore

class Window(QtGui.QMainWindow):

    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(50, 50, 1000, 300)
        self.setWindowTitle("Scoreboard")
        self.setWindowIcon(QtGui.QIcon('pic.png'))

        extractAction = QtGui.QAction("TEST", self)
        extractAction.setShortcut("Ctrl+Q")
        extractAction.setStatusTip('Leave The App')
        extractAction.triggered.connect(self.close_application)

        self.statusBar()

        mainMenu = self.menuBar();
        fileMenu = mainMenu.addMenu('File')
        fileMenu.addAction(extractAction)
        
        self.initUI()

    def initUI(self):
            
        scoreFont = QtGui.QFont()
        scoreFont.setBold(True)
        scoreFont.setPointSize(36)
        
        labelP1 = QtGui.QLabel("Player 1", self)
        labelP1.move(15, 10)
        labelP2 = QtGui.QLabel("Player 2", self)
        labelP2.move(930, 10)
        
        self.textboxP1 = QtGui.QLineEdit(self)
        self.textboxP1.move(80, 10)
        self.textboxP1.resize(150,30)
        self.textboxP2 = QtGui.QLineEdit(self)
        self.textboxP2.move(770, 10)
        self.textboxP2.resize(150,30)
        
        self.scoreP1 = QtGui.QLineEdit(self)
        self.scoreP1.move(130, 50)
        self.scoreP1.resize(50, 50)
        self.scoreP1.setAlignment(QtCore.Qt.AlignCenter)
        self.scoreP1.setFont(scoreFont)
        self.scoreP1.setText("0");

        self.scoreP2 = QtGui.QLineEdit(self)
        self.scoreP2.move(820, 50)
        self.scoreP2.resize(50, 50)
        self.scoreP2.setAlignment(QtCore.Qt.AlignCenter)
        self.scoreP2.setFont(scoreFont)
        self.scoreP2.setText("0");
        
        p1plus = QtGui.QPushButton(">", self)
        p1plus.clicked.connect(self.increment_P1)
        p1plus.resize(40, 20)
        p1plus.move(180, 65)
        p1minus = QtGui.QPushButton("<", self)
        p1minus.clicked.connect(self.decrement_P1)
        p1minus.resize(40, 20)
        p1minus.move(90, 65)
        p2plus = QtGui.QPushButton(">", self)
        p2plus.clicked.connect(self.increment_P2)
        p2plus.resize(40, 20)
        p2plus.move(870, 65)
        p2minus = QtGui.QPushButton("<", self)
        p2minus.clicked.connect(self.decrement_P2)
        p2minus.resize(40, 20)
        p2minus.move(780, 65)

        swap = QtGui.QPushButton("Swap", self)
        swap.clicked.connect(self.swap)
        swap.resize(40, 40)
        swap.move(250, 65)
        self.show()

    def increment_P1(self):
        num = self.scoreP1.text().toInt()
        if num[0] < 9:
            new = num[0] + 1
        else:
            new = num[0]
        self.scoreP1.setText(str(new))

    def decrement_P1(self):
        num = self.scoreP1.text().toInt()
        if num[0] > 0:
            new = num[0] - 1
        else:
            new = num[0]
        self.scoreP1.setText(str(new))

    def increment_P2(self):
        num = self.scoreP2.text().toInt()
        if num[0] < 9:
            new = num[0] + 1
        else:
            new = num[0]
        self.scoreP2.setText(str(new))

    def decrement_P2(self):
        num = self.scoreP2.text().toInt()
        if num[0] > 0:
            new = num[0] - 1
        else:
            new = num[0]
        self.scoreP2.setText(str(new))
            
    def swap(self):
        p1 = self.textboxP1.text()
        p2 = self.textboxP2.text()
        self.textboxP1.setText(p2)
        self.textboxP2.setText(p1)
        
    def close_application(self):
        sys.exit()
        
def main():
    app = QtGui.QApplication(sys.argv)
    GUI = Window()
    app.exec_()
    sys.exit()

main()