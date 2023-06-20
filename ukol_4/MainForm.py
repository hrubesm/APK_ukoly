# Form implementation generated from reading ui file 'form.ui'
#
# Created by: PyQt6 UI code generator 6.2.3
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
from algorithms import *
from draw import Draw
from settings import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Canvas = Draw(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Canvas.sizePolicy().hasHeightForWidth())
        self.Canvas.setSizePolicy(sizePolicy)
        self.Canvas.setObjectName("Canvas")
        self.horizontalLayout.addWidget(self.Canvas)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 17))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuElement = QtWidgets.QMenu(self.menubar)
        self.menuElement.setObjectName("menuElement")
        self.menuSimplify = QtWidgets.QMenu(self.menubar)
        self.menuSimplify.setObjectName("menuSimplify")
        self.menuOptions = QtWidgets.QMenu(self.menubar)
        self.menuOptions.setObjectName("menuOptions")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.ToolBarArea.TopToolBarArea, self.toolBar)
        #self.actionOpen = QtGui.QAction(MainWindow)
        #icon = QtGui.QIcon()
        #icon.addPixmap(QtGui.QPixmap("icons/open_file.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        #self.actionOpen.setIcon(icon)
        #self.actionOpen.setObjectName("actionOpen")
        self.actionElement = QtGui.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons/element.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionElement.setIcon(icon1)
        self.actionElement.setObjectName("actionElement")
        self.actionBarrier = QtGui.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icons/barrier.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionBarrier.setIcon(icon2)
        self.actionBarrier.setObjectName("actionBarrier")
        self.actionDisplace_1_element = QtGui.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("icons/displace.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionDisplace_1_element.setIcon(icon3)
        self.actionDisplace_1_element.setObjectName("actionDisplace_1_element")
        self.actionClear = QtGui.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("icons/clear.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionClear.setIcon(icon4)
        self.actionClear.setObjectName("actionClear")
        self.actionSettings = QtGui.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("icons/settings.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionSettings.setIcon(icon5)
        self.actionSettings.setObjectName("actionSettings")
        #self.menuFile.addAction(self.actionOpen)
        self.menuElement.addAction(self.actionElement)
        self.menuElement.addAction(self.actionBarrier)
        self.menuSimplify.addAction(self.actionDisplace_1_element)
        self.menuSimplify.addSeparator()
        self.menuSimplify.addAction(self.actionClear)
        self.menuOptions.addAction(self.actionSettings)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuElement.menuAction())
        self.menubar.addAction(self.menuSimplify.menuAction())
        self.menubar.addAction(self.menuOptions.menuAction())
        #self.toolBar.addAction(self.actionOpen)
        self.toolBar.addAction(self.actionElement)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionBarrier)
        self.toolBar.addAction(self.actionDisplace_1_element)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionSettings)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionClear)

        #User-defined actions
        #self.actionOpen.triggered.connect(self.input)
        self.actionDisplace_1_element.triggered.connect(self.displaceClick)
        #self.actionElement.triggered.connect(self.drawLineClick)
        #self.actionBarrier.triggered.connect(self.drawBarrierClick)
        self.actionClear.triggered.connect(self.clearClick)
        self.actionElement.triggered.connect(self.inputL)
        self.actionBarrier.triggered.connect(self.inputB)
        self.actionSettings.triggered.connect(self.settings)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuElement.setTitle(_translate("MainWindow", "Input"))
        self.menuSimplify.setTitle(_translate("MainWindow", "Simplify"))
        self.menuOptions.setTitle(_translate("MainWindow", "Options"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        #self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionElement.setText(_translate("MainWindow", "Element"))
        self.actionBarrier.setText(_translate("MainWindow", "Barrier"))
        self.actionDisplace_1_element.setText(_translate("MainWindow", "Displace 1 element"))
        self.actionClear.setText(_translate("MainWindow", "Clear"))
        self.actionSettings.setText(_translate("MainWindow", "Settings"))

    # Set parameters
    def __init__(self):
        self.__dmin = 100
        self.__alpha = 1
        self.__beta = 1000
        self.__gamma = 10
        self.__lam = 10
        self.__iters = 50

    # Settings
    def settings(self):
        dialog = SettingDialog(self.__dmin, self.__alpha, self.__beta, self.__gamma, self.__lam, self.__iters)
        # Get input values for signal accept
        if dialog.exec():
            dmin, alpha, beta, gamma, lam, iters = dialog.getInputs()
            self.__dmin = int(dmin)
            self.__alpha = float(alpha)
            self.__beta = float(beta)
            self.__gamma = float(gamma)
            self.__lam = float(lam)
            self.__iters = int(iters)
        else:
            return

    # Setting path for linear object
    def inputL(self):
        width = self.Canvas.frameGeometry().width()
        height = self.Canvas.frameGeometry().height()
        bar = False
        self.Canvas.setPath(width, height, bar)

    # Setting path for barrier object
    def inputB(self):
        width = self.Canvas.frameGeometry().width()
        height = self.Canvas.frameGeometry().height()
        bar = True
        self.Canvas.setPath(width, height, bar)

    def displaceClick(self):
        #Get polyline and barrier
        L = self.Canvas.getL()
        B = self.Canvas.getB()
        #print(len(L),"delka-l")
        #print(len(B),"delka-b")

        #Run displacement
        a = Algorithms()
        d, xq, yq = a.getPointLineDistance(100, 100, 0, 100, 100, 90)
        LD = a.minEnergySpline(L, B, self.__alpha, self.__beta, self.__gamma, self.__lam, self.__dmin, self.__iters)

        #Set results
        self.Canvas.setLD(LD)

        #Repaint
        self.Canvas.repaint()

    def drawLineClick(self):
        self.Canvas.setSource(True)

    def drawBarrierClick(self):
        self.Canvas.setSource(False)

    def clearClick(self):
        self.Canvas.clearAll()
        self.Canvas.repaint()
    # Closing app
    def exit(self):
        sys.exit(app.exec())


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())