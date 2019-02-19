#Name 1: Joshua Nichols
#Name 2: Brandi Durham

class Point:
    def __init__(self):
        self.xVal = 0
        self.yVal = 0

    def getX(self):
        return self.xVal
    
    def getY(self):
        return self.yVal

    def setX(self, value):
        if type(value) == int:
            self.xVal = value

    def setY(self, value):
        if type(value) == int:
            self.yVal = value
    
    def __str__(self):
        rtnStr = "(" + str(self.xVal) +"," + str(self.yVal)+ ")"
        return rtnStr
    
        
