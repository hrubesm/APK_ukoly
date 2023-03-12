from PyQt6.QtGui import *
from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
from math import *

class Algorithms:
    def __int__(self):
        pass

    # Function for getting a postion and an angle
    def getPositionAndAngle(self, q, i0, i1):
        eps = 1**(-19)
        # Vectors
        x_qi = i0.x() - q.x()
        y_qi = i0.y() - q.y()
        x_qi1 = i1.x() - q.x()
        y_qi1 = i1.y() - q.y()

        # Determinant
        det = x_qi*y_qi1 - x_qi1*y_qi

        # Position (right half-plane, left half-plane, colinear point)
        if det > eps:
            pos = 1
        elif det < -eps:
            pos = 0
        else:
            pos = -1

        # Numerator
        nu = x_qi*x_qi1 + y_qi*y_qi1

        # Denominator
        nrm_qi = (x_qi**2 + y_qi**2)**0.5
        nrm_qi1 = (x_qi1**2 + y_qi1**2)**0.5
        nrms = nrm_qi*nrm_qi1

        # Angle
        if nrms == 0:
            cos_a = 0
        else:
            cos_a = nu/nrms
            if cos_a > 1:
                cos_a = 1
            elif cos_a < -1:
                cos_a = -1
        omega = abs(acos(cos_a))

        # Position and angle
        return pos, omega

    # Function for a Winding Number method
    def getWindingNumber (self, q, pol):
        # Initializaton of deviation, lenght of polygon and sum of angles
        eps = 1**(-19)
        n = len(pol)
        omega_sum = 0

        # Proces all vertices
        for i in range(n):
            pos, omega = self.getPositionAndAngle(q, pol[i], pol[(i + 1) % n])

            # Point is in the left halfplane
            if pos == 1:
                omega_sum += omega

            # Point is a kolinear
            elif pos == -1:
                q_x = q.x()
                q_y = q.y()
                i_x = pol[i].x()
                i_y = pol[i].y()
                i1_x = pol[(i + 1) % n].x()
                i1_y = pol[(i + 1) % n].y()
                if (q_x - i_x) * (q_x - i1_x) <= 0 and (q_y - i_y) * (q_y - i1_y) <= 0:
                    return 1

            # Point is in the right halfplane
            else:
                omega_sum -= omega

        # Point is inside a polygon
        if abs(abs(omega_sum)-2*pi) < eps:
            return 1

        # Point is outside
        return 0

    # Function for a Ray Crossing method
    def getRayCrossing(self, q, pol):
        # Initializations of numbers of vercites and lenght of polygon
        kr = 0
        kl = 0
        n = len(pol)

        # Proces all vertices
        for i in range(n):

            # Reducing of coordinates
            xi = pol[i].x() - q.x()  # i-tý bod
            yi = pol[i].y() - q.y()
            xi1 = pol[(i + 1) % n].x() - q.x()
            yi1 = pol[(i + 1) % n].y() - q.y()

            # Point is vertex
            if xi == 0 and yi == 0:
                return 1

            # Computing of intersection
            if (yi1 - yi) == 0:
                continue
            else:
                xm = (xi1 * yi - xi * yi1) / (yi1 - yi)


            # Looking for a suitable segment
            # Right ray
            if (yi > 0) != (yi1 > 0) and xm > 0:
                kr += 1

            # Left ray
            elif (yi < 0) != (yi1 < 0) and xm < 0:
                kl += 1

        # Point is on boundary of polygon
        if (kr % 2) != (kl % 2):
            return 1

        # Point is inside polygon
        if (kr % 2) == 1:
            return 1
        # Point is outside
        return 0