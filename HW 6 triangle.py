## Name: Brandi Durham
## triangle.py
##
##Author: Zelle (pp. 103-04)
## Modified by Pharr to eliminate coordinates
##
##Problem: calculates the perimeter and area of a triangle
##
##Certification of Authenticity:
##    I certify that this lab is entirely my own work.


from graphics import *
import math

##Input: parameter- points to make a triangle
##Output: returns a triangle object
def makeTriangle(pt1, pt2, pt3):
    triangle = Polygon(pt1, pt2, pt3)
    triangle.setFill("peachpuff")
    triangle.setOutline("cyan")
    return triangle

##Input: parameter- two points
##Output: returns the Euclidean distance between the points
def distance(p1,p2):
    p1x = p1.getX()
    p1y = p1.getY()
    p2x = p2.getX()
    p2y = p2.getY()
    eDistance = math.sqrt((p1x-p2x)**2 + (p1y - p2y)**2)
    return eDistance

#Input: paramter- the triangle object
#Output: returns the perimeter
def perimeter(tri):
    triPoints = tri.getPoints()
    side1 = distance(triPoints[0], triPoints[1])
    side2 = distance(triPoints[1], triPoints[2])
    side3 = distance(triPoints[2], triPoints[0])
    per = side1 + side2 + side3
    return per

#Input: paramter- the triangle object
#Output: returns the area
def area(tri):
    triPoints = tri.getPoints()
    side1 = distance(triPoints[0], triPoints[1])
    pt1x = triPoints[0].getX()
    pt1y = triPoints[0].getY()
    pt2x = triPoints[1].getX()
    pt2y = triPoints[1].getY()
    middlePtx = pt2x - ((pt2x-pt1x)/2)
    middlePty = pt2y - ((pt2y-pt1y)/2)
    height = distance(triPoints[2], Point(middlePtx,middlePty))
    triArea = .5 * side1 * height
    return triArea

    
def main():
    winWidth = 400
    winHeight = 400
    
    win = GraphWin("Draw a Triangle", winWidth, winHeight)
    message = Text(Point(winWidth/2, winHeight-10), "Click on three points")
    message.draw(win)

    # Get and draw three vertices of a triangle
    p1 = win.getMouse()
    p1.draw(win)
    p2 = win.getMouse()
    p2.draw(win)
    p3 = win.getMouse()
    p3.draw(win)

    triangle = makeTriangle(p1,p2,p3)
    triangle.draw(win)


    per = perimeter(triangle)
    message2 = Text(Point(200,350), "Perimeter of the triangle is: " +str(per))
    message2.draw(win)


    triArea = area(triangle)
    message3 = Text(Point(200, 370), "Area of triangle is: " +str(triArea))
    message3.draw(win)

    
    message.setText("Click anywhere to quit")
    win.getMouse()
    win.close()
    

main()
