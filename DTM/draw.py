from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from QPoint3DF import *
from edge import *
from triangle import *
from random import *
from math import pi
import csv

class Draw(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # points, DT, contour lines, triangles
        self.__points: list[QPoint3DF] = []
        self.__dt: list[Edge] = []
        self.__contours: list[Edge] = []
        self.__emph_contours: list[Edge] = []
        self.__triangles: list[Triangle] = []


    def loadData(self, width, height):
        ###Load data from input file###
        filename, _ = QFileDialog.getOpenFileName(self, "Open file", "", "*.txt")

        #Create empty list of points if dialog window is closed
        if not filename:
            self.__points = []
            return self.__points

        #Initialize lists of coordinates
        x_list, y_list, z_list = [], [], []

        #Read file
        with open(filename, "r") as f:
            reader = csv.reader(f, delimiter='\t')
            for row in reader:
                x, y, z = map(float, row)
                x_list.append(x)
                y_list.append(y)
                z_list.append(z)

        #Get min and max x, y coordinates
        min_x, min_y = min(x_list), min(y_list)
        max_x, max_y = max(x_list), max(y_list)
        min_max = [min_x, min_y, max_x, max_y]

        #Rescale data to fit the window of application
        self.__points = []
        for x, y, z in zip(x_list, y_list, z_list):
            x = int(((x - min_x) / (max_x - min_x)) * width)
            y = int((height - (y - min_y) / (max_y - min_y) * height))
            p = QPoint3DF(x, y, z)
            self.__points.append(p)

        return self.__points


    def getAspectColor(self, aspect):
        ###Get aspect color###
        #Define color ranges for each direction
        color_ranges = [
            (11 / 8 * pi, 13 / 8 * pi, QColor(255, 165, 0)),  # North
            (13 / 8 * pi, 15 / 8 * pi, QColor(148, 0, 211)),  # Northeast
            (0, pi / 8, QColor(34, 139, 34)),  # East
            (pi / 8, 3 / 8 * pi, QColor(255, 192, 203)),  # Southeast
            (3 / 8 * pi, 5 / 8 * pi, QColor(0, 206, 209)),  # South
            (5 / 8 * pi, 7 / 8 * pi, QColor(255, 140, 0)),  # Southwest
            (7 / 8 * pi, 9 / 8 * pi, QColor(0, 255, 127)),  # West
            (9 / 8 * pi, 11 / 8 * pi, QColor(128, 0, 128))  # Northwest
        ]

        #Iterate through the color ranges and return color for the first matching range
        for r in color_ranges:
            if aspect >= r[0] and aspect < r[1]:
                return r[2]

        #Return white if no range matches
        return QColor(255, 255, 255)

    def paintEvent(self, e: QPaintEvent):
        ###Draw points and analyses of DTM###
        #Create graphic object
        qp = QPainter(self)

        #Start draw
        qp.begin(self)

        #Set attributes for points
        qp.setPen(Qt.GlobalColor.black)
        qp.setBrush(Qt.GlobalColor.white)

        #Draw points
        d = 5
        for p in self.__points:
            qp.drawEllipse(int(p.x() - d / 2), int(p.y() - d / 2), d, d)

        #Draw slope or aspect
        k = 510 / pi

        # process all triangles
        for t in self.__triangles:
            # get slope and aspect
            slope = t.getSlope()
            aspect = t.getAspect()

            #Draw slope
            if aspect == -1:
                # convert to color
                col = 255 - int(slope * k)

                #Create color
                color = QColor(col, col, col)
                qp.setBrush(color)

                #Create new polygon
                pol = QPolygonF([t.getP1(), t.getP2(), t.getP3()])

            #Draw aspect
            else:
               #Get aspect color
                color = self.getAspectColor(aspect)
                qp.setBrush(color)

                #Create new polygon
                pol = QPolygonF([t.getP1(), t.getP2(), t.getP3()])

            #Draw polygon
            qp.drawPolygon(pol)

        #Set attributes for triangles
        qp.setPen(Qt.GlobalColor.black)
        qp.setBrush(Qt.GlobalColor.transparent)

        #Draw triangles
        for e in self.__dt:
            qp.drawLine(int(e.getStart().x()), int(e.getStart().y()), int(e.getEnd().x()), int(e.getEnd().y()))

        #Set attributes for contour lines
        qp.setPen(Qt.GlobalColor.red)

        #Draw contour lines
        for c in self.__contours:
            qp.drawLine(int(c.getStart().x()), int(c.getStart().y()), int(c.getEnd().x()), int(c.getEnd().y()))

        #Set attributes for emphasized contour lines
        qp.setPen(QPen(Qt.GlobalColor.darkRed, 2))

        #Draw emphasized contour lines
        for c in self.__emph_contours:
            qp.drawLine(int(c.getStart().x()), int(c.getStart().y()), int(c.getEnd().x()), int(c.getEnd().y()))

        #End draw
        qp.end()

    def setDT(self, dt: list[Edge]):
        ###Set Delaunay triangulation###
        self.__dt = dt

    def getDT(self):
        ###Return Delaunay triangulation###
        return self.__dt

    def setContours(self, contours: list[Edge], emph_contours: list[Edge]):
        ###Set contour lines###
        self.__contours = contours
        self.__emph_contours = emph_contours

    def setTriangles(self, dtm: list[Triangle]):
        ###Set triangles###
        self.__triangles = dtm

    def getPoints(self):
        ###Return list of points###
        return self.__points

    def clearAll(self):
        ###Clear all results and points###
        self.__points: list[QPoint3DF] = []
        self.__dt: list[Edge] = []
        self.__contours: list[Edge] = []
        self.__emph_contours: list[Edge] = []
        self.__triangles: list[Triangle] = []
        self.repaint()

    def clearResults(self):
        ###Clear just results###
        self.__dt: list[Edge] = []
        self.__contours: list[Edge] = []
        self.__emph_contours: list[Edge] = []
        self.__triangles: list[Triangle] = []
        self.repaint()