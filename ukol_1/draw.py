from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
import shapefile

class Draw(QTabWidget):
    # First initialization
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)

        #Query point and polygon
        self.__q = QPointF(0,0)
        self.__pol = QPolygonF()
        self.__add_vertex = False
        self.__results = []


    # Loading data function
    def setPath(self, width, height):
        # Store the filename data
        file = QFileDialog.getOpenFileName(None, "Select SHP", "", "SHP files (*.shp)")

        # Return previous polygon if dialog box cancelled
        if bool(file[0]) == False:
            return self.__pol

        # Store the path
        path = file[0]

        # Read shapefile from path
        shpfl = shapefile.Reader(path)
        polygons = shpfl.shapes()

        # Load x,y coordinates from shapefile
        x = []
        y = []
        for k in range(len(shpfl)):
            pol_x = []
            pol_y = []
            for point in polygons[k].points:
                pol_x.append(point[0])
                pol_y.append(point[1])
            x.append(pol_x)
            y.append(pol_y)

        # Rescale loaded shapefile to screen resolution
        flat_x = []
        flat_x = [item for sublist in x for item in sublist]
        flat_y = []
        flat_y = [item for sublist in y for item in sublist]
        min_x = min(flat_x)
        min_y = min(flat_y)

        # Shift to the origin
        for i in range(len(x)):
            for j in range(len(x[i])):
                x[i][j] = (x[i][j] - min_x)
                y[i][j] = (y[i][j] - min_y)

        # Get the interval extent
        flat_xn = []
        flat_xn = [item for sublist in x for item in sublist]
        flat_yn = []
        flat_yn = [item for sublist in y for item in sublist]
        max_xn = max(flat_xn)
        max_yn = max(flat_yn)

        # Initialise the length of pol
        self.__pol = [0] * len(x)

        # Normalise to the interval from 0 to 1
        for i in range(len(x)):
            self.__pol[i] = QPolygonF()
            for j in range(len(x[i])):
                x[i][j] = int(x[i][j] / max_xn * width)
                y[i][j] = int(height - (y[i][j] / max_yn * height))
                p = QPointF(x[i][j], y[i][j])
                self.__pol[i].append(p)
        return self.__pol

    # MouseClick function
    def mousePressEvent(self, e:QMouseEvent):
        # Coordinates of mouse
        x = e.position().x()
        y = e.position().y()
        self.__q.setX(x)
        self.__q.setY(y)
        # Repaint screen
        self.repaint()

    # Paint Function
    def paintEvent(self, e:QPaintEvent):
        # Create graphic object
        qp = QPainter(self)

        # Start draw
        qp.begin(self)

        # Painting standard and results polygons
        for pol in self.__pol:
            qp.setPen(Qt.GlobalColor.blue)
            qp.setBrush(Qt.GlobalColor.white)
            qp.drawPolygon(pol)
        if len(self.__results) > 0:
            for pol in self.__results:
                qp.setPen(Qt.GlobalColor.darkMagenta)
                qp.setBrush(Qt.GlobalColor.magenta)
                qp.drawPolygon(pol)

        # Set attributes for point
        qp.setPen(Qt.GlobalColor.red)
        qp.setBrush(Qt.GlobalColor.yellow)

        # Draw point
        d = 10
        qp.drawEllipse(int((self.__q.x() - d/2)), int((self.__q.y() - d/2)), d, d)

        # End draw
        qp.end()

    # Move point or add vertex
    def switchsource(self):
        self.__add_vertex = not(self.__add_vertex)

    # Get point, standard and result polygon functions
    def getPoint(self):
        return self.__q
    def getPolygon(self):
        return self.__pol
    def getResPol(self, pol: QPolygonF):
        self.__results.append(pol)

    # Deleting functions for point and polygons
    def clearPol(self):
        self.__pol = QPolygonF()
    def clearPoint(self):
        self.__q = QPointF()
    def clearResPol(self):
        # Remove results polygons
        self.__results = []