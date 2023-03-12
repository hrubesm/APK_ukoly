# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QMainWindow, QMenu,
    QMenuBar, QSizePolicy, QStatusBar, QToolBar,
    QWidget)

from draw import Draw
import rc_Icons

class Ui_mainform(object):
    def setupUi(self, mainform):
        if not mainform.objectName():
            mainform.setObjectName(u"mainform")
        mainform.resize(800, 600)
        self.actionOpen = QAction(mainform)
        self.actionOpen.setObjectName(u"actionOpen")
        icon = QIcon()
        icon.addFile(u":/images/icons/open_file.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionOpen.setIcon(icon)
        self.actionExit = QAction(mainform)
        self.actionExit.setObjectName(u"actionExit")
        icon1 = QIcon()
        icon1.addFile(u":/images/icons/exit.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionExit.setIcon(icon1)
        self.actionPoint_Polygon = QAction(mainform)
        self.actionPoint_Polygon.setObjectName(u"actionPoint_Polygon")
        self.actionPoint_Polygon.setCheckable(True)
        self.actionPoint_Polygon.setChecked(True)
        self.actionClear = QAction(mainform)
        self.actionClear.setObjectName(u"actionClear")
        icon2 = QIcon()
        icon2.addFile(u":/images/icons/clear.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionClear.setIcon(icon2)
        self.actionPoint_Polygon_2 = QAction(mainform)
        self.actionPoint_Polygon_2.setObjectName(u"actionPoint_Polygon_2")
        icon3 = QIcon()
        icon3.addFile(u":/images/icons/polygon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionPoint_Polygon_2.setIcon(icon3)
        self.centralwidget = QWidget(mainform)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.Canvas = Draw(self.centralwidget)
        self.Canvas.setObjectName(u"Canvas")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Canvas.sizePolicy().hasHeightForWidth())
        self.Canvas.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.Canvas)

        mainform.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(mainform)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 17))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuDraw = QMenu(self.menubar)
        self.menuDraw.setObjectName(u"menuDraw")
        self.menuAnalyze = QMenu(self.menubar)
        self.menuAnalyze.setObjectName(u"menuAnalyze")
        mainform.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(mainform)
        self.statusbar.setObjectName(u"statusbar")
        mainform.setStatusBar(self.statusbar)
        self.toolBar_2 = QToolBar(mainform)
        self.toolBar_2.setObjectName(u"toolBar_2")
        mainform.addToolBar(Qt.TopToolBarArea, self.toolBar_2)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuDraw.menuAction())
        self.menubar.addAction(self.menuAnalyze.menuAction())
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuDraw.addAction(self.actionPoint_Polygon)
        self.menuDraw.addAction(self.actionClear)
        self.menuAnalyze.addAction(self.actionPoint_Polygon_2)
        self.toolBar_2.addAction(self.actionOpen)
        self.toolBar_2.addSeparator()
        self.toolBar_2.addAction(self.actionPoint_Polygon_2)
        self.toolBar_2.addSeparator()
        self.toolBar_2.addAction(self.actionClear)
        self.toolBar_2.addSeparator()
        self.toolBar_2.addAction(self.actionExit)

        self.retranslateUi(mainform)

        QMetaObject.connectSlotsByName(mainform)
    # setupUi

    def retranslateUi(self, mainform):
        mainform.setWindowTitle(QCoreApplication.translate("mainform", u"Point and polygon position", None))
        self.actionOpen.setText(QCoreApplication.translate("mainform", u"Open", None))
        self.actionExit.setText(QCoreApplication.translate("mainform", u"Exit", None))
        self.actionPoint_Polygon.setText(QCoreApplication.translate("mainform", u"Point/Polygon", None))
        self.actionClear.setText(QCoreApplication.translate("mainform", u"Clear", None))
        self.actionPoint_Polygon_2.setText(QCoreApplication.translate("mainform", u"Point and Polygon position", None))
#if QT_CONFIG(shortcut)
        self.actionPoint_Polygon_2.setShortcut(QCoreApplication.translate("mainform", u"Ctrl+P", None))
#endif // QT_CONFIG(shortcut)
        self.menuFile.setTitle(QCoreApplication.translate("mainform", u"File", None))
        self.menuDraw.setTitle(QCoreApplication.translate("mainform", u"Draw", None))
        self.menuAnalyze.setTitle(QCoreApplication.translate("mainform", u"Analyze", None))
        self.toolBar_2.setWindowTitle(QCoreApplication.translate("mainform", u"toolBar_2", None))
    # retranslateUi

