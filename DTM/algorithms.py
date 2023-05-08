from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from math import *
from QPoint3DF import *
from edge import *
from triangle import *

class Algorithms:
    def __init__(self):
        pass

    def get2LinesAngle(self, p1: QPoint3DF, p2: QPoint3DF, p3: QPoint3DF, p4: QPoint3DF):
        ###Compute angle between two lines###
        #Compute vectors
        ux = p2.x() - p1.x()
        uy = p2.y() - p1.y()
        vx = p4.x() - p3.x()
        vy = p4.y() - p3.y()

        #Dot product
        uv = (ux * vx) + (uy * vy)

        #Norms
        nu = sqrt(ux**2 + uy**2)
        nv = sqrt(vx**2 + vy**2)

        arg = uv / (nu * nv)
        arg = max(min(arg, 1), -1)

        return acos(arg)


    def getPointLinePosition(self, p: QPoint3DF, p1: QPoint3DF, p2: QPoint3DF):
        ###Point and line position###
        ux = p2.x() - p1.x()
        uy = p2.y() - p1.y()
        vx = p.x() - p1.x()
        vy = p.y() - p1.y()

        #Test criterion
        t = ux * vy - uy * vx

        #Point is in the left halfplane
        if t > 0:
            return 1

        #Point is in the right halfplane
        if t < 0:
            return 0

        #Colinear point
        return -1


    def getDelaunayPoint(self, p1: QPoint3DF, p2: QPoint3DF, points: list[QPoint3DF]):
        ###Find optimal Delaunay point###
        idx_max = -1
        om_max = 0

        #Process all points
        for i in range(len(points)):
            #Exclude identical points
            if (points[i] != p1) and (points[i] != p2):
                #Point in the left halfplane
                if self.getPointLinePosition(points[i], p1, p2) == 1:
                    #Compute angle
                    omega = self.get2LinesAngle(points[i], p1, points[i], p2)

                    # update maximum
                    if omega > om_max:
                        om_max = omega
                        idx_max = i

        return idx_max


    def getNearestPoint(self, p: QPoint3DF, points: list[QPoint3DF]):
        ###Find nearest point###
        idx_min = -1
        d_min = inf

        #Browse all points
        for i in range(len(points)):
            #Point p is different from points[i]
            if p == points[i]:
                continue
            #Compute distance
            dx = points[i].x() - p.x()
            dy = points[i].y() - p.y()
            d = sqrt(dx**2 + dy**2)

            #Update minimum
            if d < d_min:
                d_min = d
                idx_min = i

        return points[idx_min]

    def updateAEL(self, e: Edge, AEL: list[Edge]):
        ###Update of AEL###
        #Change orientation
        eo = e.switchOrientation()

        #Opposite edge in AEL
        if eo in AEL:
            AEL.remove(eo)
        #Opposite edge on in AEL
        else:
            AEL.append(e)


    def createDT(self, points: list[QPoint3DF]):
        ###Create Delaunay Triangulation###
        #Supplementary features
        dt: list[Edge] = []
        ael: list[Edge] = []

        #Find a point with the x coordinate
        p1 = min(points, key=lambda k: k.x())

        #Find nearest point to p1
        p2 = self.getNearestPoint(p1, points)

        #Create edge and opposite edge
        e = Edge(p1, p2)
        eo = Edge(p2, p1)

        #Add edges to AEL
        ael.append(e)
        ael.append(eo)

        #Process AEL until it is empty
        while ael:
            #Take the first edge
            e1 = ael.pop()

            #Switch orientation of e1
            e1o = e1.switchOrientation()

            #Get Delaunay point
            idx = self.getDelaunayPoint(e1o.getStart(), e1o.getEnd(), points)

            #If suitable point found
            if idx != -1:
                #Create remaining edges of the triangle
                e2 = Edge(e1o.getEnd(), points[idx])
                e3 = Edge(points[idx], e1o.getStart())

                #Add edges to DT
                dt.append(e1o)
                dt.append(e2)
                dt.append(e3)

                #Update AEL
                self.updateAEL(e2, ael)
                self.updateAEL(e3, ael)

        return dt


    def getContourLinePoint(self, p1: QPoint3DF, p2: QPoint3DF, z: float):
        ###Intersection of line and horizontal plane###
        xb = ((p2.x() - p1.x()) * (z - p1.getZ()) / (p2.getZ() - p1.getZ())) + p1.x()
        yb = ((p2.y() - p1.y()) * (z - p1.getZ()) / (p2.getZ() - p1.getZ())) + p1.y()

        return QPoint3DF(xb, yb, z)

    def createContourLines(self, dt: list[Edge], zmin: float, zmax: float, dz: float):
        ###Create contour lines inside the given interval and step###
        contours: list[Edge] = []
        emph_contours: list[Edge] = []

        #Process all triangles
        for i in range(0, len(dt), 3):
            #Get triangle vertices
            p1 = dt[i].getStart()
            p2 = dt[i].getEnd()
            p3 = dt[i+1].getEnd()

            #Get elevations of the points
            z1 = p1.getZ()
            z2 = p2.getZ()
            z3 = p3.getZ()

            #Test intersections of all planes
            for z in range(zmin, zmax, dz):
                #Get height differences
                dz1 = z - z1
                dz2 = z - z2
                dz3 = z - z3

                #Triangle is coplanar
                if (dz1 == 0) and (dz2 == 0) and (dz3 == 0):
                    continue

                #Edges (p1,p2) and (p2,p3) are intersected by plane
                if (dz1 * dz2 <= 0) and (dz2 * dz3 <= 0):
                    #Compute intersections
                    a = self.getContourLinePoint(p1, p2, z)
                    b = self.getContourLinePoint(p2, p3, z)
                    contours.append(Edge(a, b))

                    #Check for emphasized contour line
                    if z % (5*dz) == 0:
                        emph_contours.append(Edge(a, b))

                #Edges (p2,p3) and (p3,p1) are intersected by plane
                elif (dz2 * dz3 <= 0) and (dz3 * dz1 <= 0):
                    #Compute intersections
                    a = self.getContourLinePoint(p2, p3, z)
                    b = self.getContourLinePoint(p3, p1, z)
                    contours.append(Edge(a, b))

                    #Check for emphasized contour line
                    if z % (5 * dz) == 0:
                        emph_contours.append(Edge(a, b))

                #Edges (p3,p1) and (p1,p2) are intersected by plane
                elif (dz3 * dz1 <= 0) and (dz1 * dz2 <= 0):
                    #Compute intersections
                    a = self.getContourLinePoint(p3, p1, z)
                    b = self.getContourLinePoint(p1, p2, z)
                    contours.append(Edge(a, b))

                    #Check for emphasized contour line
                    if z % (5 * dz) == 0:
                        emph_contours.append(Edge(a, b))

        return contours, emph_contours


    def getNormVector(self, p1: QPoint3DF, p2: QPoint3DF, p3: QPoint3DF):
        ###Compute normal vector of triangle###
        #First vector
        ux = p2.x() - p1.x()
        uy = p2.y() - p1.y()
        uz = p2.getZ() - p1.getZ()

        #Second vector
        vx = p3.x() - p1.x()
        vy = p3.y() - p1.y()
        vz = p3.getZ() - p1.getZ()

        #Normal vector components
        nx = uy * vz - uz * vy
        ny = -(ux * vz - uz * vx)
        nz = ux * vy - uy * vx

        return nx, ny, nz

    def getSlope(self, p1: QPoint3DF, p2: QPoint3DF, p3: QPoint3DF):
        ###Get triangle slope###
        #Get normal vector
        nx, ny, nz = self.getNormVector(p1, p2, p3)

        #Norm
        n = sqrt(nx*nx + ny*ny + nz*nz)

        #Compute slope
        return acos(nz / n)


    def getAspect(self, p1: QPoint3DF, p2: QPoint3DF, p3: QPoint3DF):
        ###Get triangle aspect###
        #Get normal vector
        nx, ny, nz = self.getNormVector(p1, p2, p3)

        #Return aspect
        aspect = atan2(ny, nx)

        if aspect < 0:
            return (aspect + 2 *pi)

        return aspect


    def analyzeDTMSlope(self, dt: list[Edge]):
        ###Analyze slope of triangles###
        dtm: list[Triangle] = []
        #Process all triangles
        for i in range(0, len(dt), 3):
            #Get triangle vertices
            p1 = dt[i].getStart()
            p2 = dt[i].getEnd()
            p3 = dt[i+1].getEnd()

            #Compute slope
            slope = self.getSlope(p1, p2, p3)

            #Create triangle
            triangle = Triangle(p1, p2, p3, slope, -1)

            # Add triangle to the list
            dtm.append(triangle)

        #Return analyzed DTM
        return dtm

    def analyzeDTMAspect(self, dt: list[Edge]):
        ###Analyze aspect of triangles###
        dtm: list[Triangle] = []

        #Process all triangles
        for i in range(0, len(dt), 3):
            # get triangle vertices
            p1 = dt[i].getStart()
            p2 = dt[i].getEnd()
            p3 = dt[i+1].getEnd()

            #Compute slope
            aspect = self.getAspect(p1, p2, p3)

            #Create triangle and add it to list
            triangle = Triangle(p1, p2, p3, -1, aspect)

            # Add triangle to the list
            dtm.append(triangle)

        #Return analyzed DTM
        return dtm
