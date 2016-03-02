import sys
from PyQt4 import QtGui, QtCore

class Window(QtGui.QMainWindow):

    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(50, 50, 600, 210)
        self.setWindowTitle("Scoreboard")
        self.setWindowIcon(QtGui.QIcon('pic.png'))

        close = QtGui.QAction("Quit", self)
        close.setShortcut("Ctrl+Q")
        close.setStatusTip('Leave The App')
        close.triggered.connect(self.close_application)

        about = QtGui.QAction("About", self)
        about.setShortcut("Ctrl+H")
        about.setStatusTip('About this app')
        about.triggered.connect(self.display_info)

        self.statusBar()

        mainMenu = self.menuBar();
        fileMenu = mainMenu.addMenu('Menu')
        fileMenu.addAction(about)
        fileMenu.addAction(close)
        
        
        self.initUI()

    def initUI(self):
            
        scoreFont = QtGui.QFont()
        scoreFont.setBold(True)
        scoreFont.setPointSize(36)
        
        labelP1 = QtGui.QLabel("Player 1", self)
        labelP1.move(15, 10)
        labelP2 = QtGui.QLabel("Player 2", self)
        labelP2.move(530, 10)
        labelP2 = QtGui.QLabel("Player 2", self)
        labelP2.move(530, 10)

        labelA = QtGui.QLabel("Match", self)
        labelA.move(25, 115)
        labelB = QtGui.QLabel("Camera", self)
        labelB.move(530, 115)
        labelC = QtGui.QLabel("Misc. 1", self)
        labelC.move(23, 150)
        labelD = QtGui.QLabel("Misc. 2", self)
        labelD.move(530, 150)
        
        self.textboxP1 = QtGui.QLineEdit(self)
        self.textboxP1.move(80, 10)
        self.textboxP1.resize(150,30)
        self.textboxP2 = QtGui.QLineEdit(self)
        self.textboxP2.move(370, 10)
        self.textboxP2.resize(150,30)

        self.textboxA = QtGui.QLineEdit(self)
        self.textboxA.move(80, 115)
        self.textboxA.resize(150,30)
        self.textboxB = QtGui.QLineEdit(self)
        self.textboxB.move(370, 115)
        self.textboxB.resize(150,30)
        self.textboxC = QtGui.QLineEdit(self)
        self.textboxC.move(80, 150)
        self.textboxC.resize(150,30)
        self.textboxD = QtGui.QLineEdit(self)
        self.textboxD.move(370, 150)
        self.textboxD.resize(150,30)
        
        self.scoreP1 = QtGui.QLineEdit(self)
        self.scoreP1.move(130, 50)
        self.scoreP1.resize(50, 50)
        self.scoreP1.setAlignment(QtCore.Qt.AlignCenter)
        self.scoreP1.setFont(scoreFont)
        self.scoreP1.setText("0");

        self.scoreP2 = QtGui.QLineEdit(self)
        self.scoreP2.move(420, 50)
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
        p2plus.move(470, 65)
        p2minus = QtGui.QPushButton("<", self)
        p2minus.clicked.connect(self.decrement_P2)
        p2minus.resize(40, 20)
        p2minus.move(380, 65)

        swap = QtGui.QPushButton("Swap", self)
        swap.clicked.connect(self.swap)
        swap.resize(100, 30)
        swap.move(250, 10)

        reset = QtGui.QPushButton("Reset", self)
        reset.clicked.connect(self.reset)
        reset.resize(100, 40)
        reset.move(250, 55)

        save = QtGui.QPushButton("Update", self)
        save.clicked.connect(self.save)
        save.resize(100, 65)
        save.move(250, 115)
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

    def reset(self):
        self.textboxP1.setText("")
        self.textboxP2.setText("")
        self.scoreP1.setText("0")
        self.scoreP2.setText("0")

    def save(self):
        with open("info/player1.txt", "w") as text_file:
            text_file.write("%s" % self.textboxP1.text())

        with open("info/player2.txt", "w") as text_file:
            text_file.write("%s" % self.textboxP2.text())

        with open("info/p1score.txt", "w") as text_file:
            text_file.write("%s" % self.scoreP1.text())

        with open("info/p2score.txt", "w") as text_file:
            text_file.write("%s" % self.scoreP2.text())

        with open("info/match.txt", "w") as text_file:
            text_file.write("%s" % self.textboxA.text())

        with open("info/camera.txt", "w") as text_file:
            text_file.write("%s" % self.textboxB.text())

        with open("info/misc1.txt", "w") as text_file:
            text_file.write("%s" % self.textboxC.text())

        with open("info/misc2.txt", "w") as text_file:
            text_file.write("%s" % self.textboxD.text())

    def display_info(self):
        msgBox = QtGui.QMessageBox()
        msgBox.setText("Zhiyuan Liu, 2016. MyScoreboard.")
        msgBox.exec_()
        
    def close_application(self):
        sys.exit()
        
def main():
    app = QtGui.QApplication(sys.argv)
    GUI = Window()
    app.exec_()
    sys.exit()

main()