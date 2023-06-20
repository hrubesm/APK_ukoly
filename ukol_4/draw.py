from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
import shapefile
import csv
from math import *

class Draw(QWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        #Query point and polygon
        self.__add_L = True
        self.__L = QPolygonF()
        self.__B = QPolygonF()
        self.__LD = QPolygonF()
        self.__q = QPointF(0, 0)
        self.__pol = []
        self.__min_max = []
        self.__add_vertex = False
        self.__results = []

        #self.__add_vertex = True

        #p1 = QPointF(0, 150)
        #p2 = QPointF(100, 100)
        #p3 = QPointF(200, 150)
        #self.__L.append(p1)
        #self.__L.append(p2)
        #self.__L.append(p3)

        #p4 = QPointF(0, 100)
        #p5 = QPointF(100, 90)
        #p6 = QPointF(200, 100)

        #self.__B.append(p4)
        #self.__B.append(p5)
        #self.__B.append(p6)

    # Setting path for input data
    def setPath(self, width, height, bar):
        filename = QFileDialog.getOpenFileName(self, "Open file", "", "*.txt")
        path = filename[0]

        # Return loaded L and B if dialog window is closed
        if bool(filename[0]) == False:
            if bar == True:
                return self.__B
            else:
                return self.__L

        # initialize lists of coordinates
        x_list = []
        y_list = []

        # Reading of input file
        with open(path, "r", encoding='utf-8-sig') as f:
            for row in csv.reader(f, delimiter='\t'):
                # extract coordinates and convert them to float
                x_list.append(float(row[0]))
                y_list.append(float(row[1]))

        # Setting minimum and maximum of coordinates
        if self.__min_max == []:
            self.__min_max = [min(x_list), min(y_list), max(x_list), max(y_list)]

        width = width - 300
        height = height - 300

        # rescale data to fit the window of application
        for i in range(len(x_list)):
            x = int(((x_list[i] - self.__min_max[0]) / (self.__min_max[2] - self.__min_max[0]) * width)) + 150
            y = int((height - (y_list[i] - self.__min_max[1]) / (self.__min_max[3] - self.__min_max[1]) * (height))) + 150
            p = QPointF(x, y)

            # add point to L
            if bar == False:
                self.__L.append(p)

            # add point to B
            else:
                self.__B.append(p)

    def paintEvent(self, e:QPaintEvent):
        #Draw polygon

        #Create graphic object
        qp = QPainter(self)

        #Start draw
        qp.begin(self)

        #Set attributes
        qp.setPen(Qt.GlobalColor.black)

        #Draw L
        qp.drawPolyline(self.__L)

        # Set attributes
        qp.setPen(Qt.GlobalColor.blue)

        # Draw B
        qp.drawPolyline(self.__B)

        # Set attributes
        qp.setPen(Qt.GlobalColor.red)

        # Draw LD
        #for line in self.__LD:
        qp.drawPolyline(self.__LD)

        #End draw
        qp.end()

    def switchSource(self):
        #Move point or add vertex
        self.__add_vertex = not(self.__add_vertex)

    def getL(self):
        return self.__L

    def getB(self):
        return self.__B

    def setLD(self, LD_):
        self.__LD = LD_

    def setSource(self, status):
        self.__add_L = status

    def clearAll(self):
        self.__L.clear()
        self.__B.clear()
        self.__LD.clear()

