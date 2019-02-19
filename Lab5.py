# Lab5.py
# Name 1: Brandi Durham
# Name 2: Stefan Veloff

from graphics import *
import math
def cupConverter():
    # Author: RoxAnn H. Stalvey, modified by Walter Pharr
    # Illustrates getting numeric input through graphics window
    winWidth = 300
    winHeight = 200
    win = GraphWin("Convert cups to milliliters", winWidth, winHeight)

    #Specify the message for the input box
    boxDesc = Text(Point(100, 50), "Input cups: ")
    boxDesc.draw(win)

    #Create the Entry object and set its default text to a number
    #  allowing the user to see what type of value is expected
    inp = Entry(Point(200, 50), 5)
    inp.setText("0")
    inp.draw(win)

    #Create a Text object for outputting the result
    output = Text(Point(150, 150), "")
    output.draw(win)

    #This button isn't necessary, but it makes a nice point for the user
    #  to click.  If you click anywhere in the window, the code reacts
    #  the same way.
    btPtX = winWidth/2
    btPtY = winHeight/2
    button = Text(Point(btPtX, btPtY), "Click")
    button.draw(win)
    border = Rectangle(Point(btPtX-35, btPtY-20), Point(btPtX+35, btPtY+20))
    border.draw(win)

    # Wait for a mouse click
    win.getMouse()

    # Discover intput and convert it to a number
    # If numeric input wasn't needed, simply omit the eval()
    cups = eval(inp.getText())
    win.getMouse()
    output.getText()

    #Calculate milliliter equivalent here
    
    #conversion values
    CUPS_TO_OZ = 8
    OZ_TO_ML = 29.57
    
    ounces = cups * CUPS_TO_OZ
    milliliters = ounces * OZ_TO_ML


    # Display output and change button
    output.setText("value entered = " + str(cups)+ "cups =" + str(milliliters))
    button.setText("Quit")
    
    # Wait for another click to exit
    win.getMouse()
    win.close()


def target():
    winWidth = 200
    winHeight = 200
    win = GraphWin("Archery Target", winWidth, winHeight)

    # Add code here to get the dimensions and draw the target
    centerPtx = winWidth/2
    centerPty = winHeight/2
    radius = winWidth/2/5
    center= Circle(Point(centerPtx,centerPty), radius)
    firstRing = Circle(Point(centerPtx,centerPty), radius *2)
    secondRing = Circle(Point(centerPtx,centerPty), radius * 3)
    thirdRing = Circle(Point(centerPtx,centerPty), radius *4 )
    fourthRing = Circle(Point(centerPtx,centerPty), radius *5)
    center.setFill("yellow")
    firstRing.setFill("red")
    secondRing.setFill("blue")
    thirdRing.setFill("black")
    fourthRing.setFill("white")
    fourthRing.draw(win)
    thirdRing.draw(win)
    secondRing.draw(win)
    firstRing.draw(win)
    center.draw(win)
 

    # Wait for another click to exit
    win.getMouse()
    win.close()



def triangle():
    winWidth = 500
    winHeight = 500
    win = GraphWin("Draw a Triangle", winWidth, winHeight)

    # Add code here to accept the mouse clicks, draw the triangle.
    # and display its area in the graphics window.
    points = []
    for i in range (3):
        clickPt = win.getMouse()
        clickPt.draw(win)
        points.append(clickPt)
    ptAx = points[0].getX()
    ptAy = points[0].getY()
    ptBx = points[1].getX()
    ptBy = points[1].getY()
    ptCx = points[2].getX()
    ptCy = points[2].getY()
    shape = Polygon(points)
    shape.draw(win)
    dx = ptCx - ptAx
    dy = ptCx - ptBx
    dz = ptAx - ptBx
    y1 = ptCy - ptAy
    y2 = ptCy - ptBy
    y3 = ptAy - ptBy
    lengthAB = math.sqrt((dz)**2 + (y3)**2)
    lengthAC = math.sqrt((dx)**2 + (y1)**2)
    lengthBC = math.sqrt((dy)**2 + (y2)**2)
    per = lengthAB + lengthAC + lengthBC
    s = (per) / 2
    area = math.sqrt(s * (s - lengthAB) * (s - lengthAC) * (s - lengthBC))
    output = Text(Point(250,475),"perimeter ="+str( per))
    output2 = Text(Point(250, 490), "Area = "+ str(area))
    output.draw(win)
    output2.draw(win)
    
    

    # Wait for another click to exit
    win.getMouse()
    win.close()

def colorShape():
    '''Create code to allow a user to color a shape by entering rgb amounts'''

    #create window
    winWidth = 400
    winHeight = 400
    win = GraphWin("Color Shape", winWidth, winHeight)
    win.setBackground("white")

    #create text instructions
    msg = "Enter color values between 0 - 255\nClick window to color shape"
    inst = Text(Point(winWidth/2, winHeight-20), msg)
    inst.draw(win)

    #create circle in window's center
    shape = Circle(Point(winWidth/2, winHeight/2 - 30), 50)
    shape.draw(win)

    #redTexPt is 50 pixels to the left and forty pixels down from center
    redTextPt = Point(winWidth/2 - 50, winHeight/2 + 40)
    redText = Text(redTextPt, "Red: ")
    redText.setTextColor("red")
    inpRed = Entry(Point(winWidth/2, winHeight/2 +40), 5)
    inpRed.draw(win)
    

                   
    

    #greenTextPt is 30 pixels down from red
    greenTextPt = redTextPt.clone()
    greenTextPt.move(0,30)
    greenText = Text(greenTextPt, "Green: ")
    greenText.setTextColor("green")
    inpGreen = Entry(Point(winWidth/2, winHeight/2 +70), 5)
    inpGreen.draw(win)
    

    #blueTextPt is 60 pixels down from red
    blueTextPt = redTextPt.clone()
    blueTextPt.move(0,60)
    blueText = Text(blueTextPt, "Blue: ")
    blueText.setTextColor("blue")
    inpBlue = Entry(Point(winWidth/2, winHeight/2 +100), 5)
    inpBlue.draw(win)
    

    



    #display rgb text
    redText.draw(win)
    greenText.draw(win)
    blueText.draw(win)
    win.getMouse()
    red = int(inpRed.getText())
    green = int(inpGreen.getText())
    blue = int(inpBlue.getText())
    color = color_rgb(red, green, blue)
    shape.setFill(color)
    

def anotherSeries ():
    total = 0 
    numterms = eval(input("Input # of terms:"))
    for i in range (numterms):
        total = total + (i%3) *2 +2
    print (total)
    

    
    
def main():
    cupConverter()
    target()
    triangle()
    colorShape()







