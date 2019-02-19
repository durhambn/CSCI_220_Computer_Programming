from graphics import*
from random import *
import time
import math

## Name: Brandi Durham
## bumper.py
##
##Author: Zelle (pp. 103-04)
## Modified by Pharr to eliminate coordinates
##
##Problem: moves bumper cars(circles) around the ring(window), if they hit
##they bounce off each others or the wall
##
##Certification of Authenticity:
##    I certify that this lab is entirely my own work.


def getRandom(moveAmount):
    ranNum = randrange(-moveAmount, moveAmount, 20)
    return ranNum

# determines if balls collide
def didCollide(ball, ball2):
    rectp1 = Point(0,0)
    rectp2 = Point(400,400)
    center1 = ball.getCenter()
    center2 = ball2.getCenter()
    x1 = center1.getX()
    y1 = center1.getY()
    x2 = center2.getX()
    y2 = center2.getY()
    distance = math.sqrt((x1-x2)**2 + (y1-y2)**2)
    radius1 = ball.getRadius()
    radius2 = ball2.getRadius()
    totalRadius = radius1 + radius2
    if distance > totalRadius:
       rtnValue = False
    else:
       rtnValue = True
    return rtnValue

#determines if car hits sides
def hitVertical(ball, win):
    cenCarX = ball.getCenter().getX()
    if (cenCarX < 20) or (cenCarX >= 380):
        rtnVal = True
    else:
        rtnVal = False
    return rtnVal

#determines if car hits top or bottom
def hitHorizontal(ball, win):
    cenCar = ball.getCenter()
    valy = cenCar.getY()
    if (valy < 20) or (valy > 380):
        rtnVal = True
    else:
        rtnVal = False
    return rtnVal

#generates a random color from list
def randomColor():
    colorList = ["red", "blue", "green", "yellow", "purple", "pink", "orange"]
    ranColor = colorList[randrange(6)]
    return ranColor

def main():
    winHeight = 400
    winWidth = 400

    win = GraphWin("Bumper Car Simulator", winWidth, winHeight)

    car1 = Circle(Point(100, 50), 15)
    car1.draw(win)
    car1.setFill("Blue")

    car2 = Circle(Point(300, 50), 15)
    car2.draw(win)
    car2.setFill("Red")
    ranNum = getRandom(50)
    car1.move(ranNum, 30)
    ranNum2 = getRandom(50)
    car2.move(ranNum2, -20)
    time.sleep(.5)
    moveXCar1 = -30
    moveYCar1 = 30
    moveXCar2 = 20
    moveYCar2 = -20
    car1.move(moveXCar1, moveYCar1)
    car2.move(moveXCar2, moveYCar2)
    for i in range(30):
        rtnValue = didCollide(car1, car2)
        if rtnValue == True:
            moveXCar1 = -moveXCar1
            moveYCar1 = -moveYCar1
            moveXCar2 = -moveXCar2
            moveXCar2 = -moveYCar2
            car1.move(moveXCar1, moveYCar1)
            car2.move(moveXCar2, moveYCar2)
            car1.setFill(randomColor())
            car2.setFill(randomColor())
        else:
            car1.move(moveXCar1, moveYCar1)
            car2.move(moveXCar2, moveYCar2)
            
        rtn = hitVertical(car1, win)
        if rtn == True:
            moveXCar1 = -moveXCar1
            car1.move(moveXCar1, moveYCar1)
            car1.setFill(randomColor())
        else:
            car1.move(moveXCar1, moveYCar1)
            
        val = hitVertical(car2, win)
        if val == True:
            moveXCar2 = -moveXCar2
            car2.move(moveXCar2, moveYCar2)
            car2.setFill(randomColor())
        else:
            car2.move(moveXCar2, moveYCar2)
            
        hitH = hitHorizontal(car1, win)
        if hitH == True:
            moveYCar1 = -moveYCar1
            car1.move(moveXCar1, moveYCar1)
            car1.setFill(randomColor())
        else:
            car1.move(moveXCar1, moveYCar1)
            
        hitH2 = hitHorizontal(car2, win)
        if hitH2 == True:
            moveYCar2 = -moveYCar2
            car2.move(moveXCar2, moveYCar2)
            car2.setFill(randomColor())
        else:
            car2.move(moveXCar2, moveYCar2)
        time.sleep(.5)
    
            
            


        
        
    
