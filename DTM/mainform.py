from PyQt6 import QtCore, QtGui, QtWidgets
from draw import Draw
from algorithms import Algorithms


class Ui_MainForm(object):

    def setupUi(self, MainForm):
        MainForm.setObjectName("MainForm")
        MainForm.resize(800, 700)
        self.centralwidget = QtWidgets.QWidget(parent=MainForm)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Canvas = Draw(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Canvas.sizePolicy().hasHeightForWidth())
        self.Canvas.setSizePolicy(sizePolicy)
        self.Canvas.setObjectName("Canvas")
        self.horizontalLayout.addWidget(self.Canvas)
        MainForm.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainForm)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 872, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(parent=self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuAnalysis = QtWidgets.QMenu(parent=self.menubar)
        self.menuAnalysis.setObjectName("menuAnalysis")
        self.menuSettings = QtWidgets.QMenu(parent=self.menubar)
        self.menuSettings.setObjectName("menuSettings")
        self.menuView = QtWidgets.QMenu(parent=self.menubar)
        self.menuView.setObjectName("menuView")
        MainForm.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainForm)
        self.statusbar.setObjectName("statusbar")
        MainForm.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(parent=MainForm)
        self.toolBar.setObjectName("toolBar")
        MainForm.addToolBar(QtCore.Qt.ToolBarArea.TopToolBarArea, self.toolBar)
        self.actionCreate_DT = QtGui.QAction(parent=MainForm)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/triangles.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionCreate_DT.setIcon(icon)
        self.actionCreate_DT.setObjectName("actionCreate_DT")
        self.actionCreate_contour_lines = QtGui.QAction(parent=MainForm)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons/contours.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionCreate_contour_lines.setIcon(icon1)
        self.actionCreate_contour_lines.setObjectName("actionCreate_contour_lines")
        self.actionAnalyse_slope = QtGui.QAction(parent=MainForm)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icons/slope.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionAnalyse_slope.setIcon(icon2)
        self.actionAnalyse_slope.setObjectName("actionAnalyse_slope")
        self.actionAnalyse_aspect = QtGui.QAction(parent=MainForm)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("icons/orientation.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionAnalyse_aspect.setIcon(icon3)
        self.actionAnalyse_aspect.setObjectName("actionAnalyse_aspect")
        self.actionOpen = QtGui.QAction(parent=MainForm)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("icons/open_file.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionOpen.setIcon(icon4)
        self.actionOpen.setObjectName("actionOpen")
        self.actionExit = QtGui.QAction(parent=MainForm)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("icons/exit.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionExit.setIcon(icon5)
        self.actionExit.setObjectName("actionExit")
        self.actionContoursParameters = QtGui.QAction(parent=MainForm)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("icons/settings.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionContoursParameters.setIcon(icon6)
        self.actionContoursParameters.setObjectName("actionSetting")
        self.actionClear_results = QtGui.QAction(parent=MainForm)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("icons/clear1.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionClear_results.setIcon(icon7)
        self.actionClear_results.setObjectName("actionClear_results")
        self.actionClear_all = QtGui.QAction(parent=MainForm)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("icons/clear.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionClear_all.setIcon(icon8)
        self.actionClear_all.setObjectName("actionClear_all")
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionExit)
        self.menuAnalysis.addAction(self.actionCreate_DT)
        self.menuAnalysis.addAction(self.actionCreate_contour_lines)
        self.menuAnalysis.addAction(self.actionAnalyse_slope)
        self.menuAnalysis.addAction(self.actionAnalyse_aspect)
        self.menuSettings.addAction(self.actionContoursParameters)
        self.menuView.addAction(self.actionClear_results)
        self.menuView.addAction(self.actionClear_all)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuAnalysis.menuAction())
        self.menubar.addAction(self.menuSettings.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.toolBar.addAction(self.actionOpen)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionCreate_DT)
        self.toolBar.addAction(self.actionCreate_contour_lines)
        self.toolBar.addAction(self.actionAnalyse_slope)
        self.toolBar.addAction(self.actionAnalyse_aspect)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionContoursParameters)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionClear_results)
        self.toolBar.addAction(self.actionClear_all)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionExit)

        #Actions
        self.actionOpen.triggered.connect(self.openFile)
        self.actionCreate_DT.triggered.connect(self.runDT)
        self.actionCreate_contour_lines.triggered.connect(self.runContourLines)
        self.actionAnalyse_slope.triggered.connect(self.runSlope)
        self.actionAnalyse_aspect.triggered.connect(self.runAspect)
        self.actionClear_all.triggered.connect(self.clearAll)
        self.actionClear_results.triggered.connect(self.clearResults)
        self.actionExit.triggered.connect(sys.exit)
        self.actionContoursParameters.triggered.connect(self.setContourParameter)
        self.actionContoursParameters.triggered.connect(self.show_contour_parameters)


        self.retranslateUi(MainForm)
        QtCore.QMetaObject.connectSlotsByName(MainForm)

    def retranslateUi(self, MainForm):
        _translate = QtCore.QCoreApplication.translate
        MainForm.setWindowTitle(_translate("MainForm", "DTM analysis"))
        self.menuFile.setTitle(_translate("MainForm", "File"))
        self.menuAnalysis.setTitle(_translate("MainForm", "Analysis"))
        self.menuSettings.setTitle(_translate("MainForm", "Settings"))
        self.menuView.setTitle(_translate("MainForm", "View"))
        self.toolBar.setWindowTitle(_translate("MainForm", "toolBar"))
        self.actionCreate_DT.setText(_translate("MainForm", "Generate DT"))
        self.actionCreate_DT.setToolTip(_translate("MainForm", "Generate Delaunay triangulation"))
        self.actionCreate_contour_lines.setText(_translate("MainForm", "Create contour lines"))
        self.actionAnalyse_slope.setText(_translate("MainForm", "Analyse slope"))
        self.actionAnalyse_slope.setToolTip(_translate("MainForm", "Analyse slope of DTM"))
        self.actionAnalyse_aspect.setText(_translate("MainForm", "Analyse aspect"))
        self.actionAnalyse_aspect.setToolTip(_translate("MainForm", "Analyse aspect of DTM"))
        self.actionOpen.setText(_translate("MainForm", "Open"))
        self.actionOpen.setToolTip(_translate("MainForm", "Open file"))
        self.actionExit.setText(_translate("MainForm", "Exit"))
        self.actionExit.setToolTip(_translate("MainForm", "Exit application"))
        self.actionContoursParameters.setText(_translate("MainForm", "Contour Parameters"))
        self.actionContoursParameters.setToolTip(_translate("MainForm", "Set contour lines parameters"))

        self.actionClear_results.setText(_translate("MainForm", "Clear results"))
        self.actionClear_all.setText(_translate("MainForm", "Clear all"))


    def openFile(self):
        ###Load points from input file###
        width = self.Canvas.frameSize().width()
        height = self.Canvas.frameSize().height()
        self.Canvas.loadData(width, height)


    def runDT(self):
        ###Delaunay triangulation###
        points = self.Canvas.getPoints()

        if points == []:
            return

        a = Algorithms()

        dt = a.createDT(points)

        self.Canvas.setDT(dt)
        self.Canvas.repaint()

    def runSlope(self):
        ###Analyze slope of triangles###
        #Get DT
        dt = self.Canvas.getDT()

        a = Algorithms()
        dtm = a.analyzeDTMSlope(dt)

        self.Canvas.setTriangles(dtm)
        self.Canvas.repaint()


    def runAspect(self):
        ###Analyze aspect###
        #Get DT
        dt = self.Canvas.getDT()

        a = Algorithms()
        dtm = a.analyzeDTMAspect(dt)

        self.Canvas.setTriangles(dtm)
        self.Canvas.repaint()

    #Default contours parameters
    def __init__(self):
        self.__contours_min = 0
        self.__contours_max = 400
        self.__contours_step = 10



    def runContourLines(self):
        ###Create contour lines###
        #Get DT
        dt = self.Canvas.getDT()

        #Create contour lines
        a = Algorithms()

        #Parameters
        contours, emph_contours = a.createContourLines(dt, self.__contours_min, self.__contours_max, self.__contours_step)

        self.Canvas.setContours(contours, emph_contours)
        self.Canvas.repaint()

    def setContourParameter(self, parameter):
        ###Setting Countours parameters###
        if parameter == "min":
            cmin, ok = QtWidgets.QInputDialog.getInt(self.Canvas, "Contour lines minimum", "Set contour lines minimum", value=self.__contours_min)
            if ok:
                self.__contours_min = cmin
        elif parameter == "max":
            cmax, ok = QtWidgets.QInputDialog.getInt(self.Canvas, "Contour lines maximum", "Set contour lines maximum", value=self.__contours_max)
            if ok:
                self.__contours_max = cmax
        elif parameter == "step":
            step, ok = QtWidgets.QInputDialog.getInt(self.Canvas, "Contour lines step", "Set contour lines step", value=self.__contours_step)
            if ok:
                self.__contours_step = step

    def show_contour_parameters(self):
        ###Dialog box with parameters###
        contour_dialog = QtWidgets.QDialog()
        contour_dialog.setWindowTitle("Contour parameters")
        contour_dialog.setModal(True)

        #Buttons
        min_button = QtWidgets.QPushButton(f"Set minimum", contour_dialog)
        min_button.move(50, 50)
        min_button.clicked.connect(lambda: self.setContourParameter("min"))

        max_button = QtWidgets.QPushButton(f"Set maximum", contour_dialog)
        max_button.move(50, 100)
        max_button.clicked.connect(lambda: self.setContourParameter("max"))

        step_button = QtWidgets.QPushButton(f"Set step", contour_dialog)
        step_button.move(50, 150)
        step_button.clicked.connect(lambda: self.setContourParameter("step"))

        ok_button = QtWidgets.QPushButton("OK", contour_dialog)
        ok_button.move(50, 200)
        ok_button.clicked.connect(lambda: [self.runContourLines(), contour_dialog.accept()])

        cancel_button = QtWidgets.QPushButton("Cancel", contour_dialog)
        cancel_button.move(150, 200)
        cancel_button.clicked.connect(contour_dialog.reject)

        #Showing dialog box
        contour_dialog.exec()

    def clearAll(self):
        ###Clear points and all results###
        self.Canvas.clearAll()

    def clearResults(self):
        ###Clear just results###
        self.Canvas.clearResults()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainForm = QtWidgets.QMainWindow()
    ui = Ui_MainForm()
    ui.setupUi(MainForm)
    MainForm.show()
    sys.exit(app.exec())
