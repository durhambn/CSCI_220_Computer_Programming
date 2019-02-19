#Name 1: Joshua Nichols
#Name 2: Brandi Durham

from point import Point
import math

class Circle:
    def __init__(self, x, y, radius):
        self.center = Point()
        self.center.setX(x)
        self.center.setY(y)
        self.radius = radius

    def getCenter(self):
        return self.center

    def getRadius(self):
        return self.radius

    def setCenter(self, xVal, yVal):
        self.center.setX(xVal)
        self.center.setY(yVal)

    def setRadius(self, r):
        if (type(r) == float or type(r) == int) and r > 0:
            self.radius = r

    def area(self):
        PI = math.pi
        area = PI * self.radius**2
        return area

    def __str__(self):
        rtnStr = "Circle: \nCenter: " +str(self.center)
        rtnStr += "\nRadius: " +str(self.radius)
        rtnStr += "\nArea: " +str(self.area())
        return rtnStr
